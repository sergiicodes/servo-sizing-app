from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import os

app = Flask(__name__, static_folder='static')

app.secret_key = '445'  # replace with your own secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get data from POST request and process it
        data = request.form
        gbx_type = data.get('gbx')
        peak_speed = float(data.get('peak_speed'))
        peak_torque_input = float(data.get('peak_torque_input'))
        peak_acceleration = float(data.get('peak_acceleration'))
        max_inertia = float(data.get('max_inertia')) / 10000

        # Pandas Read
        current_dir = os.path.dirname(os.path.abspath(__file__))
        location = os.path.join(current_dir, 'AnalyzerSelection.xlsx')
        df_gbx = pd.read_excel(location, sheet_name="GBX DATABASE")
        df_servo = pd.read_excel(location, sheet_name="SERVO DATABASE")

        # Read Gearbox Specs from Excel Database 
        gbx_name = df_gbx.iloc[1:, 1].astype(str).str.strip()
        gbx_ratio = pd.to_numeric(df_gbx.iloc[1:,3], errors='coerce')
        gbx_speed = pd.to_numeric(df_gbx.iloc[1:,4], errors='coerce')
        gbx_torque = pd.to_numeric(df_gbx.iloc[1:,5], errors='coerce')
        gbx_inertia = pd.to_numeric(df_gbx.iloc[1:,6], errors='coerce')
        gbx_cost = pd.to_numeric(df_gbx.iloc[1:,7], errors='coerce')

        # Inputs
        if gbx_type == "Cone Drive":
            first_three_letters = "S"
        else:
            first_three_letters = gbx_type[:4]  # Get the first three letters of the selected gearbox type

        # Filter the gbx_name column based on the first three letters of gearbox names
        selected_gbx_names = gbx_name[gbx_name.str.startswith(first_three_letters)]

        # Calculate the new speed for each selected gearbox
        new_speeds = []
        for ratio in gbx_ratio[gbx_name.str.startswith(first_three_letters)]:
            new_speeds.append(ratio * peak_speed)


        # Read Servo Specs from Excel Database 
        servo_name = df_servo.iloc[1:, 1].astype(str).str.strip().dropna()
        servo_peak_torque = pd.to_numeric(df_servo.iloc[1:,3], errors='coerce').dropna()
        servo_velocity = pd.to_numeric(df_servo.iloc[1:,4], errors='coerce').dropna()
        servo_inertia = pd.to_numeric(df_servo.iloc[1:,6], errors='coerce').dropna()
        servo_cost = pd.to_numeric(df_servo.iloc[1:,7], errors='coerce').dropna()


        seen_combinations = set()
        # Create a list of dictionaries with the desired columns
        results = []
        for name, ratio, gbxSpeed, gbxTq, gbxInertia in zip(selected_gbx_names, gbx_ratio[gbx_name.str.startswith(first_three_letters)], gbx_speed[gbx_name.str.startswith(first_three_letters)], gbx_torque[gbx_name.str.startswith(first_three_letters)], gbx_inertia[gbx_name.str.startswith(first_three_letters)]):
            new_speed = ratio * peak_speed
            for servo, velocity, servocost, peak_torque, ServoInertia in zip(servo_name, servo_velocity, servo_cost, servo_peak_torque, servo_inertia):

                # Calculations 
                post_gbx_torque = round((peak_torque_input) / ((ratio) * ((1 - ((max_inertia* peak_acceleration) / (peak_torque * ratio))))), 2)
                
                servo_percentage_speed = round(((new_speed / velocity) * 100), 2)
                servo_percentage_peak_torque = round(((post_gbx_torque / peak_torque) * 100), 2)
                
                gbx_speed_protect = round((( (peak_speed  * ratio) / gbxSpeed) * 100) , 2)
                gbx_torque_protect = round((( peak_torque_input / gbxTq) * 100), 2)
                
                inertia_ratio = round(((((max_inertia * (1/(ratio**2))) + (gbxInertia/10000)) / (ServoInertia/10000))), 2)
                
                combination = None
                
                if (servo_percentage_speed <= 80) and (servo_percentage_peak_torque <= 80) and (gbx_speed_protect <= 80) and (gbx_torque_protect <= 80) and (servo_percentage_peak_torque >= 0) and (inertia_ratio <= 10):
                    combination = (servo_percentage_speed, servo_percentage_peak_torque)      

                    if combination is not None and combination not in seen_combinations:
                        total_cost = round((servocost + gbx_cost[gbx_name == name].iloc[0]), 2)
                        seen_combinations.add(combination)
                        result = {"Servo": servo, "Gearbox Name": name, "% Speed [Servo]": servo_percentage_speed, "% Peak-Torque [Servo]": servo_percentage_peak_torque, "% Speed [GBX]": gbx_speed_protect, "% Torque [GBX]": gbx_torque_protect, "Inertia Ratio": inertia_ratio, "Total Cost": total_cost}
                        results.append(result)
                        
        # Convert the list of dictionaries to a pandas dataframe
        df_results = pd.DataFrame(results)
        html = df_results.to_html(table_id="resultsTable")

        with open(os.path.join(current_dir, 'templates', 'results_table.html'), 'w') as f:
            f.write(html)
            
        return redirect(url_for('results'))
    
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)

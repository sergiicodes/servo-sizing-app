# Gearbox-Servo Selection Web Application

## Project Description

In my day to day job as a Research & Development Engineer, I am tasked with observing either mechanical components or assemblies to machine/project. Here's an example of a given project I would be working on:
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/8c79e3d5-50be-4bcb-a1a2-91750caa03e4)
  
And then here's an assembly/part within the project: 
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/3c9c1513-6e27-4b91-b37d-82f47b855f01)

More specifically, I am in charge of ensuring that the servo motor and gearbox combination that will be used in the particular assembly is capable of the given application. The brand of servos I use at work are [Allen Bradley](https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/motion-control/rotary-servo-motors.html) and the brand of gearboxes I use are [WITTENSTEIN alpha
](https://alpha.wittenstein-us.com/). I created this web-app to improve on the [Motion Analyzer](https://motionanalyzer.rockwellautomation.com/)  tool used for sizing and selecting motor and drive solutions. I found Motion Analyzer to be a very manual tool, and I wanted to "automate" the process of finding the right servo and gearbox combination.

This project is a web application designed to aid in the selection of suitable gearbox and servo systems based on given input criteria. Users input their criteria (including peak speed, peak torque input, peak acceleration, and maximum inertia), and the application cross-references these inputs with a provided database to offer suitable options. The resulting selections, along with some calculated metrics, are then displayed on a web page in tabular form.

## Features

- Users can input their selection criteria including: peak speed, peak torque input, peak acceleration, and maximum inertia.
- The application cross-references these inputs with a database of gearbox and servo systems.
- The application then calculates the speed and torque percentages for the servo and gearbox, as well as the inertia ratio, based on the user's inputs.
- The application checks for combinations of gearboxes and servos that meet certain conditions (e.g., certain maximum percentages for speed and torque, and a maximum inertia ratio).
- Suitable combinations are displayed in a table, along with their calculated metrics and total cost.

## Usage

To use the application, follow these steps:

1. Ensure that the necessary database files (`AnalyzerSelection.xlsx`) are in the correct location on your local machine.
2. Run the Flask application (`app.py`).
3. Navigate to the displayed local URL (usually `localhost:5000`) in your web browser.
4. Input your selection criteria into the form on the web page and submit the form:
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/9c3be226-6fa4-4fc6-acba-0c96fa2a09c8)

6. The page will display a table of suitable combinations of gearboxes and servos based on your input criteria:
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/7ab687eb-bc7d-40c2-a963-8c568b5e9ebc)

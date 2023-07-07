# Gearbox-Servo Selection Web Application

## Project Description

In my day-to-day role as a Research & Development Engineer, I am often tasked with observing mechanical components and assemblies for various machine and project applications. Here's an example of a given project I would be working on:
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/8c79e3d5-50be-4bcb-a1a2-91750caa03e4)
  
And then here's an assembly/part within the project: 
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/3c9c1513-6e27-4b91-b37d-82f47b855f01)

To streamline the process of selecting the optimal servo motor and gearbox combination, I have developed the Gearbox-Servo Selection Web Application. This web application caters to Mechanical Systems Engineers and Motion Control Engineers specializing in analyzing and designing mechanical systems involving motion, specifically with [Allen Bradley](https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/motion-control/rotary-servo-motors.html) servo motors and [WITTENSTEIN alpha](https://alpha.wittenstein-us.com/) gearboxes. By automating the selection process, the web application addresses the challenges of manual calculations and time-consuming searches for suitable servo and gearbox combinations, improving on the [Motion Analyzer](https://motionanalyzer.rockwellautomation.com/)  tool used for sizing and selecting motor and drive solutions. I found Motion Analyzer to be a very manual tool, and I wanted to "automate" the process of finding the right servo and gearbox combination.

Users can input their selection criteria, including peak speed, peak torque input, peak acceleration, and maximum inertia, and the application cross-references these inputs with a comprehensive database. Leveraging a backend Python program, the application calculates the speed and torque percentages for the servo and gearbox, as well as the inertia ratio, based on user inputs. Combinations that meet specific conditions, such as maximum speed and torque percentages and a desired inertia ratio, are displayed in a user-friendly table format. Furthermore, the web application considers cost as a crucial factor in the selection process. Gearbox-Servo Selection Web Application significantly improves upon existing tools by automating and simplifying the process of finding the ideal servo and gearbox combination, empowering engineers to optimize mechanical performance and efficiency.

## Features

The Gearbox-Servo Selection Web Application offers the following features:

- **User Input Criteria**: Users can input their selection criteria, including peak speed, peak torque input, peak acceleration, and maximum inertia, into an intuitive web form.
- **Intelligent Cross-Referencing**: The application cross-references the user inputs with a comprehensive database of gearbox and servo systems to identify suitable combinations.
- **Automated Calculations**: Leveraging a backend Python program, the application automatically calculates the speed and torque percentages for the servo and gearbox, as well as the inertia ratio, based on the user's input criteria.
- **Condition Checks**: The application performs condition checks on the combinations, ensuring they meet specific requirements such as maximum speed and torque percentages and a desired inertia ratio.
- **Interactive Results Display**: Suitable combinations of gearboxes and servos are displayed in a tabular format on a web page, providing users with detailed metrics and information.
- **Cost Consideration**: The web application incorporates cost as an important factor in the selection process, allowing users to evaluate and compare the financial aspects of different combinations.
- **Intuitive User Experience**: The web application offers a user-friendly interface that simplifies the process of selecting suitable servo and gearbox systems.
- **Optimization and Efficiency**: By automating the selection process, engineers can optimize mechanical performance and efficiency, saving time and effort in the design phase.

## Usage

To use the application, follow these steps:

1. Ensure that the necessary database files (`AnalyzerSelection.xlsx`) are in the correct location on your local machine.
2. Run the Flask application (`app.py`).
3. Navigate to the displayed local URL (usually `localhost:5000`) in your web browser.
4. Input your selection criteria into the form on the web page and submit the form:
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/9c3be226-6fa4-4fc6-acba-0c96fa2a09c8)

6. The page will display a table of suitable combinations of gearboxes and servos based on your input criteria:
![image](https://github.com/sergiicodes/servo-sizing-app/assets/79073281/7ab687eb-bc7d-40c2-a963-8c568b5e9ebc)

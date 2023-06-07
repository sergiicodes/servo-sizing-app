# Gearbox-Servo Selection Web Application

## Project Description

This project is a web application designed to aid in the selection of suitable gearbox and servo systems based on given input criteria. Users input their criteria (including peak speed, peak torque input, peak acceleration, and maximum inertia), and the application cross-references these inputs with a provided database to offer suitable options. The resulting selections, along with some calculated metrics, are then displayed on a web page in tabular form.

## Features

- Users can input their selection criteria, including peak speed, peak torque input, peak acceleration, and maximum inertia.
- The application cross-references these inputs with a database of gearbox and servo systems.
- The application then calculates the speed and torque percentages for the servo and gearbox, as well as the inertia ratio, based on the user's inputs.
- The application checks for combinations of gearboxes and servos that meet certain conditions (e.g., certain maximum percentages for speed and torque, and a maximum inertia ratio).
- Suitable combinations are displayed in a table, along with their calculated metrics and total cost.

## Usage

To use the application, follow these steps:

1. Ensure that the necessary database files (`Analyzer Selection2.xlsx`) are in the correct location on your local machine.
2. Run the Flask application (`app.py`).
3. Navigate to the displayed local URL (usually `localhost:5000`) in your web browser.
4. Input your selection criteria into the form on the web page and submit the form.
5. The page will display a table of suitable combinations of gearboxes and servos based on your input criteria.

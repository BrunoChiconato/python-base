#!/usr/bin/env python3
"""
Temperature Alert System

Make a program that asks for the actual temperature and the umidity level.
Depending on the temperature and the umidity level, the program will display a message to alert the user of the following situations:

- If the temperature is higher than 45 degrees: "Alert! High temperature".
- If the temperature is 3 times bigger or equals to the umidity level: "Alert! High temperature and humidity".
- If the temperature is between 10 and 30 degrees: "The temperature is ok".
- If the temperature is between 0 and 10 degrees: "Alert! Low temperature".
- If the temperature is lower than 0 degrees: "Alert! Extremely low temperature".
"""

try:
    temperature = float(input("Enter the temperature: "))
    umidity_level = float(input("Enter the umidity level: "))

    if temperature >= 3 * umidity_level:
        print("Alert! High temperature and humidity")
    elif temperature > 45:
        print("Alert! High temperature")
    elif temperature >= 10 and temperature <= 30:
        print("The temperature is ok")
    elif temperature >= 0 and temperature < 10:
        print("Alert! Low temperature")
    elif temperature < 0:
        print("Alert! Extremely low temperature")
except ValueError:
    print("Please enter a valid number.")

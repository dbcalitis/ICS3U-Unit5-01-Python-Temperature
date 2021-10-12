#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program does temperature conversion


def fahrenheit():
    # This function converts Celcius to Fahrenheit
    # input
    celcius_temp = input("Enter a temperature (°C): ")

    # process & output
    try:
        celcius_temp = float(celcius_temp)
        fahrenheit_temp = round((9 / 5) * celcius_temp + 32, 1)
        print("{0}°C is equal to {1}°F.".format(celcius_temp, fahrenheit_temp))
    except (Exception):
        print("Invalid Input.")


def main():
    # This function is the main function
    fahrenheit()

    print("\nDone.")


if __name__ == "__main__":
    main()

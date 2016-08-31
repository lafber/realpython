''' Real Python
    Assignment: Convert temperatures
    
'''

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_celsius = float(input('Entrez une température en degrés celsius : '))

print("{}°C = {}°F".format(temperature_celsius, celsius_to_fahrenheit(temperature_celsius)))

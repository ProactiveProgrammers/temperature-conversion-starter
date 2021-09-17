"""Convert from Celsius to Fahrenheit and from Fahrenheit to Celsius."""

from converter import units


def convert_celsius_to_fahrenheit(temperature: float):
    """Convert the provided temperature from Celsius to Fahrenheit."""
    # TODO: convert the temperature from Celsius to Fahrenheit
    # TODO: delete this placeholder return statement and add the correct one
    return 0


def convert_fahrenheit_to_celsius(temperature: float):
    """Convert the provided temperature from Fahrenheit to Celsius."""
    # TODO: convert the temperature from Fahrenheit to Celsius
    # TODO: delete this placeholder return statement and add the correct one
    return 0

def convert_temperature(
    temperature: float,
    from_unit: units.TemperatureUnitOfMeasurement,
    to_unit: units.TemperatureUnitOfMeasurement,
):
    """Convert a temperature given the from_unit and the to_unit."""
    converted_temperature = 0
    # the requested temperature conversion is Celsius --> Fahrenheit
    if from_unit.value == "Celsius" and to_unit.value == "Fahrenheit":
        # TODO: call the function that will convert from Celsius to Fahrenheit
    # the requested temperature conversion is Fahrenheit --> Celsius
    elif from_unit.value == "Fahrenheit" and to_unit.value == "Celsius":
        # TODO: call the function that will convert from Celsius to Fahrenheit
    return converted_temperature

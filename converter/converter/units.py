# TODO: Add a docstring comment to this file that explains it at a high-level

from enum import Enum

# TODO: Add at least one single-line comment that further explains the meaning
# and purpose of the source code in this file


class TemperatureUnitOfMeasurement(str, Enum):
    """Define an enumeration of the types of measurement units for temperature."""

    celsius = "Celsius"
    fahrenheit = "Fahrenheit"

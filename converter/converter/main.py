"""Perform temperature conversion between Fahrenheit and Celsius."""

from rich.console import Console

import typer

from converter import convert
from converter import units

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def converter(
    from_unit: units.TemperatureUnitOfMeasurement = units.TemperatureUnitOfMeasurement.celsius,
    to_unit: units.TemperatureUnitOfMeasurement = units.TemperatureUnitOfMeasurement.fahrenheit,
    temperature: float = typer.Option(98.6, min=-130, max=140),
):
    """Convert units.from Fahrenheit to Celsius or from Celsius to Fahrenheit."""
    # TODO: create a new Console object
    # TODO: display the two input parameters provided on the command line
    # TODO: perform the conversion of the temperature from one unit to another unit
    # TODO: display an extra blank line between the two entires
    # TODO: display the original temperature and then the converted temperature, always using units

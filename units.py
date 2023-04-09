from enum import Enum
from typing import Callable


ConversionFn = Callable[[float | int], float | int]


class Units(Enum):
    KM = "kilometers"
    M = "miles"
    N = "nautical miles"
    C = "˚ Celcius"
    F = "˚ Fahrenheit"
    K = "Kelvin"


def kilometer_to_miles(distance: float | int) -> float | int:
    return distance * 0.621371192


def miles_to_kilometer(distance: float | int) -> float | int:
    return distance * 1.609344


def kilometer_to_nautical_mile(distance: float | int) -> float | int:
    return distance * 0.539956803


def nautical_mile_to_kilometer(distance: float | int) -> float | int:
    return distance * 1.85200


def mile_to_nautical_mile(distance: float | int) -> float | int:
    return distance * 0.868976242


def nautical_mile_to_mile(distance: float | int) -> float | int:
    return distance * 1.15077945


def celcius_to_fahrenheit(degrees: float | int) -> float | int:
    return (degrees * 9/5) + 32


def fahrenheit_to_celcius(degrees: float | int) -> float | int:
    return (degrees-32) * 5/9


def celcius_to_kelvin(degrees: float | int) -> float | int:
    return degrees + 273.15


def kelvin_to_celcius(degrees: float | int) -> float | int:
    return degrees - 273.15


def fahrenheit_to_kelvin(degrees: float | int) -> float | int:
    return (degrees - 32) * 5/9 + 273.15


def kelvin_to_fahrenheit(degrees: float | int) -> float | int:
    return (degrees - 273.15) * 9/5 + 32


CONVERTER: dict[(Units, Units), ConversionFn] = {
    (Units.KM, Units.M): kilometer_to_miles,
    (Units.M, Units.KM): miles_to_kilometer,
    (Units.KM, Units.N): kilometer_to_nautical_mile,
    (Units.N, Units.KM): nautical_mile_to_kilometer,
    (Units.M, Units.N): mile_to_nautical_mile,
    (Units.N, Units.M): nautical_mile_to_mile,
    (Units.C, Units.F): celcius_to_fahrenheit,
    (Units.F, Units.C): fahrenheit_to_celcius,
    (Units.C, Units.K): celcius_to_kelvin,
    (Units.K, Units.C): kelvin_to_celcius,
    (Units.F, Units.K): fahrenheit_to_kelvin,
    (Units.K, Units.F): kelvin_to_fahrenheit,
}
import pytest

from validation.address import *

def test_zip_code_format_validation():
    valid_5_digits_zip = "22207"
    assert is_zip_code_format_valid(valid_5_digits_zip) == True
    invalid_5_digits_zip = "2A207"
    assert is_zip_code_format_valid(invalid_5_digits_zip) == False
    invalid_5_digits_zip = "22207-1234"
    assert is_zip_code_format_valid(invalid_5_digits_zip) == True
    invalid_5_digits_zip = "22207-12345"
    assert is_zip_code_format_valid(invalid_5_digits_zip) == False

def test_city_zip_code_pair_valid():
    zip = "22033"
    city = "Fairfax"
    assert is_city_zip_code_pair_valid(city, zip) == True


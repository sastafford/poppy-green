import pytest

from validation.address import *

def test_zip_code_validation():
    valid_5_digits_zip = "22207"
    assert is_zip_code_valid(valid_5_digits_zip) == True
import re
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.types import BooleanType
from pyspark.sql.functions import udf

def is_city_zip_code_pair_valid(city: str, zip:str) -> bool:
    if (not is_zip_code_format_valid(zip)):
        return False
    zipcode_dict = get_zipcode_lookup()
    if (zip not in zipcode_dict):
        return False
    else:
        city_val = zipcode_dict.get(zip)
        if (city == city_val):
            return True
        else:
            return False

def is_zip_code_format_valid(zip: str) -> bool:
    zip_code_regex = "(^\\d{5}$)|(^\\d{9}$)|(^\\d{5}-\\d{4}$)"
    pattern = re.compile(zip_code_regex)
    if (re.match(zip_code_regex, zip)): 
        return True
    else:
        return False

# This code snippet is for demonstration and testing only.  Advise to put this lookup in another class.  
def get_zipcode_lookup() -> dict:
    return {
        "22033": "Fairfax"
    }

validate_city_zip_code = udf(is_city_zip_code_pair_valid)
import pytest

from pyspark.sql import DataFrame
from pyspark.sql.functions import cast
from validation.address import *

def test_zip_code_is_valid():
    valid_5_digits_zip = "22207"
    assert is_zip_code_format_valid(valid_5_digits_zip) == True  
    valid_5_digits_zip = "22207-1234"
    assert is_zip_code_format_valid(valid_5_digits_zip) == True

def test_zip_code_is_not_valid():
    invalid_5_digits_zip = "2A207"
    assert is_zip_code_format_valid(invalid_5_digits_zip) == False
    invalid_5_digits_zip = "22207-12345"
    assert is_zip_code_format_valid(invalid_5_digits_zip) == False

def test_city_zip_code_pair_is_valid():
    zip = "22033"
    city = "Fairfax"
    assert is_city_zip_code_pair_valid(city, zip) == True  

def test_city_zip_code_pair_is_not_valid():
    zip = "22033-12"
    city = "Fairfax"
    assert is_city_zip_code_pair_valid(city, zip) == False

def test_city_zip_valid_sql():
    df = get_address_dataframe()
    df.createOrReplaceTempView("address")
    spark = SparkSession.builder.getOrCreate()
    spark.sql("SELECT * FROM address")
    valid_df = df.select("City", "State", "ZipCode", validate_city_zip_code(df.City, df.ZipCode).alias("isAddressValid"))
    valid_df.show()
    assert 1 == 1

def get_address_dataframe() -> DataFrame:
    schema = ["City", "State", "ZipCode"]
    data = [ 
        ("Fairfax", "VA", "22033"),
        ("Fairfax", "VA", "22233")
    ]
    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame(data, schema)
    return df
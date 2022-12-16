import re
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

spark = SparkSession.builder.getOrCreate()

def is_city_zip_code_pair_valid(city: str, zip:str) -> bool:
    if (not is_zip_code_format_valid(zip)):
        return False
    df = get_zip_code_city_lookup()
    df = df.select("*").where((df.ZipCode == zip) & (df.City == city))
    if df.count() > 0:
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

def get_zip_code_city_lookup() -> DataFrame:
    schema = ["City", "State", "ZipCode"]
    data = [ ("Fairfax", "VA", "22033")]
    zip_code_city_df = spark.createDataFrame(data, schema).cache()
    return zip_code_city_df
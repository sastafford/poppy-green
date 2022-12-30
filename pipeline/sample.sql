-- Databricks notebook source
-- MAGIC %python
-- MAGIC 
-- MAGIC from validation.address import validate_city_zip_code
-- MAGIC 
-- MAGIC schema = ["City", "State", "ZipCode"]
-- MAGIC data = [ 
-- MAGIC     ("Fairfax", "VA", "22033"),
-- MAGIC     ("Fairfax", "VA", "22233"),
-- MAGIC     ("Funfax", "VA", "22033")
-- MAGIC ]
-- MAGIC df = spark.createDataFrame(data, schema)

-- COMMAND ----------

-- MAGIC %python
-- MAGIC spark.udf.register("validateAddress", validate_city_zip_code)
-- MAGIC df.createOrReplaceTempView("address")

-- COMMAND ----------

SELECT *, validateAddress(City, ZipCode) as isAddressValid
FROM address

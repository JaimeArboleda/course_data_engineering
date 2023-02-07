import pandas as pd
from prefect import task, flow, get_run_logger
from prefect_gcp.bigquery import BigQueryWarehouse 
from typing import List
import requests

@task
def create_materialized_table() -> None:
    block = BigQueryWarehouse.load("zoom-bq")
    operation = """\
CREATE OR REPLACE TABLE `watchful-idea-375011.fhv_trips_data.tripdata_materialized`
AS SELECT * FROM `watchful-idea-375011.fhv_trips_data.tripdata`;
"""
    block.execute(operation)

@task
def create_external_table() -> None:
    block = BigQueryWarehouse.load("zoom-bq")
    operation = """\
CREATE OR REPLACE EXTERNAL TABLE `watchful-idea-375011.fhv_trips_data.tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://dtc_data_lake_watchful-idea-375011/fhv_tripdata/fhv_tripdata_2019-*.csv.gz']
);
"""
    block.execute(operation)

@flow
def create_table() -> None:
    create_external_table()
    create_materialized_table()

if __name__ == "__main__":
    create_table()
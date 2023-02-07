from io import BytesIO
from prefect import task, flow, get_run_logger
from prefect_gcp.cloud_storage import GcsBucket
from typing import List
import requests

BASE_REMOTE_PATH = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-MONTH.csv.gz"

@task
def fetch_data(month: int) -> bytes:
    month_str = f"{month:02d}"
    r = requests.get(BASE_REMOTE_PATH.replace("MONTH", month_str))
    return r.content

@task
def load_in_bucket(month: int, data: bytes) -> None:
    month_str = f"{month:02d}"
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.upload_from_file_object(BytesIO(data), f"fhv_tripdata/fhv_tripdata_2019-{month_str}.csv.gz")

@flow
def gcs_flow(months: list[int]) -> None:
    for month in months:
        data = fetch_data(month)
        load_in_bucket(month, data)

if __name__ == "__main__":
    months = list(range(1, 13))
    gcs_flow(months)
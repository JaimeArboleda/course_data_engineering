0. Loading datasets in Big Query

I decided to automate the process with two flows. The [first](gcs_flow.py) one, will load the files in a GCS bucket, respecting the .gz format. 
The [second](bq_flow.py) one, will take those files and create big query tables from them. I've run them using prefect cloud and the blocks defined in the previous week. 
For login in prefect cloud:
```bash
prefect cloud login
```
For spinning up a local agent:
```bash
prefect agent start --work-queue default
```

1. For this exercise and the rest, the queries are stored [here](bq.sql)
43244696

2. 317.94MB for the BQ Table and 0B for the external table.

3. 717748

4. Partition by pickup_datetime Cluster on affiliated_base_number, using a daily or monthly partitioning scheme. 

5. 647.87 MB for non partitioned. 23.05 MB for partitioned.

6. GCP Bucket

7. False. It depends on the use case. 

8. Not implemented, but it should be easy to modify the [flow](gcs_flow.py) to convert to parquet after downloading the data and then uploading the parquet file to GCS. 
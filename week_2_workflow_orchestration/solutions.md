# Solutions

1. In order to modify the flow, we have to change the parameters (color, year and month) and to modify the clean task because the datetimes columns start with "l" and not with "t".

The updated python script is [here](flows/03_deployments/parameterized_flow_homework.py)

The solution, looking at the logs in Prefect, is 447770 rows.

2. 0 5 1 * * is the specification of such a schedule in cron.

3. First we need to upload the data to the bucket, using the parametrized flow with parameters: 

```python
    color = "yellow"
    months = [2, 3]
    year = 2019
    etl_parent_flow(months, year, color)
```
Second, we adapt the etl_gcs_to_bq to make it parametrized and to remove the 't' part.
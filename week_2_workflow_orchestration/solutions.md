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
 
Third, we add log_prints to log the number of rows, which is 14851920 rows

The updated python script is [here](flows/02_gcp/etl_gcs_to_bq_homework.py)

4. I created the deployment with a Python script located [here](flows/03_deployments/parameterized_flow_homework_github.py). The deployment points to the parametrized flow version used in the first exercise. 

To run it, we used the UI with custom params.

Lastly, we run a local agent with `prefect agent start  --work-queue "default"`
 
88605 rows were processed. 

I had some problems with the relative paths in directories, so I used absolute paths.

5. I decided to use email notifications with Prefect Cloud. I created the account, , the automation, login in prefect cloud from the CLI and then I run the python script again.

To make it work, I needed to add the blocks I had locally in Orion to the Prefect Cloud. And the GPC block was created from code, [here](flows/03_deployments/blocks_cloud.py)
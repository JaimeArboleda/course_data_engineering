from prefect.deployments import Deployment
from parameterized_flow_homework import etl_parent_flow
from prefect.filesystems import GitHub 

storage = GitHub.load("github-de-zoomcamp")

deployment = Deployment.build_from_flow(
     flow=etl_parent_flow,
     name="github-example",
     storage=storage,
     entrypoint="week_2_workflow_orchestration/flows/03_deployments/parameterized_flow_homework.py:etl_parent_flow")

if __name__ == "__main__":
    deployment.apply()
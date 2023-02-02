from prefect_gcp import GcpCredentials 
from prefect_gcp.cloud_storage import GcsBucket    
                                                                      
gcp_credentials_block = GcpCredentials.load("zoom-de-credentials")  
                                                                          
GcsBucket(bucket="dtc_data_lake_watchful-idea-375011",                                   
          gcp_credentials=gcp_credentials_block                
          ).save("zoom-gcs")  
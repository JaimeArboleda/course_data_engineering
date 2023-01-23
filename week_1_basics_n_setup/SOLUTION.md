# Commands and SQL queries for completing the first part of assignment

```bash
docker build --help | grep Write
```

```bash
docker run -it --entrypoint /bin/bash python:3.9
pip list 
```

```sql
SELECT 
COUNT(*) 
FROM green_taxi_data
WHERE to_char(lpep_pickup_datetime, 'YYYY-MM-DD') = '2019-01-15' 
AND to_char(lpep_dropoff_datetime, 'YYYY-MM-DD') = '2019-01-15' 
```

```sql 
SELECT 
lpep_pickup_datetime 
FROM green_taxi_data
ORDER BY trip_distance 
DESC 
LIMIT 1
```

```sql
SELECT 
passenger_count, 
COUNT(*) 
FROM green_taxi_data
WHERE 
to_char(lpep_pickup_datetime, 'YYYY-MM-DD') = '2019-01-01' 
AND (passenger_count = 2 OR passenger_count = 3) 
GROUP BY passenger_count
```

```sql
SELECT 
green_taxi_data."PULocationID", 
green_taxi_data."DOLocationID", 
green_taxi_data.tip_amount, 
puzones."LocationID" as puzoneid, 
puzones."Zone" as puzone,
dozones."LocationID" AS dozoneid,
dozones."Zone" AS dozone
FROM
green_taxi_data
JOIN zones puzones ON "PULocationID" = puzones."LocationID"
JOIN zones dozones ON "DOLocationID" = dozones."LocationID"
WHERE
puzones."Zone" = 'Astoria'
ORDER BY 
tip_amount
DESC
LIMIT 1
```

# Commands and considerations for completing the second part 

* Configure a VM in GCP
* Configure a ssh connection to the VM in GCP (creating a .ssh folder in the home directory, and using the IP address of the machine)
* Install all needed software including terraform
* Clone the git project
* Copy a GCP service account (json file) to authenticate to google cloud from the VM
* Follow the instructions for connecting to GCP from the command line.
* Apply all terraform commands.

The videos for those tasks are: 
* https://www.youtube.com/watch?v=Hajwnmj0xfQ&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=12&ab_channel=DataTalksClub%E2%AC%9B
* https://www.youtube.com/watch?v=dNkEgO-CExg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13&ab_channel=DataTalksClub%E2%AC%9B
* https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=14&ab_channel=DataTalksClub%E2%AC%9B
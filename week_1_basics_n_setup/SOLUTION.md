# Commands and SQL queries for completing the assignments

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
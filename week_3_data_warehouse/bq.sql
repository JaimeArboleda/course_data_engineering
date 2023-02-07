SELECT COUNT(*) FROM `watchful-idea-375011.fhv_trips_data.tripdata_materialized`;


SELECT DISTINCT(Affiliated_base_number) FROM `watchful-idea-375011.fhv_trips_data.tripdata_materialized`;
SELECT DISTINCT(Affiliated_base_number) FROM `watchful-idea-375011.fhv_trips_data.tripdata`;


SELECT COUNT(*) FROM `watchful-idea-375011.fhv_trips_data.tripdata_materialized`
WHERE PUlocationID IS NULL AND DOlocationID IS NULL;


CREATE TABLE
`watchful-idea-375011.fhv_trips_data.tripdata_optimized` 
PARTITION BY
DATE(pickup_datetime)
CLUSTER BY 
Affiliated_base_number
AS (
SELECT * FROM `watchful-idea-375011.fhv_trips_data.tripdata_materialized` 
);


SELECT DISTINCT(Affiliated_base_number) 
FROM `watchful-idea-375011.fhv_trips_data.tripdata_materialized` 
WHERE DATE(pickup_datetime) BETWEEN '2019-03-01' AND '2019-03-31';

SELECT DISTINCT(Affiliated_base_number) 
FROM `watchful-idea-375011.fhv_trips_data.tripdata_materialized` 
WHERE DATE(pickup_datetime) BETWEEN '2019-03-01' AND '2019-03-31';
-- LC#584 - Find Customer Referee [Easy]
-- Topic: NULL Handling / WHERE clause
-- ML Connection: NULL-safe filtering mirrors how ML pipelines handle 
-- missing categorical features — treating NULL as a separate category 
-- rather than letting it silently exclude rows.

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;

-- LC#601 - Human Traffic of Stadium [Hard]
-- Topic: Self Join / Consecutive Row Detection
-- ML Connection: Detecting consecutive high-traffic periods mirrors 
-- anomaly detection in time-series ML — identifying sustained 
-- high-activity windows in streaming data pipelines.

WITH cte AS (
    SELECT DISTINCT s1.*
    FROM Stadium s1
    JOIN Stadium s2 ON s2.id IN (s1.id - 1, s1.id + 1)
    JOIN Stadium s3 ON s3.id IN (s1.id - 1, s1.id + 1)
        AND s2.id != s3.id
    WHERE s1.people >= 100
      AND s2.people >= 100
      AND s3.people >= 100
)
SELECT * FROM cte
ORDER BY visit_date;

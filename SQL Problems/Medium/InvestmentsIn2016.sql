-- LC#585 - Investments in 2016 [Medium]
-- Topic: Subquery / GROUP BY / HAVING
-- ML Connection: Filtering on duplicate vs unique attribute combinations 
-- mirrors feature-based deduplication in ML pipelines — selecting 
-- records that are unique on one dimension but shared on another.

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);

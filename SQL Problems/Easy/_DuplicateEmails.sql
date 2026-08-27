-- LC#182 - Duplicate Emails [Easy]
-- Topic: GROUP BY / HAVING
-- ML Connection: Finding duplicates via GROUP BY + HAVING mirrors 
-- data deduplication in ML pipelines — detecting duplicate training 
-- samples before model training to avoid data leakage.

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;

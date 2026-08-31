-- LC#183 - Customers Who Never Order [Easy]
-- Topic: LEFT JOIN / NOT IN / Subquery
-- ML Connection: Finding unmatched records mirrors anti-join operations 
-- in feature stores — identifying users with no activity data 
-- before applying cold-start ML models.

SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;

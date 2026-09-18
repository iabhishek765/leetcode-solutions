-- LC#607 - Sales Person [Easy]
-- Topic: NOT IN / Subquery / Multi-table Join
-- ML Connection: Anti-join filtering mirrors how ML pipelines exclude 
-- users who triggered a specific event — used in churn model training 
-- to separate control from treatment groups.

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);

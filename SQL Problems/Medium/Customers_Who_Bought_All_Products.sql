-- LC#1045 - Customers Who Bought All Products
-- Difficulty: Medium
-- Topics: SQL, GROUP BY, HAVING, Subquery
--
-- Approach: Group by customer_id, count distinct product_keys
--           per customer. Keep customers whose count matches
--           total products in Product table via subquery.
--
-- ML Connection: This GROUP BY + HAVING pattern mirrors
-- feature completeness checks in ML pipelines where you
-- verify which samples have all required features before
-- training (no missing values per row).

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);

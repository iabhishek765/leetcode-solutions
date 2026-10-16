-- Problem: List the Products Ordered in a Period (LC #1327)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/list-the-products-ordered-in-a-period/
--
-- Approach:
-- JOIN Products with Orders on product_id
-- Filter orders in February 2020 using BETWEEN
-- GROUP BY product, SUM units
-- HAVING filters groups with total >= 100
-- Time: O(n) | Space: O(n)
--
-- ML Connection:
-- Time-period filtering is used in time-series ML
-- to create training windows for forecasting models
-- HAVING with aggregation mirrors threshold filtering
-- in anomaly detection pipelines

SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;

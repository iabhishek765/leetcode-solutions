-- Problem: Product Price at a Given Date (LC #1164)
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/product-price-at-a-given-date/
--
-- Approach:
-- For each distinct product, find most recent price change
-- on or before 2019-08-16 using correlated subquery
-- If no change exists before that date, default price = 10
-- IFNULL handles products with no changes before the date
-- Time: O(n^2) | Space: O(n)
--
-- ML Connection:
-- Point-in-time lookups are critical in ML feature stores
-- to prevent data leakage during model training
-- Getting the "last known value" at a given time is a
-- core technique in time-series feature engineering

SELECT
    product_id,
    IFNULL(
        (SELECT new_price
         FROM Products p2
         WHERE p2.product_id = p1.product_id
         AND p2.change_date <= '2019-08-16'
         ORDER BY change_date DESC
         LIMIT 1),
        10
    ) AS price
FROM (SELECT DISTINCT product_id FROM Products) p1;

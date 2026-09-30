-- Problem: Average Selling Price (LC #1251)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/average-selling-price/
--
-- Approach:
-- LEFT JOIN Prices with UnitsSold on product_id and date range
-- Weighted average = SUM(units * price) / SUM(units)
-- IFNULL handles products with no sales (return 0)
-- Time: O(n * m) | Space: O(n)
--
-- ML Connection:
-- Weighted averages are used in ensemble ML models
-- where each model's prediction is weighted by confidence
-- Also core to gradient descent loss averaging in training

SELECT 
    p.product_id,
    IFNULL(ROUND(SUM(u.units * p.price) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

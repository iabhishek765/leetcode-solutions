-- Problem: Group Sold Products By The Date (LC #1484)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/group-sold-products-by-the-date/
--
-- Approach:
-- GROUP BY sell_date to aggregate per date
-- COUNT(DISTINCT product) for unique product count
-- GROUP_CONCAT(DISTINCT product ORDER BY product) for sorted names
-- ORDER BY sell_date for chronological output
-- Time: O(n log n) | Space: O(n)
--
-- ML Connection:
-- GROUP_CONCAT is used in feature aggregation pipelines
-- where multiple values per entity are combined into
-- a single feature string for NLP or categorical models

SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;

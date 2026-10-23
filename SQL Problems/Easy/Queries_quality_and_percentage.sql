-- Problem: Queries Quality and Percentage (LC #1211)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/queries-quality-and-percentage/
--
-- Approach:
-- quality = AVG(rating / position) per query_name
-- poor_query_percentage = (count of rating < 3) / total * 100
-- Use IF(rating < 3, 1, 0) to count poor queries
-- WHERE query_name IS NOT NULL handles edge case
-- ROUND to 2 decimal places as required
-- Time: O(n) | Space: O(n)
--
-- ML Connection:
-- Quality ratio metrics are used in ML model evaluation
-- (precision/recall per class) aggregated per category
-- Poor query percentage mirrors false positive rate
-- used in classification model performance analysis

SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(IF(rating < 3, 1, 0)) * 100 / COUNT(*), 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;

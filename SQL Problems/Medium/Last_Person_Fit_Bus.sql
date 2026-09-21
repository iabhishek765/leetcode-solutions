-- LC#1204 - Last Person to Fit in the Bus
-- Difficulty: Medium
-- Topics: SQL, Window Functions, Running Sum
--
-- Approach: Use SUM() OVER (ORDER BY turn) to compute
--           running cumulative weight in boarding order.
--           Filter where cumulative <= 1000, take the last
--           one (highest cumulative still within limit).
--
-- ML Connection: Running cumulative sums mirror online
-- learning weight updates where model parameters are
-- updated incrementally and capped at a budget threshold.

SELECT person_name
FROM (
    SELECT person_name,
           SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) t
WHERE cumulative_weight <= 1000
ORDER BY cumulative_weight DESC
LIMIT 1;

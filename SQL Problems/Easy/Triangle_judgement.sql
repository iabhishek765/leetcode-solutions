-- Problem: Triangle Judgement (LC #610)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/triangle-judgement/
--
-- Approach:
-- Triangle inequality: sum of any 2 sides > third side
-- Check all 3 combinations using CASE WHEN
-- Time: O(n) | Space: O(1)
--
-- ML Connection:
-- Conditional logic in SQL mirrors if-else branching
-- in decision tree nodes during ML inference
-- Triangle inequality also appears in metric learning
-- where valid distance functions must satisfy it

SELECT x, y, z,
    CASE
        WHEN x + y > z AND y + z > x AND x + z > y THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;

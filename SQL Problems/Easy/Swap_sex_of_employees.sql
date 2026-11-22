-- Problem: Swap Sex of Employees (LC #627)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/swap-sex-of-employees/
--
-- Approach:
-- Single UPDATE with CASE: 'm' becomes 'f', everything else becomes 'm'
-- All rows are evaluated against their old value, so no temp table needed
-- Time: O(n) | Space: O(1)
--
-- ML Connection:
-- Flipping binary labels in place is a basic data-cleaning
-- transformation, e.g. inverting a 0/1 target or category encoding.

UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    ELSE 'm'
END;

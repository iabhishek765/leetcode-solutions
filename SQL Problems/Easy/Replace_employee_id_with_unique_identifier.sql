-- Problem: Replace Employee ID With The Unique Identifier (LC #1378)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
--
-- Approach:
-- LEFT JOIN Employees with EmployeeUNI on id
-- Employees without a unique id get NULL automatically
-- Time: O(n) | Space: O(n)
--
-- ML Connection:
-- LEFT JOIN with NULLs for missing matches is the standard way
-- to merge feature tables where some entities lack a record,
-- a common step before imputing missing values.

SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;

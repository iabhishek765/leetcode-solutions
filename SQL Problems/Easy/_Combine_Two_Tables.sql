-- LC#175 - Combine Two Tables
-- Difficulty: Easy
-- Topics: SQL, LEFT JOIN, Table Relationships
--
-- Approach:
-- Use a LEFT JOIN to keep every person from the Person table,
-- even when there is no matching address.
-- Match the tables using personId.
--
-- Time: O(n + m)
-- Space: O(n + m) depending on the database execution plan
--
-- ML Connection:
-- JOIN operations are fundamental in data preprocessing and feature
-- engineering, where information from multiple tables is combined
-- to create a single dataset for analysis or machine learning models.


SELECT
    firstName,
    lastName,
    city,
    state
FROM Person AS P
LEFT JOIN Address AS A
    ON P.personId = A.personId;

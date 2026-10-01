-- Problem: Fix Names in a Table (LC #1667)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/fix-names-in-a-table/
--
-- Approach:
-- UPPER(LEFT(name, 1)) → capitalize first character
-- LOWER(SUBSTRING(name, 2)) → lowercase rest of string
-- CONCAT both parts → properly cased name
-- ORDER BY user_id as required
-- Time: O(n) | Space: O(1)
--
-- ML Connection:
-- String normalization is a key preprocessing step
-- in NLP pipelines before tokenization and embedding
-- Consistent casing reduces vocab size in text models

SELECT 
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;

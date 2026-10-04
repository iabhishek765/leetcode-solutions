-- Problem: Find Users With Valid E-Mails (LC #1517)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/find-users-with-valid-emails/
--
-- Approach:
-- Use REGEXP to validate email format:
-- 1. Prefix starts with a letter [a-zA-Z]
-- 2. Prefix can have letters, digits, underscore, period, dash
-- 3. Domain must be exactly @leetcode.com
-- Time: O(n) | Space: O(1)
--
-- ML Connection:
-- Regex-based validation is used in data cleaning
-- pipelines before feeding text into NLP models
-- Email/text pattern matching is a feature extraction
-- technique in spam detection ML systems

SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$';

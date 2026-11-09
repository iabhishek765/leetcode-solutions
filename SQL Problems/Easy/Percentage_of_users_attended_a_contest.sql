-- Problem: Percentage of Users Attended a Contest (LC #1633)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/percentage-of-users-attended-a-contest/
--
-- Approach:
-- GROUP BY contest_id on Register and COUNT users per contest
-- Divide by total users from a scalar subquery, multiply by 100
-- ROUND to 2 decimals; ORDER BY percentage DESC, contest_id ASC
-- Time: O(n) | Space: O(n)
--
-- ML Connection:
-- Computing a rate per group (here, participation per contest)
-- is the same pattern used for per-class rates in model
-- evaluation, such as conversion or error rate per segment.

SELECT
    contest_id,
    ROUND(COUNT(user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;

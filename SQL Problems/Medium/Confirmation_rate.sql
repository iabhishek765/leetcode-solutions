-- Problem: Confirmation Rate (LC #1934)
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/confirmation-rate/
--
-- Approach:
-- LEFT JOIN Signups with Confirmations to keep all users
-- IF(action = 'confirmed', 1, 0) converts to binary
-- AVG of binary values = rate directly
-- ROUND to 2 decimal places as required
-- Time: O(n) | Space: O(n)
--
-- ML Connection:
-- Binary encoding of categorical values (confirmed=1, timeout=0)
-- is exactly label encoding used in ML preprocessing
-- AVG of binary labels = class probability used in
-- logistic regression and probability calibration

SELECT
    s.user_id,
    ROUND(AVG(IF(c.action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;

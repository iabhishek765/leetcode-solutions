-- Problem: Customer Who Visited but Did Not Make Any Transactions (LC #1581)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
--
-- Approach:
-- LEFT JOIN Visits with Transactions on visit_id
-- Keep only visits with no matching transaction (IS NULL)
-- GROUP BY customer_id and COUNT those visits
-- Time: O(n) | Space: O(n)
--
-- ML Connection:
-- Finding records with no match (anti-join) is how you build
-- negative labels, such as users who viewed but did not convert.

SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;

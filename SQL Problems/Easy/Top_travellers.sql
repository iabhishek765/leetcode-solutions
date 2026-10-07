-- Problem: Top Travellers (LC #1407)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/top-travellers/
--
-- Approach:
-- LEFT JOIN Users with Rides to keep users with no rides
-- SUM(distance) per user, IFNULL handles null (no rides → 0)
-- ORDER BY distance DESC, name ASC for tie-breaking
-- Time: O(n log n) | Space: O(n)
--
-- ML Connection:
-- Aggregation + ranking is used in recommendation systems
-- to rank users or items by engagement score
-- LEFT JOIN pattern mirrors handling missing data
-- in ML feature tables (users with no activity)

SELECT u.name, IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;

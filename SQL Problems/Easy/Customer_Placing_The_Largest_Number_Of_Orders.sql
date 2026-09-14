-- LC#586 - Customer Placing the Largest Number of Orders [Easy]
-- Topic: GROUP BY / ORDER BY / LIMIT
-- ML Connection: Finding the top-k customers by order count mirrors 
-- how recommendation systems rank users by activity level for 
-- targeted model personalization.

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

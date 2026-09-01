-- LC#262 - Trips and Users [Hard]
-- Topic: JOIN / Aggregation / CASE WHEN / Date Filter
-- ML Connection: Computing cancellation rates per time window mirrors 
-- how ML monitoring systems calculate model error rates per day 
-- to detect performance degradation in production.

SELECT 
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) 
        / COUNT(*), 
    2) AS `Cancellation Rate`
FROM Trips t
JOIN Users client ON t.client_id = client.users_id AND client.banned = 'No'
JOIN Users driver ON t.driver_id = driver.users_id AND driver.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;

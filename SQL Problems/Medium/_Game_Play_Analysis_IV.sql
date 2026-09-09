-- LC#550 - Game Play Analysis IV [Medium]
-- Topic: Subquery / DATE_ADD / Aggregation
-- ML Connection: Day-1 retention rate is a key feature in churn 
-- prediction models — players who return next day are far less 
-- likely to churn, used as a label in ML retention models.

SELECT ROUND(
    COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
) AS fraction
FROM Activity a
JOIN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) first ON a.player_id = first.player_id
AND a.event_date = DATE_ADD(first.first_login, INTERVAL 1 DAY);

-- LC#511 - Game Play Analysis I [Easy]
-- Topic: GROUP BY / MIN / Aggregation
-- ML Connection: Finding first event per user mirrors how ML systems 
-- track user onboarding dates — used as a feature in churn prediction 
-- and cohort analysis models.

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;

-- LC#1321 - Restaurant Growth
-- Difficulty: Medium
-- Topics: SQL, Window Functions, Moving Average
--
-- Approach: First GROUP BY visited_on to get daily totals.
--           Then apply sliding window SUM over 7 rows
--           (6 preceding + current). Filter dates with full
--           7-day window. Round average to 2 decimal places.
--
-- ML Connection: Moving averages are used in time-series
-- preprocessing for ML models — smoothing noisy signals
-- before feeding into LSTM or Prophet forecasting models.

SELECT visited_on,
       amount,
       ROUND(amount / 7, 2) AS average_amount
FROM (
    SELECT visited_on,
           SUM(SUM(amount)) OVER (
               ORDER BY visited_on
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           ) AS amount
    FROM Customer
    GROUP BY visited_on
) t
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) 
    FROM Customer
)
ORDER BY visited_on;

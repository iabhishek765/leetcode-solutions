git add SQL/Easy/LC197_RisingTemperature.sql
git commit -m "Day N: LC#197 Rising Temperature [Easy] SQL"
git push

SELECT w1.id
FROM Weather w1
JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;

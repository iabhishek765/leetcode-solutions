-- LC#180 - Consecutive Numbers [Medium]
-- Topic: Self Join / Consecutive Row Detection
-- ML Connection: Detecting consecutive repeated patterns mirrors 
-- run-length encoding and sequence pattern detection used in 
-- time-series anomaly detection for ML systems.

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id + 1 = l2.id AND l1.num = l2.num
JOIN Logs l3 ON l1.id + 2 = l3.id AND l1.num = l3.num;

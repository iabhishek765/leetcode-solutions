-- LC#178 - Rank Scores [Medium]
-- Topic: Window Functions / DENSE_RANK
-- ML Connection: Ranking with no gaps mirrors how model evaluation 
-- leaderboards rank submissions — tied scores get same rank, 
-- next rank is consecutive (used in Kaggle-style competitions).

SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;

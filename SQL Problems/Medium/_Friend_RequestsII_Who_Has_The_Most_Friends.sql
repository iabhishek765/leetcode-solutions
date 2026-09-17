-- LC#602 - Friend Requests II: Who Has the Most Friends [Medium]
-- Topic: UNION ALL / GROUP BY / ORDER BY
-- ML Connection: Counting bidirectional graph edges per node mirrors 
-- degree centrality computation in graph ML — used in social network 
-- analysis and GNN-based recommendation systems.

SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) combined
GROUP BY id
ORDER BY num DESC
LIMIT 1;

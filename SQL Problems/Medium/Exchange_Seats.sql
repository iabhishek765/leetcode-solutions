-- LC#626 - Exchange Seats [Medium]
-- Topic: CASE WHEN / Conditional Logic
-- ML Connection: Conditional row transformation mirrors feature 
-- engineering in ML pipelines — applying different transformations 
-- to odd/even indexed samples in batch processing.

SELECT 
    CASE
        WHEN id % 2 = 1 AND id = (SELECT COUNT(*) FROM Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id;

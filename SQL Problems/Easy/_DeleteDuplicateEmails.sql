-- LC#196 - Delete Duplicate Emails [Easy]
-- Topic: DELETE with Self Join
-- ML Connection: Deduplication keeping the earliest record mirrors 
-- how data pipelines handle duplicate training samples — keeping 
-- the first occurrence and dropping redundant copies.

DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;

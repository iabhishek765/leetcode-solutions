-- LC#620 - Not Boring Movies
-- Difficulty: Easy
-- Topics: SQL, WHERE, ORDER BY
--
-- Approach: Filter odd id using modulo (id % 2 = 1),
--           exclude description = 'boring',
--           sort by rating descending.
--
-- ML Connection: Data filtering before model training —
-- removing low-quality or irrelevant samples from dataset
-- is the same concept as this WHERE clause filtering.

SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;

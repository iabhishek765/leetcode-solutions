-- LC#619 - Biggest Single Number
-- Difficulty: Easy
-- Topics: SQL, GROUP BY, HAVING, Subquery
--
-- Approach: Inner query filters numbers appearing exactly once
--           using GROUP BY + HAVING COUNT(*) = 1.
--           Outer MAX() picks the largest single number.
--           Returns NULL automatically if no single numbers exist.
--
-- ML Connection: Filtering unique/singleton values mirrors
-- rare class detection in imbalanced datasets before
-- applying oversampling techniques like SMOTE in ML pipelines.

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;

-- LC#1341 - Movie Rating
-- Difficulty: Medium
-- Topics: SQL, JOIN, GROUP BY, UNION ALL, Aggregation
--
-- Approach: Two separate aggregation queries combined with UNION ALL.
--   Q1: JOIN Users+MovieRating, group by user, order by count DESC
--       then name ASC, LIMIT 1.
--   Q2: JOIN Movies+MovieRating, filter Feb 2020, group by movie,
--       order by AVG(rating) DESC then title ASC, LIMIT 1.
--
-- ML Connection: Aggregating user-item interaction data and
-- finding top performers mirrors collaborative filtering in
-- recommendation systems where user activity scores and
-- item ratings are aggregated to rank candidates.

(
    SELECT u.name AS results
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT m.title AS results
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE DATE_FORMAT(mr.created_at, '%Y-%m') = '2020-02'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);

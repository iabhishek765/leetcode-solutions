-- LC#1280 - Students and Examinations
-- Difficulty: Easy
-- Topics: SQL, CROSS JOIN, LEFT JOIN, GROUP BY
--
-- Approach: CROSS JOIN Students × Subjects gives all possible
--           student-subject pairs. LEFT JOIN Examinations to
--           count actual attendance. COUNT(e.subject_name)
--           returns 0 for unattended (NULLs not counted).
--
-- ML Connection: Generating all feature combinations before
-- filtering mirrors cross-product feature engineering in ML
-- where all pairwise interactions are created before
-- selecting relevant ones via feature importance.

SELECT s.student_id,
       s.student_name,
       sub.subject_name,
       COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
    ON s.student_id = e.student_id
    AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;

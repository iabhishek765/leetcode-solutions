-- LC#596 - Classes With at Least 5 Students [Easy]
-- Topic: GROUP BY / HAVING

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;

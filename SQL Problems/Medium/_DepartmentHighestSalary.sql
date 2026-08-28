-- LC#184 - Department Highest Salary [Medium]
-- Topic: GROUP BY / Subquery / JOIN
-- ML Connection: Finding max value per group mirrors how 
-- argmax operations work in ML — selecting the best performing 
-- model per category/class in evaluation pipelines.

SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);

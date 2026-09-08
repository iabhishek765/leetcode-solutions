git add SQL/Hard/LC185_DepartmentTopThreeSalaries.sql
git commit -m "Day N: LC#185 Department Top Three Salaries [Hard] SQL"
git push

SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT 
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
) e
JOIN Department d ON e.departmentId = d.id
WHERE e.rnk <= 3;

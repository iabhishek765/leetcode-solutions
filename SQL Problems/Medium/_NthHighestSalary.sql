-- LC#177 - Nth Highest Salary [Medium]
-- Topic: LIMIT / OFFSET / Subquery
-- ML Connection: Selecting the Nth ranked item mirrors top-k 
-- selection in ML — retrieving the Nth best model or prediction 
-- from a ranked list.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET N
  );
END

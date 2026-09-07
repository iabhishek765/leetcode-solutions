-- LC#181 - Employees Earning More Than Their Managers [Easy]
-- Topic: Self Join
-- ML Connection: Self-joins for hierarchical comparisons mirror how 
-- tree-based ML models compare parent-child node values during 
-- decision tree traversal and pruning.

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;

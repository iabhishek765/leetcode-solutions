git add SQL/Easy/LC577_EmployeeBonus.sql
git commit -m "Day N: LC#577 Employee Bonus [Easy] SQL"
git push

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;

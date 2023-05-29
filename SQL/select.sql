SELECT COUNT(*) as EmployeeCount FROM Employee_Table;
SELECT e.EmployeeId, e.EmployeeName, e.Age, e.Salary
FROM Employee_Table as e
GO
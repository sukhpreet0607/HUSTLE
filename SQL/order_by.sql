SELECT EmployeeName,Salary FROM Employee_Table
ORDER BY Salary  
-- by default this query selects in asscending 
--    order

SELECT EmployeeName,Salary FROM Employee_Table
ORDER BY Salary DESC
-- this will select in descending order

SELECT EmployeeName,EmployeeId,Region FROM Employee_Table
ORDER BY Salary,EmployeeId
-- it orders by salary, but if some rows have the same salary, it orders them by tablenameid


SELECT * FROM Employee_Table
ORDER BY Age ASC, Salary DESC;



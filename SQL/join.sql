SELECT Employees.EmployeeName , Employees_info.Experience
FROM Employees
INNER JOIN Employees_info ON Employees.TableNameId=Employees_info.ID;


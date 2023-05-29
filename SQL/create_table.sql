use Employees
GO
CREATE TABLE dbo.Employee_Table
(
    EmployeeId INT NOT NULL PRIMARY KEY, -- primary key column
    EmployeeName VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Salary INT NOT NULL
);
GO
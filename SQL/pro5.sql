-- =========================================
-- EMPLOYEES DATABASE
-- =========================================

-- Remove the old table
DROP TABLE IF EXISTS Employees;

-- Create the Employees table
CREATE TABLE Employees (
    Employee_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Department TEXT,
    Salary REAL
);

-- =========================================
-- INSERT EMPLOYEE DATA
-- =========================================

INSERT INTO Employees
(Employee_ID, Name, Age, Department, Salary)
VALUES
(101, 'Ali', 25, 'IT', 50000),
(102, 'Sara', 28, 'HR', 45000),
(103, 'John', 31, 'Sales', 55000),
(104, 'Aisha', 26, 'Finance', 60000),
(105, 'David', 30, 'IT', 52000);

-- =========================================
-- DISPLAY ALL EMPLOYEE DETAILS
-- =========================================

SELECT *
FROM Employees;
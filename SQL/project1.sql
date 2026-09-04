-- =========================================
-- 1. DELETE OLD TABLE
-- =========================================

DROP TABLE IF EXISTS Employees;


-- =========================================
-- 2. CREATE THE EMPLOYEES TABLE
-- =========================================

CREATE TABLE Employees (
    Employee_id INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Job_title TEXT,
    Salary REAL,
    City TEXT
);


-- =========================================
-- 3. INSERT EMPLOYEE DATA
-- =========================================

INSERT INTO Employees
(Employee_id, Name, Department, Job_title, Salary, City)
VALUES
(101, 'John Smith', 'IT', 'Software Developer', 5500, 'Kuala Lumpur'),
(102, 'Sarah Lee', 'HR', 'HR Manager', 6200, 'Penang'),
(103, 'David Kumar', 'Finance', 'Accountant', 5800, 'Kuala Lumpur'),
(104, 'Emma Wilson', 'IT', 'Data Analyst', 6000, 'Johor Bahru'),
(105, 'Michael Tan', 'Sales', 'Sales Executive', 4500, 'Kuala Lumpur'),
(106, 'Sophia Lim', 'Finance', 'Financial Analyst', 6500, 'Penang'),
(107, 'Daniel Wong', 'IT', 'System Administrator', 5700, 'Malacca'),
(108, 'Olivia Chen', 'Sales', 'Sales Manager', 7000, 'Kuala Lumpur');


-- =========================================
-- 4. DISPLAY ALL EMPLOYEES
-- =========================================

SELECT * FROM Employees;


-- =========================================
-- 5. DISPLAY ONLY NAMES
-- =========================================

SELECT Name
FROM Employees;


-- =========================================
-- 6. DISPLAY NAMES AND DEPARTMENTS
-- =========================================

SELECT Name, Department
FROM Employees;


-- =========================================
-- 7. FIND EMPLOYEES IN THE IT DEPARTMENT
-- =========================================

SELECT *
FROM Employees
WHERE Department = 'IT';


-- =========================================
-- 8. FIND EMPLOYEES IN FINANCE
-- =========================================

SELECT *
FROM Employees
WHERE Department = 'Finance';


-- =========================================
-- 9. FIND EMPLOYEES FROM KUALA LUMPUR
-- =========================================

SELECT *
FROM Employees
WHERE City = 'Kuala Lumpur';


-- =========================================
-- 10. FIND EMPLOYEES WITH SALARY ABOVE 6000
-- =========================================

SELECT *
FROM Employees
WHERE Salary > 6000;


-- =========================================
-- 11. SORT EMPLOYEES BY SALARY
-- =========================================

SELECT Name, Salary
FROM Employees
ORDER BY Salary DESC;


-- =========================================
-- 12. FIND THE HIGHEST-PAID EMPLOYEE
-- =========================================

SELECT Name, Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 1;


-- =========================================
-- 13. COUNT THE NUMBER OF EMPLOYEES
-- =========================================

SELECT COUNT(*) AS Total_Employees
FROM Employees;


-- =========================================
-- 14. FIND THE AVERAGE SALARY
-- =========================================

SELECT AVG(Salary) AS Average_Salary
FROM Employees;


-- =========================================
-- 15. FIND THE LOWEST SALARY
-- =========================================

SELECT MIN(Salary) AS Lowest_Salary
FROM Employees;


-- =========================================
-- 16. FIND THE HIGHEST SALARY
-- =========================================

SELECT MAX(Salary) AS Highest_Salary
FROM Employees;
-- =========================================
-- CUSTOMER DATABASE
-- =========================================

DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    Customer_ID INTEGER PRIMARY KEY,
    Customer_Name TEXT,
    Product TEXT,
    Product_Price REAL,
    Export_Country TEXT
);

-- =========================================
-- ADD CUSTOMER DATA
-- =========================================

INSERT INTO Customers
(Customer_ID, Customer_Name, Product, Product_Price, Export_Country)
VALUES
(1, 'Aaron', 'Laptop', 1200, 'Malaysia'),
(2, 'Arora', 'Phone', 800, 'India'),
(3, 'Alice', 'Tablet', 600, 'Singapore'),
(4, 'George', 'Camera', 900, 'Japan'),
(5, 'Amor', 'Headphones', 150, 'Thailand'),
(6, 'David', 'Keyboard', 100, 'Malaysia');

-- =========================================
-- FIND CUSTOMERS WHOSE NAME:
-- 1. Starts with "a"
-- 2. Contains "or"
-- =========================================

SELECT *
FROM Customers
WHERE Customer_Name LIKE 'a%'
AND Customer_Name LIKE '%or%';
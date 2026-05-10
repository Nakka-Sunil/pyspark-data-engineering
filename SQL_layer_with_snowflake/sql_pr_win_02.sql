use database sandbox;
create or replace Schema playground_02;

-- ─────────────────────────────────────────
-- 1. DEPARTMENTS
-- ─────────────────────────────────────────
CREATE TABLE departments (
    department_id   INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Sales'),
(4, 'HR'),
(5, 'Finance');


-- ─────────────────────────────────────────
-- 2. EMPLOYEES
-- ─────────────────────────────────────────
CREATE TABLE employees (
    employee_id   INT PRIMARY KEY,
    name          VARCHAR(50),
    department_id INT,
    salary        DECIMAL(10,2),
    manager_id    INT,
    hire_date     DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO employees VALUES
(1,  'Arjun Sharma',    1, 120000, NULL,       '2018-03-01'),
(2,  'Priya Nair',      1,  95000, 1,          '2019-06-15'),
(3,  'Ravi Kumar',      1,  95000, 1,          '2020-01-10'),
(4,  'Sneha Reddy',     1,  80000, 1,          '2021-03-22'),
(5,  'Vikram Singh',    1,  75000, 2,          '2022-07-01'),
(6,  'Anita Desai',     2, 110000, NULL,       '2017-09-10'),
(7,  'Rohit Mehta',     2,  88000, 6,          '2019-11-05'),
(8,  'Kavya Pillai',    2,  88000, 6,          '2020-05-18'),
(9,  'Suresh Iyer',     2,  72000, 6,          '2021-08-30'),
(10, 'Deepa Joshi',     2,  65000, 7,          '2023-01-15'),
(11, 'Manoj Gupta',     3, 105000, NULL,       '2016-04-20'),
(12, 'Pooja Verma',     3,  90000, 11,         '2018-09-12'),
(13, 'Kiran Rao',       3,  90000, 11,         '2019-03-07'),
(14, 'Arun Bhat',       3,  78000, 11,         '2020-11-25'),
(15, 'Lakshmi Menon',   3,  70000, 12,         '2022-02-14'),
(16, 'Sanjay Patil',    4,  98000, NULL,       '2015-07-08'),
(17, 'Rekha Nair',      4,  82000, 16,         '2018-12-01'),
(18, 'Vivek Sharma',    4,  82000, 16,         '2019-06-22'),
(19, 'Meena Iyer',      4,  68000, 16,         '2021-04-15'),
(20, 'Ganesh Kumar',    4,  60000, 17,         '2023-07-01'),
(21, 'Nisha Patel',     5, 115000, NULL,       '2014-02-28'),
(22, 'Rahul Jain',      5,  92000, 21,         '2017-08-19'),
(23, 'Divya Menon',     5,  92000, 21,         '2018-05-11'),
(24, 'Sunil Rao',       5,  85000, 21,         '2020-09-30'),
(25, 'Anjali Singh',    5,  75000, 22,         '2022-11-07'),
(26, 'Aditya Kumar',    1,  95000, 1,          '2020-08-15'),
(27, 'Bhavna Shah',     2,  72000, 7,          '2022-03-10'),
(28, 'Chetan Verma',    3,  90000, 11,         '2019-07-22'),
(29, 'Disha Nair',      4,  68000, 17,         '2021-09-05'),
(30, 'Eshan Gupta',     5,  85000, 23,         '2020-12-18');


-- ─────────────────────────────────────────
-- 3. CUSTOMERS
-- ─────────────────────────────────────────
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY,
    name          VARCHAR(50),
    email         VARCHAR(80),
    city          VARCHAR(30),
    created_date  DATE
);

INSERT INTO customers VALUES
(1,  'Aarav Mehta',     'aarav@gmail.com',      'Bengaluru',  '2022-01-10'),
(2,  'Bhavna Iyer',     'bhavna@yahoo.com',     'Mumbai',     '2022-03-15'),
(3,  'Chirag Patel',    'chirag@gmail.com',      'Ahmedabad',  '2022-05-20'),
(4,  'Divya Sharma',    'divya@outlook.com',    'Delhi',      '2022-07-08'),
(5,  'Eshan Nair',      'eshan@gmail.com',       'Kochi',      '2022-09-25'),
(6,  'Fiona Desai',     'fiona@yahoo.com',      'Pune',       '2023-01-12'),
(7,  'Gaurav Rao',      'gaurav@gmail.com',      'Hyderabad',  '2023-02-28'),
(8,  'Hema Pillai',     'hema@outlook.com',     'Chennai',    '2023-04-15'),
(9,  'Ishaan Singh',    'ishaan@gmail.com',      'Jaipur',     '2023-06-01'),
(10, 'Jaya Kumar',      'jaya@yahoo.com',       'Bengaluru',  '2023-08-20');


-- ─────────────────────────────────────────
-- 4. PRODUCTS
-- ─────────────────────────────────────────
CREATE TABLE products (
    product_id    INT PRIMARY KEY,
    product_name  VARCHAR(60),
    category      VARCHAR(30),
    price         DECIMAL(10,2)
);

INSERT INTO products VALUES
(1,  'Laptop Pro 15',      'Electronics',  85000.00),
(2,  'Wireless Mouse',     'Electronics',   1200.00),
(3,  'Mechanical Keyboard','Electronics',   4500.00),
(4,  'USB-C Hub',          'Electronics',   2800.00),
(5,  'Monitor 27 inch',    'Electronics',  28000.00),
(6,  'Standing Desk',      'Furniture',    22000.00),
(7,  'Ergonomic Chair',    'Furniture',    18000.00),
(8,  'Bookshelf',          'Furniture',     8500.00),
(9,  'Desk Lamp',          'Furniture',     2200.00),
(10, 'Whiteboard',         'Furniture',     5500.00),
(11, 'Python Book',        'Books',          650.00),
(12, 'SQL Mastery',        'Books',          750.00),
(13, 'System Design',      'Books',          850.00),
(14, 'Clean Code',         'Books',          600.00),
(15, 'Data Engineering',   'Books',          800.00),
(16, 'Notebook Set',       'Stationery',     350.00),
(17, 'Pen Pack',           'Stationery',     120.00),
(18, 'Sticky Notes',       'Stationery',     80.00),
(19, 'File Organizer',     'Stationery',     450.00),
(20, 'Stapler',            'Stationery',     280.00);


-- ─────────────────────────────────────────
-- 5. ORDERS
-- ─────────────────────────────────────────
CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT,
    order_date  DATE,
    total_amount DECIMAL(10,2),
    status      VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(1001, 1, '2024-01-05', 86200.00, 'delivered'),
(1002, 1, '2024-01-28', 5700.00,  'delivered'),
(1003, 1, '2024-03-10', 28000.00, 'delivered'),
(1004, 2, '2024-01-08', 23200.00, 'delivered'),
(1005, 2, '2024-02-14', 1200.00,  'delivered'),
(1006, 2, '2024-03-22', 4500.00,  'delivered'),
(1007, 3, '2024-01-15', 18000.00, 'delivered'),
(1008, 3, '2024-02-20', 8500.00,  'delivered'),
(1009, 3, '2024-04-05', 2800.00,  'shipped'),
(1010, 4, '2024-01-20', 85000.00, 'delivered'),
(1011, 4, '2024-02-25', 22000.00, 'delivered'),
(1012, 4, '2024-05-10', 750.00,   'pending'),
(1013, 5, '2024-01-22', 4500.00,  'delivered'),
(1014, 5, '2024-03-18', 650.00,   'delivered'),
(1015, 5, '2024-04-30', 1200.00,  'shipped'),
(1016, 6, '2024-02-08', 28000.00, 'delivered'),
(1017, 6, '2024-02-27', 5500.00,  'delivered'),
(1018, 6, '2024-04-12', 2200.00,  'delivered'),
(1019, 7, '2024-01-30', 8500.00,  'delivered'),
(1020, 7, '2024-03-05', 18000.00, 'delivered'),
(1021, 7, '2024-04-20', 850.00,   'delivered'),
(1022, 8, '2024-02-10', 22000.00, 'delivered'),
(1023, 8, '2024-03-28', 4500.00,  'delivered'),
(1024, 8, '2024-05-15', 800.00,   'pending'),
(1025, 9, '2024-01-12', 1200.00,  'delivered'),
(1026, 9, '2024-02-18', 2800.00,  'delivered'),
(1027, 9, '2024-03-25', 85000.00, 'delivered'),
(1028, 10,'2024-01-25', 18000.00, 'delivered'),
(1029, 10,'2024-02-22', 8500.00,  'delivered'),
(1030, 10,'2024-04-08', 5500.00,  'delivered');


-- ─────────────────────────────────────────
-- 6. ORDER ITEMS
-- ─────────────────────────────────────────
CREATE TABLE order_items (
    item_id     INT PRIMARY KEY,
    order_id    INT,
    product_id  INT,
    quantity    INT,
    unit_price  DECIMAL(10,2),
    FOREIGN KEY (order_id)   REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_items VALUES
(1,  1001, 1,  1, 85000.00),
(2,  1001, 2,  1,  1200.00),
(3,  1002, 3,  1,  4500.00),
(4,  1002, 17, 5,   120.00),
(5,  1003, 5,  1, 28000.00),
(6,  1004, 6,  1, 22000.00),
(7,  1004, 2,  1,  1200.00),
(8,  1005, 2,  1,  1200.00),
(9,  1006, 3,  1,  4500.00),
(10, 1007, 7,  1, 18000.00),
(11, 1008, 8,  1,  8500.00),
(12, 1009, 4,  1,  2800.00),
(13, 1010, 1,  1, 85000.00),
(14, 1011, 6,  1, 22000.00),
(15, 1012, 12, 1,    750.00),
(16, 1013, 3,  1,  4500.00),
(17, 1014, 11, 1,    650.00),
(18, 1015, 2,  1,  1200.00),
(19, 1016, 5,  1, 28000.00),
(20, 1017, 10, 1,  5500.00),
(21, 1018, 9,  1,  2200.00),
(22, 1019, 8,  1,  8500.00),
(23, 1020, 7,  1, 18000.00),
(24, 1021, 13, 1,    850.00),
(25, 1022, 6,  1, 22000.00),
(26, 1023, 3,  1,  4500.00),
(27, 1024, 15, 1,    800.00),
(28, 1025, 2,  1,  1200.00),
(29, 1026, 4,  1,  2800.00),
(30, 1027, 1,  1, 85000.00),
(31, 1028, 7,  1, 18000.00),
(32, 1029, 8,  1,  8500.00),
(33, 1030, 10, 1,  5500.00),
-- extra items to make product revenue interesting
(34, 1001, 3,  1,  4500.00),  -- keyboard in same order
(35, 1004, 9,  1,  2200.00),
(36, 1010, 2,  2,  1200.00),
(37, 1011, 9,  1,  2200.00),
(38, 1016, 2,  1,  1200.00),
(39, 1019, 4,  1,  2800.00),
(40, 1027, 3,  1,  4500.00);


-- ─────────────────────────────────────────
-- 7. DAILY SALES  (for 7-day rolling avg)
-- ─────────────────────────────────────────
CREATE TABLE daily_sales (
    sale_id    INT PRIMARY KEY,
    product_id INT,
    sale_date  DATE,
    quantity   INT,
    revenue    DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO daily_sales VALUES
-- Product 1 (Laptop) — Jan 2024
(1,  1, '2024-01-01', 2, 170000),
(2,  1, '2024-01-02', 1,  85000),
(3,  1, '2024-01-03', 3, 255000),
(4,  1, '2024-01-04', 0,      0),
(5,  1, '2024-01-05', 1,  85000),
(6,  1, '2024-01-06', 2, 170000),
(7,  1, '2024-01-07', 4, 340000),
(8,  1, '2024-01-08', 1,  85000),
(9,  1, '2024-01-09', 2, 170000),
(10, 1, '2024-01-10', 0,      0),
(11, 1, '2024-01-11', 3, 255000),
(12, 1, '2024-01-12', 1,  85000),
(13, 1, '2024-01-13', 2, 170000),
(14, 1, '2024-01-14', 5, 425000),
-- Product 2 (Mouse) — Jan 2024
(15, 2, '2024-01-01', 10, 12000),
(16, 2, '2024-01-02', 15, 18000),
(17, 2, '2024-01-03',  8,  9600),
(18, 2, '2024-01-04', 20, 24000),
(19, 2, '2024-01-05', 12, 14400),
(20, 2, '2024-01-06',  5,  6000),
(21, 2, '2024-01-07', 18, 21600),
(22, 2, '2024-01-08', 22, 26400),
(23, 2, '2024-01-09', 10, 12000),
(24, 2, '2024-01-10', 14, 16800),
(25, 2, '2024-01-11',  9, 10800),
(26, 2, '2024-01-12', 25, 30000),
(27, 2, '2024-01-13', 11, 13200),
(28, 2, '2024-01-14', 16, 19200),
-- Product 3 (Keyboard) — Jan 2024
(29, 3, '2024-01-01',  5, 22500),
(30, 3, '2024-01-02',  3, 13500),
(31, 3, '2024-01-03',  7, 31500),
(32, 3, '2024-01-04',  4, 18000),
(33, 3, '2024-01-05',  6, 27000),
(34, 3, '2024-01-06',  2,  9000),
(35, 3, '2024-01-07',  8, 36000),
(36, 3, '2024-01-08',  5, 22500),
(37, 3, '2024-01-09',  3, 13500),
(38, 3, '2024-01-10',  9, 40500),
(39, 3, '2024-01-11',  4, 18000),
(40, 3, '2024-01-12',  6, 27000),
(41, 3, '2024-01-13',  7, 31500),
(42, 3, '2024-01-14',  5, 22500),
-- Product 5 (Monitor) — Jan 2024
(43, 5, '2024-01-01',  3,  84000),
(44, 5, '2024-01-02',  1,  28000),
(45, 5, '2024-01-03',  4, 112000),
(46, 5, '2024-01-04',  2,  56000),
(47, 5, '2024-01-05',  3,  84000),
(48, 5, '2024-01-06',  1,  28000),
(49, 5, '2024-01-07',  5, 140000),
(50, 5, '2024-01-08',  2,  56000),
(51, 5, '2024-01-09',  3,  84000),
(52, 5, '2024-01-10',  4, 112000),
(53, 5, '2024-01-11',  1,  28000),
(54, 5, '2024-01-12',  2,  56000),
(55, 5, '2024-01-13',  3,  84000),
(56, 5, '2024-01-14',  4, 112000);


SELECT 'SELECT * FROM SANDBOX.PLAYGROUND_02.'||TABLE_NAME ||';' AS QUERY_
FROM SANDBOX.INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'PLAYGROUND_02';

SELECT * FROM SANDBOX.PLAYGROUND_02.DEPARTMENTS;
SELECT * FROM SANDBOX.PLAYGROUND_02.ORDER_ITEMS;
SELECT * FROM SANDBOX.PLAYGROUND_02.ORDERS;
SELECT * FROM SANDBOX.PLAYGROUND_02.PRODUCTS;
SELECT * FROM SANDBOX.PLAYGROUND_02.CUSTOMERS;
SELECT * FROM SANDBOX.PLAYGROUND_02.DAILY_SALES;
SELECT * FROM SANDBOX.PLAYGROUND_02.EMPLOYEES;

----------------------------------------------------------------------
--sql Practcie: window functions 
--Q1 — Second highest salary
WITH second_high_sal AS (
    SELECT 
        E.NAME,
        D.DEPARTMENT_NAME,
        E.SALARY,
        DENSE_RANK() OVER(
            PARTITION BY E.DEPARTMENT_ID
            ORDER BY E.SALARY DESC
        ) AS RNK
    FROM SANDBOX.PLAYGROUND_02.EMPLOYEES E
    JOIN SANDBOX.PLAYGROUND_02.DEPARTMENTS D
        ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
)

SELECT
    NAME,
    DEPARTMENT_NAME,
    SALARY
FROM second_high_sal
WHERE RNK = 2;

--Q2: Difference Between Current and Previous Order Amount

WITH order_diff AS (
    SELECT
        O.CUSTOMER_ID,
        O.ORDER_ID,
        O.ORDER_DATE,
        O.TOTAL_AMOUNT,
        LAG(O.TOTAL_AMOUNT) OVER(
            PARTITION BY O.CUSTOMER_ID
            ORDER BY O.ORDER_DATE
        ) AS PREVIOUS_AMOUNT
    FROM SANDBOX.PLAYGROUND_02.ORDERS O
)

SELECT
    CUSTOMER_ID,
    ORDER_ID,
    ORDER_DATE,
    TOTAL_AMOUNT,
    PREVIOUS_AMOUNT,
    TOTAL_AMOUNT - PREVIOUS_AMOUNT AS DIFFERENCE
FROM order_diff
ORDER BY CUSTOMER_ID, ORDER_DATE;

--Q3: Rank Employees by Salary Within Department
SELECT
    E.NAME,
    D.DEPARTMENT_NAME,
    E.SALARY,
    RANK() OVER(
        PARTITION BY E.DEPARTMENT_ID
        ORDER BY E.SALARY DESC
    ) AS SALARY_RANK
FROM SANDBOX.PLAYGROUND_02.EMPLOYEES E
JOIN SANDBOX.PLAYGROUND_02.DEPARTMENTS D
    ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
ORDER BY D.DEPARTMENT_NAME, SALARY_RANK;

--Q4: Top 3 Products by Revenue in Each Category
WITH product_revenue AS (

    SELECT
        P.CATEGORY,
        P.PRODUCT_NAME,
        SUM(OI.QUANTITY * OI.UNIT_PRICE) AS TOTAL_REVENUE
    FROM SANDBOX.PLAYGROUND_02.ORDER_ITEMS OI
    JOIN SANDBOX.PLAYGROUND_02.PRODUCTS P
        ON OI.PRODUCT_ID = P.PRODUCT_ID
    GROUP BY
        P.CATEGORY,
        P.PRODUCT_NAME
),

ranked_products AS (

    SELECT
        CATEGORY,
        PRODUCT_NAME,
        TOTAL_REVENUE,
        DENSE_RANK() OVER(
            PARTITION BY CATEGORY
            ORDER BY TOTAL_REVENUE DESC
        ) AS RNK
    FROM product_revenue
)

SELECT
    CATEGORY,
    PRODUCT_NAME,
    TOTAL_REVENUE,
    RNK
FROM ranked_products
WHERE RNK <= 3
ORDER BY CATEGORY, RNK;

--Q5: 7-Day Rolling Average of Daily Sales

SELECT
    P.PRODUCT_NAME,
    S.SALE_DATE,
    S.REVENUE,

    AVG(S.REVENUE) OVER(
        PARTITION BY S.PRODUCT_ID
        ORDER BY S.SALE_DATE
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS ROLLING_AVG

FROM SANDBOX.PLAYGROUND_02.DAILY_SALES S
JOIN SANDBOX.PLAYGROUND_02.PRODUCTS P
    ON S.PRODUCT_ID = P.PRODUCT_ID

ORDER BY
    P.PRODUCT_NAME,
    S.SALE_DATE;

--Q6: Cumulative Revenue Per Customer
SELECT
    O.CUSTOMER_ID,
    O.ORDER_ID,
    O.ORDER_DATE,
    O.TOTAL_AMOUNT,

    SUM(O.TOTAL_AMOUNT) OVER(
        PARTITION BY O.CUSTOMER_ID
        ORDER BY O.ORDER_DATE
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS CUMULATIVE_REVENUE

FROM SANDBOX.PLAYGROUND_02.ORDERS O

ORDER BY
    O.CUSTOMER_ID,
    O.ORDER_DATE;

--Q7: First and Most Recent Purchase Date Without GROUP BY
SELECT
    CUSTOMER_ID,

    MIN(ORDER_DATE) OVER(
        PARTITION BY CUSTOMER_ID
    ) AS FIRST_PURCHASE_DATE,

    MAX(ORDER_DATE) OVER(
        PARTITION BY CUSTOMER_ID
    ) AS LATEST_PURCHASE_DATE

FROM SANDBOX.PLAYGROUND_02.ORDERS
ORDER BY CUSTOMER_ID;


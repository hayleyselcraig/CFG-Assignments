-- HS PHOTOGRAPHY DATABASE
-- This database was created for a photography business to manage customers,
-- bookings, shoot types, products, and customer purchases.

DROP DATABASE IF EXISTS photography_business;
CREATE DATABASE photography_business;
USE photography_business;

-- ==================================================
-- TABLE CREATION
-- ==================================================

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

CREATE TABLE shoot_types (
    shoot_id INT AUTO_INCREMENT PRIMARY KEY,
    shoot_name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    duration_hours INT NOT NULL
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    shoot_id INT NOT NULL,
    booking_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (shoot_id) REFERENCES shoot_types(shoot_id)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ==================================================
-- INSERT DATA: customers (11 rows total)
-- ==================================================
INSERT INTO customers (first_name, last_name, email, phone)
VALUES
('Emily', 'Jones', 'emilyjones@hotmail.com', '07123456789'),
('Daniel', 'Smith', 'danielsmith@gmail.com', '07234567890'),
('Sophie', 'Brown', 'sophiebrown@outlook.com', '07345678901'),
('Olivia', 'Taylor', 'olivia.taylor@gmail.com', '07456789012'),
('James', 'Wilson', 'james.wilson@yahoo.com', '07567890123'),
('Charlotte', 'Evans', 'charlotte.evans@hotmail.com', '07678901234'),
('Benjamin', 'Thomas', 'ben.thomas@gmail.com', '07789012345'),
('Amelia', 'Roberts', 'amelia.roberts@outlook.com', '07890123456'),
('Lucas', 'Walker', 'lucas.walker@gmail.com', '07901234567'),
('Grace', 'Hall', 'grace.hall@yahoo.com', '07111222333'),
('Henry', 'Allen', 'henry.allen@hotmail.com', '07222333444');

-- ==================================================
-- INSERT DATA: shoot_types (12 rows total)
-- ==================================================
INSERT INTO shoot_types (shoot_name, price, duration_hours)
VALUES
('Wedding', 1200.00, 8),
('Portrait', 150.00, 1),
('Event', 500.00, 4),
('Maternity', 200.00, 2),
('Newborn', 250.00, 2),
('Family', 300.00, 2),
('Engagement', 350.00, 3),
('Birthday Party', 400.00, 4),
('Corporate Headshots', 275.00, 2),
('Graduation', 180.00, 1),
('Pet Portrait', 160.00, 1),
('Fashion Shoot', 450.00, 3);

-- ==================================================
-- INSERT DATA: bookings (12 rows total)
-- ==================================================

INSERT INTO bookings (customer_id, shoot_id, booking_date)
VALUES
(1, 1, '2026-05-10'),
(2, 2, '2026-05-12'),
(3, 3, '2026-05-15'),
(4, 5, '2026-05-18'),
(5, 6, '2026-05-20'),
(6, 7, '2026-05-22'),
(7, 8, '2026-05-25'),
(8, 9, '2026-05-27'),
(9, 10, '2026-05-29'),
(10, 11, '2026-06-02'),
(11, 12, '2026-06-05'),

-- Additional wedding booking added so filtered booking queries return multiple results
(2, 1, '2026-06-10');

-- ==================================================
-- INSERT DATA: products (14 rows total)
-- ==================================================
INSERT INTO products (product_name, price, stock_quantity)
VALUES
('Photo Print 6x4', 10.00, 50),
('Photo Print 8x10', 18.00, 30),
('Wedding Album', 250.00, 10),
('Canvas Print', 120.00, 15),
('Framed Portrait', 80.00, 20),
('USB Photo Package', 45.00, 25),
('Mini Photo Book', 35.00, 18),
('Large Canvas Print', 180.00, 12),
('Keyring Photo Gift', 15.00, 40),
('Digital Download Package', 90.00, 50),
('A4 Mounted Print', 25.00, 35),
('Thank You Cards Pack', 20.00, 22),
('Photo Calendar', 30.00, 16),
('Acrylic Print', 140.00, 14);

-- ==================================================
-- INSERT DATA: orders (14 rows total)
-- ==================================================
INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES
(1, 1, 2, '2026-05-11'),
(2, 3, 1, '2026-05-13'),
(3, 4, 1, '2026-05-16'),
(1, 6, 1, '2026-05-17'),
(4, 7, 1, '2026-05-19'),
(5, 8, 1, '2026-05-21'),
(6, 9, 3, '2026-05-23'),
(7, 10, 1, '2026-05-26'),
(8, 11, 2, '2026-05-28'),
(9, 12, 1, '2026-05-30'),
(10, 13, 2, '2026-06-03'),
(11, 14, 1, '2026-06-06');

-- Additional orders added so customer 1 has products related to a wedding package 
-- for purpose of the stored procedure

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES
(1, 3, 1, '2026-05-18'),
(1, 12, 1, '2026-05-18');

-- ==================================================
-- BASIC VIEW QUERIES
-- ==================================================

SELECT * FROM customers ORDER BY last_name, first_name;
SELECT * FROM shoot_types ORDER BY price DESC;
SELECT * FROM bookings ORDER BY booking_date;
SELECT * FROM products ORDER BY stock_quantity;
SELECT * FROM orders ORDER BY order_date;

-- ==================================================
-- BUSINESS QUERIES
-- ==================================================

-- Business query: displays the full booking schedule with customer names,
-- shoot type, and booking date

SELECT 
    customers.first_name,
    customers.last_name,
    shoot_types.shoot_name,
    bookings.booking_date
FROM bookings
JOIN customers ON bookings.customer_id = customers.customer_id
JOIN shoot_types ON bookings.shoot_id = shoot_types.shoot_id
ORDER BY bookings.booking_date;

-- Business query: shows only wedding bookings so the photographer can
-- focus on planning larger or premium events

SELECT 
    customers.first_name,
    customers.last_name,
    shoot_types.shoot_name,
    bookings.booking_date
FROM bookings
JOIN customers ON bookings.customer_id = customers.customer_id
JOIN shoot_types ON bookings.shoot_id = shoot_types.shoot_id
WHERE shoot_types.shoot_name = 'Wedding'
ORDER BY bookings.booking_date;

-- Business query: shows customer orders, product details, and total price spent

SELECT 
    customers.first_name,
    customers.last_name,
    products.product_name,
    orders.quantity,
    products.price,
    (orders.quantity * products.price) AS total_price,
    orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
ORDER BY orders.order_date;

-- Business query: checks low stock products such as prints, albums, or extras

SELECT 
    product_name,
    price,
    stock_quantity
FROM products
WHERE stock_quantity < 20
ORDER BY stock_quantity;

-- ==================================================
-- AGGREGATE FUNCTIONS
-- ==================================================

-- Aggregate query: calculates the total number of bookings using COUNT

SELECT COUNT(*) AS total_bookings
FROM bookings;

-- Aggregate query: calculates the total revenue from all orders using SUM

SELECT SUM(products.price * orders.quantity) AS total_revenue
FROM orders
JOIN products ON orders.product_id = products.product_id;

-- ==================================================
-- BUILT-IN FUNCTIONS
-- ==================================================

-- Built-in function: combines first and last name into one column using CONCAT

SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    email
FROM customers;

-- Built-in function: calculates how many days remain until each booking using DATEDIFF

SELECT 
    customers.first_name,
    customers.last_name,
    shoot_types.shoot_name,
    bookings.booking_date,
    DATEDIFF(bookings.booking_date, CURDATE()) AS days_until_booking
FROM bookings
JOIN customers ON bookings.customer_id = customers.customer_id
JOIN shoot_types ON bookings.shoot_id = shoot_types.shoot_id
WHERE bookings.booking_date >= CURDATE()
ORDER BY bookings.booking_date;

-- ==================================================
-- VALIDATION CHECKS
-- ==================================================

-- Validation check: confirms there are no products with negative stock quantities

SELECT *
FROM products
WHERE stock_quantity < 0;

-- Validation check: confirms there are no orders with a quantity less than 1

SELECT *
FROM orders
WHERE quantity < 1;

-- Validation check: confirms there are no bookings without matching customer records

SELECT *
FROM bookings
LEFT JOIN customers ON bookings.customer_id = customers.customer_id
WHERE customers.customer_id IS NULL;

-- Validation check: confirms there are no bookings without matching shoot type records

SELECT *
FROM bookings
LEFT JOIN shoot_types ON bookings.shoot_id = shoot_types.shoot_id
WHERE shoot_types.shoot_id IS NULL;

-- ==================================================
-- UPDATE QUERY
-- ==================================================

-- Update query: changes a customer's phone number
-- for example if the customer provides new contact details.

UPDATE customers
SET phone = '07999999999'
WHERE customer_id = 1;

-- Update query: increases the price of a product
-- for example if printing or material costs increase.

UPDATE products
SET price = 275.00
WHERE product_name = 'Wedding Album';

-- Check update query has made these new updates.
SELECT * FROM customers
SELECT * FROM products
    
-- ==================================================
-- DELETE QUERY
-- ==================================================

-- Delete query: removes an incorrect order entry from the orders table,
-- for example if a mistake was made during data entry or the order was cancelled.


DELETE FROM orders WHERE order_id = 1;

-- ==================================================
-- STORED PROCEDURE
-- ==================================================

-- Drops the stored procedure if it already exists, allowing it to be recreated without errors

DROP PROCEDURE IF EXISTS GetCustomerSummary;

-- Stored procedure: creates a customer summary report showing
-- full customer name, booking details, products ordered, and total cost
-- DELIMITER changes the statement ending symbol from ; to // so semicolons can be used
-- inside the stored procedure without ending it too early

DELIMITER //

CREATE PROCEDURE GetCustomerSummary(IN selected_customer_id INT)
BEGIN

    SELECT 
        CONCAT(customers.first_name, ' ', customers.last_name) AS full_name,
        bookings.booking_date,
        shoot_types.shoot_name,
        shoot_types.price AS shoot_price,
        GROUP_CONCAT(products.product_name SEPARATOR ', ') AS products_ordered,
        SUM(orders.quantity * products.price) AS products_total,
        (shoot_types.price + SUM(orders.quantity * products.price)) AS overall_total
    FROM customers
    JOIN bookings ON customers.customer_id = bookings.customer_id
    JOIN shoot_types ON bookings.shoot_id = shoot_types.shoot_id
    JOIN orders ON customers.customer_id = orders.customer_id
    JOIN products ON orders.product_id = products.product_id
    WHERE customers.customer_id = selected_customer_id
    GROUP BY 
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        bookings.booking_date,
        shoot_types.shoot_name,
        shoot_types.price
    ORDER BY bookings.booking_date;

END //

DELIMITER ;

-- Example call: shows a full booking and order summary for customer 1
-- Example call: run separately in DBeaver after the procedure has been created
CALL GetCustomerSummary(1);

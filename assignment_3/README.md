# 📸 HS Photography Database

## Project Overview

HS Photography Database is a relational database I created for my own photography business. It stores customer details, manages photography bookings, records available shoot packages, tracks product sales, and monitors stock levels.  

The database uses linked tables with primary and foreign keys to keep information organised and reduce duplicate data. It also includes queries, reports, and a stored procedure to retrieve useful business information such as booking schedules, customer orders, revenue totals, and customer summaries.

This system helps me manage daily business operations more efficiently while improving organisation, customer service, and decision making.

---

## Creative Scenario of Use

I run a growing photography business offering weddings, portraits, family shoots, and events. As bookings increase, it becomes more difficult to manage customers, bookings, and additional product sales such as albums, prints, USB packages, and thank you cards.  

I created this database to provide a structured system that allows me to track bookings, manage customer orders, check stock availability, monitor sales, and quickly generate customer summaries for upcoming shoots.

This helps save time, reduce mistakes, and keep the business organised as it grows.

---

## Assignment Requirements Checklist

- [x] **Create a database with at least 3 tables**  
Created 5 tables: `customers`, `shoot_types`, `bookings`, `products`, `orders`

- [x] **Use good naming conventions**  
Clear table and column names using lowercase with underscores

- [x] **Link tables using primary and foreign keys**  
Primary keys in all tables, foreign keys used in `bookings` and `orders`

- [x] **At least 8 rows of mock data per table**  
All tables contain 11+ rows of sample data

- [x] **Include all setup commands and demo queries**  
Full SQL script includes database creation, tables, inserts, queries, and procedure

- [x] **Use at least 3 different data types**  
Used `INT`, `VARCHAR`, `DATE`, `DECIMAL`

- [x] **Use at least 2 constraints (not PK/FK)**  
Used `NOT NULL`, `UNIQUE`, `CHECK`

- [x] **Use at least 3 INSERT queries**  
Multiple INSERT queries used across all tables

- [x] **Use at least 5 SELECT queries**  
Includes basic views, business reports, validation checks, and summary queries

- [x] **Use at least 1 DELETE query**  
Included commented example: `DELETE FROM orders WHERE order_id = 1;`

- [x] **Use at least 2 aggregate functions**  
Used `COUNT()` and `SUM()`

- [x] **Use at least 2 joins**  
Used multiple `INNER JOIN` and `LEFT JOIN` queries

- [x] **Use at least 2 additional built-in functions**  
Used `CONCAT()` and `DATEDIFF()`

- [x] **Use ORDER BY in majority of queries**  
Sorting used throughout the script

- [x] **Create and use one stored procedure or function**  
Created `GetCustomerSummary`

- [x] **Normalise the database**  
Data split into separate linked tables to avoid duplication

- [x] **Provide a creative scenario of use**  
Photography business management system

---

## Database Tables

- customers  
- shoot_types  
- bookings  
- products  
- orders  

---

## Features

- Store customer records  
- Manage photography bookings  
- Record different shoot packages  
- Track customer product purchases  
- Monitor stock levels  
- Display booking schedules  
- Show customer orders and totals  
- Calculate revenue using aggregate functions  
- Generate customer summaries using a stored procedure  

---

## SQL Features Used

- CREATE DATABASE / CREATE TABLE  
- PRIMARY KEY  
- FOREIGN KEY  
- NOT NULL / UNIQUE / CHECK constraints  
- INSERT INTO  
- SELECT queries  
- DELETE query  
- INNER JOIN / LEFT JOIN  
- COUNT()  
- SUM()  
- CONCAT()  
- DATEDIFF()  
- ORDER BY  
- Stored Procedure  

---

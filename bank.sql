-- Create the "bank" database (if it doesn't already exist)
CREATE DATABASE IF NOT EXISTS bank;

-- Use the "bank" database
USE bank;

-- Create the "customer" table
CREATE TABLE customer (
    customer_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    customer_password VARCHAR(100) NOT NULL
);

-- Create the "account" table
CREATE TABLE account (
    account_number INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    routing_number INT, 
    user_id INT,
    statement_number INT, 
    FOREIGN KEY (statement_number) REFERENCES customer_statement(statement_id),
    FOREIGN KEY (user_id) REFERENCES customer(customer_id)
);

CREATE TABLE customer_statement
(
    statement_id     INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    current_balance float,
    withdraw_amount float,
    deposit_amount  float,
    modify_date DATE NOT NULL,
    the_description varchar(255)
);
SELECT
	user_id      AS "UserName",
    account_number  AS "Account Number",
    routing_number  AS "Routing Number",
    statement_number AS "Statement ID"
FROM account;
SELECT
	first_name AS "First Name",
    last_name  AS "Last Name",
    customer_id    AS "Customer ID",
    customer_password  AS "PassWord"
FROM customer;
SELECT
	statement_id    as "Statement Id",
    current_balance as "Current Balance",
    withdraw_amount as "Withdrawal Balance",
    deposit_amount  as "Deposit Balance",
    modify_date as "Date",
    the_description as "Description"
From customer_statement;



CREATE DATABASE atm_system;
USE atm_system;
CREATE TABLE User(
id INT PRIMARY KEY auto_increment,
name varchar (255) NOT NULL,
pin INT NOT NULL,
balance decimal(10, 2) DEFAULT 0.00
);

CREATE TABLE transcation(
id INT auto_increment PRIMARY KEY,
user_id INT NOT NULL, 
type enum('deposit', 'withdraw', 'check_balance') NOT NULL,
amount DECIMAL(10, 2), 
timestamp TIMESTAMP DEFAULT current_timestamp,
foreign key (user_id) references User(id)
);

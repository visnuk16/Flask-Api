CREATE DATABASE Eshop
    DEFAULT CHARACTER SET = 'utf8mb4';

CREATE TABLE Customer(  
    id INT,
    name VARCHAR(250),
    mail VARCHAR(250)
);

INSERT INTO Customer 
(id, name, mail) VALUES 
(1,'kavin','kavin@gmail'),
(2,'kavin','kavin@gmail');

SELECT * FROM Customer;

CREATE Table Empt(statement VARCHAR(250));
INSERT INTO Empt(statement) VALUES('NO DATA FOUND');
SELECT * FROM Empt;

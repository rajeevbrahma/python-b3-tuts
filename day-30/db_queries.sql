CREATE TABLE user (
    
    id int NOT NULL AUTO_INCREMENT, 
    name varchar(45), 
    password varchar(10), 
    balance float, 
    account_number int,
    PRIMARY KEY (id)
);

SELECT * FROM user;

SELECT name,password FROM user;

select * from user where id=2;


INSERT INTO user (account_number,name, password,balance) VALUES (123456789,'user1','pasd1',8293.23);
INSERT INTO user (account_number,name, password,balance) VALUES (123456790,'user2','pasd2',8293.23);
INSERT INTO user (account_number,name, password,balance) VALUES (123456791,'user2','pasd2',8293.23);

UPDATE user set name='user3' where id=3;

DELETE from user where id=3;
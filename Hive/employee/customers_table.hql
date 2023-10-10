create database if not exists classicmodels;
use classicmodels;

CREATE TABLE customers (
  customerNumber INT,
  customerName STRING,
  contactLastName STRING,
  contactFirstName STRING,
  phone STRING,
  addressLine1 STRING,
  addressLine2 STRING,
  city STRING,
  state STRING,
  postalCode STRING,
  country STRING,
  salesRepEmployeeNumber INT,
  creditLimit DECIMAL(10, 2)
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/classicmodels.db/customers';
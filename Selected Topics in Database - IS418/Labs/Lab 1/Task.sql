-- Check if the database already exists; if not, create it
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'FCAI_DB')
BEGIN
    CREATE DATABASE FCAI_DB;
END
GO

-- Switch to the database
USE FCAI_DB;
GO

-- 1. Create a non-clustered index on Salary.
CREATE NONCLUSTERED INDEX IX_Employees_Department 
ON Employees(Department);

-- 2. View all indexes using sp_helpindex. 
EXEC sp_helpindex 'Employees';

-- 3. Drop an index you created.
DROP INDEX IX_Employees_Department ON Employees;
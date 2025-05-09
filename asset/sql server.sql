CREATE DATABASE Data_test
GO
USE Data_test
GO

CREATE TABLE "User"(
    id_user INT IDENTITY(1,1) NOT NULL,
    name NVARCHAR(45),
    last_name NVARCHAR(45),
    rol NVARCHAR(max),
    user NVARCHAR(45),
    password VARBINARY(max),
    loged_date DATE,
    modify_date DATETIME,
    status bit,
    deleted_status bit DEFAULT 0
)



-- Crear una nueva base de datos llamada Data_test
CREATE DATABASE Data_test
GO

-- Usar la base de datos recién creada
USE Data_test
GO

-- Crear una tabla llamada "User" con los siguientes campos
CREATE TABLE "User"(
    id_user INT IDENTITY(1,1) NOT NULL,       -- ID autoincremental, clave primaria implícita
    name NVARCHAR(45),                        -- Nombre del usuario (máx. 45 caracteres)
    last_name NVARCHAR(45),                   -- Apellido del usuario
    rol NVARCHAR(max),                        -- Rol del usuario (sin límite de longitud)
    user NVARCHAR(45),                        -- Nombre de usuario
    password VARBINARY(max),                  -- Contraseña cifrada o en formato binario
    loged_date DATE,                          -- Fecha en que se conectó o registró
    modify_date DATETIME,                     -- Fecha y hora de última modificación
    status bit,                               -- Estado (activo/inactivo)
    deleted_status bit DEFAULT 0              -- Indicador lógico de eliminación (0 = no eliminado, 1 = eliminado)
)

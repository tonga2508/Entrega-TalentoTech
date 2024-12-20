-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS inventario;

-- Usar la base de datos
USE inventario;

-- Crear la tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(255)
);

-- Insertar varios productos para pruebas
INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES
('Producto 1', 'Descripción del producto 1', 50, 10.99, 'Categoría A'),
('Producto 2', 'Descripción del producto 2', 30, 20.50, 'Categoría B'),
('Producto 3', 'Descripción del producto 3', 15, 5.75, 'Categoría A'),
('Producto 4', 'Descripción del producto 4', 60, 8.90, 'Categoría C'),
('Producto 5', 'Descripción del producto 5', 10, 12.30, 'Categoría B');

-- Generar productos masivos para pruebas (gracias Coderhouse)
DELIMITER $$
CREATE PROCEDURE generar_productos_masivos()
BEGIN
    DECLARE i INT DEFAULT 6;
    WHILE i <= 200 DO
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (CONCAT('Producto ', i), CONCAT('Descripción del producto ', i),
                FLOOR(RAND() * 100), ROUND(RAND() * 50, 2), CONCAT('Categoría ', CHAR(65 + (i MOD 3))));
        SET i = i + 1;
    END WHILE;
END $$
DELIMITER ;

-- Llamar al procedimiento para generar productos masivos
CALL generar_productos_masivos();

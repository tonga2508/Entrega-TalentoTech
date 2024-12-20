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
    categoria VARCHAR(50) NOT NULL
);

-- Insertar 200 productos de prueba con descripciones detalladas y categorías simplificadas
INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES
('Producto 1', 'Lampara de escritorio', 50, 10.99, 'A'),
('Producto 2', 'Radio portátil', 30, 20.50, 'B'),
('Producto 3', 'Mouse óptico', 15, 5.75, 'A'),
('Producto 4', 'Ventilador de techo', 60, 8.90, 'C'),
('Producto 5', 'Auriculares inalámbricos', 10, 12.30, 'B'),
('Producto 6', 'Teclado mecánico', 37, 22.69, 'A'),
('Producto 7', 'Altavoz Bluetooth', 15, 20.37, 'B'),
('Producto 8', 'Tablet de 8 pulgadas', 25, 150.99, 'C'),
('Producto 9', 'Monitor de 24 pulgadas', 18, 199.99, 'A'),
('Producto 10', 'Cargador inalámbrico', 40, 25.00, 'B'),
('Producto 11', 'Lámpara LED', 20, 14.99, 'A'),
('Producto 12', 'Smartwatch deportivo', 12, 99.90, 'B'),
('Producto 13', 'Cámara de seguridad', 8, 49.99, 'C'),
('Producto 14', 'Disco duro externo', 45, 79.99, 'A'),
('Producto 15', 'Impresora multifunción', 9, 149.50, 'C'),
('Producto 16', 'Mouse gamer', 28, 29.99, 'A'),
('Producto 17', 'Smartphone básico', 5, 120.00, 'B'),
('Producto 18', 'Router Wi-Fi', 17, 59.99, 'C'),
('Producto 19', 'Teclado inalámbrico', 30, 39.99, 'A'),
('Producto 20', 'Cámara web HD', 23, 69.00, 'B'),
('Producto 21', 'Proyector portátil', 12, 220.00, 'C'),
('Producto 22', 'Monitor curvo', 18, 299.99, 'A'),
('Producto 23', 'Cargador rápido', 50, 19.99, 'B'),
('Producto 24', 'Lector de tarjetas', 35, 12.50, 'C'),
('Producto 25', 'Auriculares gaming', 15, 79.99, 'B');

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

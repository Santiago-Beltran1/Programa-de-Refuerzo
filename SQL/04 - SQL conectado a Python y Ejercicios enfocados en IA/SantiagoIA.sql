-- Este ejemplo de SQL con conexión a Python y IA lo haremos con un Sistema de Detección y Predicción de Enfermedades en Cosechas

--Comenzamos haciendo justamente toda la base de datos más los datos que llevaría

CREATE DATABASE santiago_IA;
USE santiago_IA;

CREATE TABLE santiago_cultivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    fecha_siembra DATE
);

CREATE TABLE santiago_sensores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cultivo_id INT,
    humedad FLOAT,
    temperatura FLOAT,
    luminosidad FLOAT,
    fecha DATETIME,
    FOREIGN KEY (cultivo_id) REFERENCES santiago_cultivos(id)
);

CREATE TABLE santiago_imagenes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cultivo_id INT,
    url_imagen VARCHAR(255),
    etiqueta VARCHAR(100),
    fecha DATETIME,
    FOREIGN KEY (cultivo_id) REFERENCES santiago_cultivos(id)
);

CREATE TABLE santiago_alertas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cultivo_id INT,
    mensaje VARCHAR(255),
    nivel VARCHAR(20),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO santiago_cultivos (nombre, tipo, fecha_siembra) VALUES
('Producción 1', 'Cebolla', '2025-11-12'),
('Producción 2', 'Aguacate', '2025-11-11');

INSERT INTO santiago_sensores (cultivo_id, humedad, temperatura, luminosidad, fecha) VALUES
(1, 27, 27, 790, '2025-01-11 7:00:00'),
(1, 17, 31, 880, '2025-01-11 9:00:00'),
(2, 47, 19, 410, '2025-02-12 14:00:00');

INSERT INTO santiago_imagenes (cultivo_id, url_imagen, etiqueta, fecha) VALUES
(1, '/img/cebollaEnferma.jpg', 'enfermo', NOW()),
(1, '/img/CebollaBuena.jpg', 'sano', NOW());


-- Así sería el ejemplo de una vista para ver el estado del clima en una cosecha:
CREATE VIEW santiago_vista_clima AS
SELECT c.nombre AS cultivo,
       s.humedad,
       s.temperatura,
       s.luminosidad,
       s.fecha
FROM santiago_sensores s
JOIN santiago_cultivos c ON s.cultivo_id = c.id;

-- Ejemplo de trigger que generaría una alerta automática si la humedad baja del 20%

CREATE TRIGGER santiago_trigger_humedad_baja
AFTER INSERT ON santiago_sensores
FOR EACH ROW
BEGIN
    IF NEW.humedad < 20 THEN
        INSERT INTO santiago_alertas(cultivo_id, mensaje, nivel)
        VALUES (NEW.cultivo_id, 'Humedad peligrosa, posible enfermedad fúngica', 'ALTA');
    END IF;
END;

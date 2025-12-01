-- Aquí haremos consultas de ejemplo que se pueden hacer en cada tabla para 

-- Selects para seleccionar info de las tablas según sea necesario

-- Ver todos los juegos
SELECT * FROM Games;

-- Ver todos los clientes
SELECT * FROM Clientes;

-- Ver todas las ventas
SELECT * FROM Ventas;


-- Filtro con Where

-- Juegos con precio mayor a 30mil COP$
SELECT titulo, precio
FROM Games
WHERE precio > 30000;

-- Clientes que en el correo contenga "gmail"
SELECT nombre_cliente, email
FROM Clientes
WHERE email LIKE '%gmail%';

-- Empleados que sean cajeros
SELECT *
FROM Empleados
WHERE puesto = 'Cajero';


-- Joins (Unir tablas)
-- Ver juegos con su desarrolladora y distribuidora
SELECT g.titulo, d.nombre_dev, ds.nombre_dist
FROM Games g
JOIN Devs d ON g.id_dev = d.id_dev
JOIN Dists ds ON g.id_dist = ds.id_dist;

-- Ver stock por juego y plataforma
SELECT g.titulo, p.nombre_plat, gp.stock
FROM Game_Plat gp
JOIN Games g ON gp.id_game = g.id_game
JOIN Plats p ON gp.id_plat = p.id_plat;

-- 4. Funciones (SUM, AVG, COUNT, MAX, MIN)

-- Total de ventas registradas
SELECT SUM(monto_total) AS total_ventas
FROM Ventas;

-- Promedio de precio de juegos
SELECT AVG(precio) AS precio_promedio
FROM Games;

-- Cantidad de clientes registrados
SELECT COUNT(*) AS total_clientes
FROM Clientes;

-- Juego más caro
SELECT titulo, precio
FROM Games
ORDER BY precio DESC
LIMIT 1;

--Expresiones Regulares:

-- Buscar clientes cuyo email termine en gmail.com
SELECT nombre_cliente, email
FROM Clientes
WHERE email ~* 'gmail\.com$'; -- ~* indica case-insensitive

-- Buscar juegos cuyo título comience con "C" o "M"
SELECT titulo
FROM Games
WHERE titulo ~ '^(C|M)';

-- Condicionales: 

-- Clasificar juegos según precio
SELECT titulo,
       CASE
           WHEN precio < 30000 THEN 'Barato'
           WHEN precio BETWEEN 50000 AND 100000 THEN 'Precio Moderado'
           ELSE 'Caro'
       END AS categoria_precio
FROM Games;

-- SubConsultas
-- Juegos más caros que el precio promedio
SELECT titulo, precio
FROM Games
WHERE precio > (SELECT AVG(precio) FROM Games);

-- Clientes que hayan comprado más de una venta
SELECT nombre_cliente
FROM Clientes
WHERE id_cliente IN (
    SELECT id_cliente
    FROM Ventas
    GROUP BY id_cliente
    HAVING COUNT(*) > 1
);


-- SubConsultas correlacionadas

-- Mostrar juegos y su stock máximo por plataforma
SELECT g.titulo, gp.stock
FROM Game_Plat gp
JOIN Games g ON gp.id_game = g.id_game
WHERE gp.stock = (
    SELECT MAX(stock)
    FROM Game_Plat
    WHERE id_game = gp.id_game
);


-- UPDATE o actualizar datos

-- Aumentar el precio de todos los juegos 10%
UPDATE Games
SET precio = precio * 1.10;

-- Aumentar el stock de una plataforma específica
UPDATE Game_Plat
SET stock = stock + 50
WHERE id_plat = 2;

-- DELETE o eliminación de datos

-- Borra un cliente 
DELETE FROM Clientes
WHERE id_cliente = 3;  -- Elimina James Rodriguez

-- Borrar un juego 
DELETE FROM Games
WHERE id_game = 2; -- Elimina Zenless Zone Zero

--ALTER 

-- Agregar una columna nueva a Clientes
ALTER TABLE Clientes
ADD COLUMN telefono VARCHAR(20);

-- Cambiar el tipo de dato de una columna (precio a integer)
ALTER TABLE Games
ALTER COLUMN precio TYPE INTEGER USING precio::INTEGER;


-- Consultas Avanzadas - Analizar Ventas en este caso

-- Detalle completo de ventas (venta, juego, plataforma, cliente, empleado)
SELECT v.id_venta, g.titulo, p.nombre_plat, c.nombre_cliente, e.nombre_empleado,
       dv.cantidad, dv.precio_unit
FROM Detalle_Venta dv
JOIN Ventas v ON dv.id_venta = v.id_venta
JOIN Games g ON dv.id_game = g.id_game
JOIN Plats p ON dv.id_plat = p.id_plat
JOIN Clientes c ON v.id_cliente = c.id_cliente
JOIN Empleados e ON v.id_empleado = e.id_empleado
ORDER BY v.id_venta;


-- El juego más vendido (en cantidad total)
SELECT g.titulo, SUM(dv.cantidad) AS total_vendido
FROM Detalle_Venta dv
JOIN Games g ON dv.id_game = g.id_game
GROUP BY g.titulo
ORDER BY total_vendido DESC
LIMIT 1;


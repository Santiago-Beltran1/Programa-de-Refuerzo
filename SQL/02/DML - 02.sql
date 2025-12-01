-- DML y Ejercicios propuestos realizados en el caso de mi base de datos:

USE santiagoMulti;

-- Selects más condiciones:

-- Buscar productos por coincidencia (LIKE)
SELECT * FROM prd
WHERE nom LIKE '%Tesla%' OR sku LIKE 'TSL%';

-- Todos los clientes
SELECT * FROM cli;

-- Productos con precio mayor a 100.000
SELECT id, nom, precio 
FROM prd 
WHERE precio > 100000
ORDER BY precio DESC;

-- Clientes de una ciudad específica
SELECT nom, ape, ciudad
FROM cli
WHERE ciudad = 'Funza';

-- Joins + Inner + Left:

-- Pedidos con datos del cliente
SELECT o.id AS id_pedido, c.nom, c.ape, o.estado, o.total
FROM ord o
JOIN cli c ON o.id_cli = c.id;

-- Detalle del pedido con info del producto
SELECT oi.id_ord, p.nom AS producto, oi.cant, oi.subtotal
FROM oi
JOIN prd p ON oi.id_prd = p.id;

-- Libros y su autor
SELECT b.tit, CONCAT(a.nom,' ',a.ape) AS autor
FROM bk b
JOIN auth a ON b.id_auth = a.id;

-- GROUP BY + HAVING:

-- Total gastado por cliente
SELECT c.id, c.nom, c.ape,
       COUNT(o.id) AS num_pedidos,
       SUM(o.total) AS total_gastado
FROM cli c
LEFT JOIN ord o ON o.id_cli = c.id
GROUP BY c.id
HAVING total_gastado IS NOT NULL;

-- Cantidad de productos por categoría
SELECT cat.nom AS categoria, COUNT(p.id) AS productos
FROM prd p
JOIN cat ON p.id_cat = cat.id
GROUP BY cat.nom;

-- Promedio de precios por categoría (solo las que superan 100.000)
SELECT cat.nom AS categoria, AVG(p.precio) AS promedio
FROM prd p
JOIN cat ON p.id_cat = cat.id
GROUP BY cat.nom
HAVING promedio > 100000;

-- SUBQUERIES

-- Productos con precio mayor al promedio general
SELECT *
FROM prd
WHERE precio > (SELECT AVG(precio) FROM prd);

-- Clientes que NO han hecho pedidos
SELECT *
FROM cli
WHERE id NOT IN (SELECT id_cli FROM ord);

-- Precio máximo de producto por categoría
SELECT nom, precio
FROM prd
WHERE precio = (
    SELECT MAX(precio)
    FROM prd pr2
    WHERE pr2.id_cat = prd.id_cat
);

-- Vistas y Creación:

CREATE OR REPLACE VIEW v_resumen_clientes AS
SELECT c.id AS id_cli,
       CONCAT(c.nom,' ',c.ape) AS cliente,
       COUNT(o.id) AS pedidos,
       COALESCE(SUM(o.total),0) AS total_gastado
FROM cli c
LEFT JOIN ord o ON o.id_cli = c.id
GROUP BY c.id;

-- Uso de la vista:
SELECT * FROM v_resumen_clientes ORDER BY total_gastado DESC;

-- UPDATE Y DELETE: 

-- Actualizar estado de un pedido
UPDATE ord
SET estado = 'En Proceso'
WHERE id = 1;

-- Cambiar precio de un producto
UPDATE prd
SET precio = precio * 1.05
WHERE id = 2;

-- Borrar notas muy cortas
DELETE FROM note
WHERE LENGTH(titulo) < 5;

-- Funciones Análiticas
-- Ranking de productos por precio
SELECT id, nom, precio,
       RANK() OVER(ORDER BY precio DESC) AS ranking
FROM prd;

-- Ventas acumuladas por cliente
SELECT c.id, c.nom, o.total,
       SUM(o.total) OVER(PARTITION BY c.id ORDER BY o.id) AS acumulado
FROM ord o
JOIN cli c ON o.id_cli = c.id;

-- AGREGADOS: AVG(), SUM(), MAX(), MIN(), COUNT():

-- Precio promedio de los productos
SELECT AVG(precio) AS promedio_precios
FROM prd;

-- Stock total de la tabla productos
SELECT SUM(stock) AS total_stock
FROM prd;

-- Precio máximo y mínimo por categoría
SELECT cat.nom AS categoria,
       MAX(p.precio) AS precio_max,
       MIN(p.precio) AS precio_min
FROM prd p
JOIN cat ON p.id_cat = cat.id
GROUP BY cat.nom;

-- 2. BETWEEN — RANGOS:
   
-- Productos con precio entre 80.000 y 1.000.000
SELECT id, nom, precio
FROM prd
WHERE precio BETWEEN 80000 AND 1000000;

-- Libros con año de publicación entre 2016 y 2020
SELECT tit, anio
FROM bk
WHERE anio BETWEEN 2016 AND 2020;

-- FUNCIONES DE TEXTO: UPPER, LOWER, CONCAT, LENGTH, REPLACE

-- Convertir nombres de productos a mayúsculas
SELECT UPPER(nom) AS producto_mayus
FROM prd;

-- Convertir ciudades en minúscula
SELECT LOWER(ciudad) AS ciudad_minus
FROM cli;

-- Unir nombre y apellido del cliente
SELECT CONCAT(nom, ' ', ape) AS nombre_completo
FROM cli;

-- Longitud del título de cada libro
SELECT tit, LENGTH(tit) AS longitud
FROM bk;

-- Reemplazar texto en notas
SELECT titulo, REPLACE(titulo, 'a', '@') AS cambiado
FROM note;

-- FECHAS: NOW(), CURDATE(), DATEDIFF()

-- Fecha actual del sistema
SELECT NOW() AS fecha_actual;

-- Días desde que se realizó un pago
SELECT id, fecha,
       DATEDIFF(NOW(), fecha) AS dias_transcurridos
FROM pay;

-- Transacción Ejemplo:

START TRANSACTION;

-- Crear un pedido
INSERT INTO ord (id_cli, estado, subtotal, impuesto, total)
VALUES (3, 'Pendiente', 80000, 15200, 95200);

SET @new_ord = LAST_INSERT_ID();

-- Insertar detalle
INSERT INTO oi (id_ord, id_prd, cant, precio_unit, descuento, subtotal)
VALUES (@new_ord, 3, 1, 80000, 0, 80000);

-- Reducir stock del producto
UPDATE prd
SET stock = stock - 1
WHERE id = 3 AND stock >= 1;

-- Confirmar
COMMIT;

-- Reportes y Consultas más complejos

-- Producto más caro por categoría
SELECT cat.nom AS categoria, p.nom AS producto, p.precio
FROM prd p
JOIN cat ON p.id_cat = cat.id
WHERE (p.id_cat, p.precio) IN (
    SELECT id_cat, MAX(precio)
    FROM prd
    GROUP BY id_cat
);

-- Total vendido por método de pago
SELECT metodo, COUNT(id) AS transacciones, SUM(monto) AS total
FROM pay
GROUP BY metodo;

-- Ejercicios:

-- 1: Libros publicados después de 2016
SELECT b.tit, a.nom, a.ape, b.anio
FROM bk b
JOIN auth a ON b.id_auth = a.id
WHERE b.anio > 2016;

-- 2: Top 3 clientes con mayor gasto
SELECT *
FROM v_resumen_clientes
ORDER BY total_gastado DESC
LIMIT 3;

-- 3: Productos con stock menor a 50
SELECT id, nom, stock
FROM prd
WHERE stock < 50;

-- 4: Cantidad de notas por cada topic
SELECT t.nom, COUNT(nt.id_note) AS notas
FROM topic t
LEFT JOIN note_topic nt ON nt.id_topic = t.id
GROUP BY t.nom;

-- 5: Pedido completo con sumatoria del detalle
SELECT o.id, c.nom AS cliente, SUM(oi.subtotal) AS total_items
FROM ord o
JOIN cli c ON o.id_cli = c.id
JOIN oi ON oi.id_ord = o.id
GROUP BY o.id;

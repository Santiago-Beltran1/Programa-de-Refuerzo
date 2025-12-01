-- Ingreso de datos para cada tabla ejemplo:

-- Devs
INSERT INTO Devs (nombre_dev, pais) VALUES
('Supercell', 'Finlandia'),
('Hoyoverse', 'Shanghái'),
('Mojang', 'Suecia'),

-- Dists
INSERT INTO Dists (nombre_dist, contacto) VALUES
('Supercell', 'supercell@gmail.com'),
('HoyoVerse', 'miHoyo@gmail.com'),
('Mojang Studios', 'minecraft@microsoft.com'),

-- Plats
INSERT INTO Plats (nombre_plat) VALUES
('PC'),
('Xbox Series X/S'),
('PS5'),

-- Games
INSERT INTO Games (titulo, fecha_lanz, precio, id_dev, id_dist) VALUES
('Clash Royale', '2016-03-02', 15000, 1, 1),
('Zenless Zone Zero', '2024-07-04', 20000, 2, 2),
('Minecraft', '2009-03-17', 130000, 3, 3),

-- Clientes
INSERT INTO Clientes (nombre_cliente, email, direccion) VALUES
('Santiago Beltran', 'SantiagoB@gmail.com', 'Avenida Brazil'),
('David Pedraza', 'DavidP@gmail.com', 'Avenida Spain'),
('James Rodriguez', 'james@gmail.com', 'Calle fulvito'),

-- Empleados
INSERT INTO Empleados (nombre_empleado, puesto) VALUES
('Pepito P.', 'Cajero'),
('Pepita P.', 'Vendedor'),
('Susano S.', 'Supervisor'),

-- Game_Plat
INSERT INTO Game_Plat (id_game, id_plat, stock) VALUES
(1, 1, 150),
(2, 2, 150),
(3, 3, 150),

-- Ventas
INSERT INTO Ventas (monto_total, id_cliente, id_empleado) VALUES
(15000, 1, 1),
(20000, 2, 2),
(130000, 3, 3),

-- Detalle_Venta
INSERT INTO Detalle_Venta (id_venta, id_game, id_plat, cantidad, precio_unit) VALUES
(1, 3, 2, 1, 15000),
(2, 2, 3, 2, 20000),
(3, 1, 1, 3, 130000),
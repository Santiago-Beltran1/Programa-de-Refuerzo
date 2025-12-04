-- Inserción de datos:

USE santiagoMulti;

INSERT INTO cat (nom, des) VALUES
('Elec', 'Dispositivos Electrónicos'),
('Herramientas', 'Cosntrucción y Maquinaría'),
('Ropa', 'Prendas y Moda'),
('Carros', 'Industria Automotriz y Transporte');

INSERT INTO prd (nom, sku, id_cat, precio, stock) VALUES
('Smartphone Oppo a5 5g', 'OP001', 1, 1000000, 35),
('Taladro Marca Pepito', 'TMP01', 2, 300000, 100),
('Buzo Shingeki', 'BSNK1', 3, 80000, 20),
('Tesla Model 3', 'TSL03', 4, 120000000, 100);

INSERT INTO cli (nom, ape, email, tel, ciudad) VALUES
('Santiago', 'Beltran', 'sb@gmail.com', '3001111111', 'Mosquera'),
('David', 'Pedraza', 'dp@gmail.com', '3002222222', 'Funza'),
('Santiago', 'Pedraza', 'sp@gmail.com', '3003333333', 'Madrid'),
('David', 'Beltran', 'db@gmail.com', '3004444444', 'Tunja');

INSERT INTO ord (id_cli, estado, subtotal, impuesto, total) VALUES
(1, 'Pendiente', 1000000, 19.00, 1190000),
(2, 'Entregado', 300000, 19.00 , 357000);

-- detalle pedidos
INSERT INTO oi (id_ord, id_prd, cant, precio_unit, descuento, subtotal) VALUES
(1, 1, 1, 79.90, 0, 79.90),
(2, 2, 2, 24.50, 0, 49.00),
(2, 4, 1, 19.99, 0, 19.99),
(1, 3, 1, 39.99, 10, 35.99); -- ejemplo con descuento (nota: subtotal calculado por app)

INSERT INTO pay (id_ord, monto, metodo, ref, estado) VALUES
(1, 1000000,'Tarjeta', 'REF001', 'Completado'),
(2, 300000,'Efectivo', NULL, 'Completado'),
(2, 80000,'Efectivo', NULL, 'Reembolsado'),
(1, 120000000,'Tarjeta', 'REF002', 'En Proceso');

-- autores (Ejemplo de libros)
INSERT INTO auth (nom, ape) VALUES
('Santiago','Beltran'),
('David','Beltran'),
('Santiago','Pedraza'),
('David','Pedraza');

-- libros 
INSERT INTO bk (tit, id_auth, isbn, anio, paginas) VALUES
('Chainsaw', 1, '000-1111111111', 2022, 120),
('Clash Royale Guía', 2, '000-2222222222', 2016, 1500),
('El libro troll', 3, '000-3333333333', 2017, 350),
('Luna de Plutón', 4, '000-4444444444', 2017, 750);

INSERT INTO topic (nom, des) VALUES
('Manga','Manga y Escritos Japóneses'),
('Ciencia','TOP 500 Articulos mejores estrategiás de ataque'),
('Entretenimiento','Categoría de entretenimiento'),
('Refleciónes personales','Hecho por: Dross');

INSERT INTO note (ubicacion, titulo) VALUES
('n1','Muerte del protagonista pag..'),
('n2','Jugada 1'),
('n3','JWJJWWJJWJ'),
('n4','Trabaja Inteligente');

-- relacion note_topic (N:M)
INSERT INTO note_topic (id_note, id_topic) VALUES
(1,1),(1,2),(2,2),(3,4),(4,4),(2,3);

-- audit logs (ejemplos)
INSERT INTO audit_log (quien, accion, tabla, fila_id) VALUES
('admin','INSERT','prd',1),
('system','UPDATE','ord',2),
('admin','INSERT','cli',1),
('admin','INSERT','bk',1);

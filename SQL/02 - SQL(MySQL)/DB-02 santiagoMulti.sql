-- DDL (crear BD y tablas 3FN)
-- Comercio Multifuncional (para aplicar las consultas después que se proponen en la guía):
-- Ahora a diferencia del módulo 01 la haremos con MySQL en este caso

DROP DATABASE IF EXISTS santiagoMulti;  --Si la base de datos ya existe eliminarla para que no hayan conflicto y crear la nuestra
CREATE DATABASE santiagoMulti CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; -- Se puede almacenar cualquier carácter unicode (como emojis)
USE santiagoMulti;

-- categorías:
CREATE TABLE cat (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(50) NOT NULL UNIQUE,
  des TEXT -- des usa para almacenar cadenas de texto largas, como el cuerpo de artículos, descripciones de productos o comentarios.
);

-- productos:
CREATE TABLE prd (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  sku VARCHAR(30) UNIQUE,
  id_cat INT NOT NULL,
  precio DECIMAL(10,2) NOT NULL CHECK (precio > 0),
  stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
  activo BOOLEAN NOT NULL DEFAULT TRUE,
  FOREIGN KEY (id_cat) REFERENCES cat(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- clientes:
CREATE TABLE cli (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(60) NOT NULL,
  ape VARCHAR(60),
  email VARCHAR(120) UNIQUE,
  tel VARCHAR(20),
  ciudad VARCHAR(50),
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ordenes:
CREATE TABLE ord (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_cli INT NOT NULL,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente',
  subtotal DECIMAL(10,2) DEFAULT 0 CHECK (subtotal >= 0),
  impuesto DECIMAL(10,2) DEFAULT 0 CHECK (impuesto >= 0),
  total DECIMAL(10,2) DEFAULT 0 CHECK (total >= 0),
  FOREIGN KEY (id_cli) REFERENCES cli(id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CHECK (estado IN ('Pendiente','Procesando','Enviado','Entregado','Cancelado'))
);

-- Detalles de pedidos 
CREATE TABLE oi (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_ord INT NOT NULL,
  id_prd INT NOT NULL,
  cant INT NOT NULL CHECK (cant > 0),
  precio_unit DECIMAL(10,2) NOT NULL CHECK (precio_unit > 0),
  descuento DECIMAL(5,2) DEFAULT 0 CHECK (descuento >= 0 AND descuento <= 100),
  subtotal DECIMAL(10,2) NOT NULL CHECK (subtotal >= 0),
  FOREIGN KEY (id_ord) REFERENCES ord(id) ON DELETE CASCADE,
  FOREIGN KEY (id_prd) REFERENCES prd(id) ON DELETE RESTRICT
);

-- Pagos:
CREATE TABLE pay (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_ord INT NOT NULL,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  monto DECIMAL(10,2) NOT NULL CHECK (monto > 0),
  metodo VARCHAR(30) NOT NULL,
  ref VARCHAR(50),
  estado VARCHAR(20) DEFAULT 'Completado',
  FOREIGN KEY (id_ord) REFERENCES ord(id) ON DELETE CASCADE,
  CHECK (estado IN ('Pendiente','Completado','Rechazado','Reembolsado'))
);

-- Libros y autores (esta no se pondría en un comercio ya que haria parte de una categoría más servirá para mostrar ejemplos de consultas de db para bibliotecas)
CREATE TABLE auth (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(80) NOT NULL,
  ape VARCHAR(80)
);

CREATE TABLE bk (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tit VARCHAR(200) NOT NULL,
  id_auth INT NOT NULL,
  isbn VARCHAR(20) UNIQUE,
  anio INT,
  paginas INT CHECK (paginas > 0),
  dispo BOOLEAN DEFAULT TRUE,
  fecha_reg DATE DEFAULT CURRENT_DATE,
  FOREIGN KEY (id_auth) REFERENCES auth(id) ON DELETE RESTRICT
);

-- Notas
CREATE TABLE topic (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL UNIQUE,
  des TEXT
);

CREATE TABLE note (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ubicacion VARCHAR(100) NOT NULL, -- p.ej. estanteria/carpeta
  titulo VARCHAR(150) NOT NULL,
  creado DATE DEFAULT CURRENT_DATE
);

CREATE TABLE note_topic (
  id_note INT NOT NULL,
  id_topic INT NOT NULL,
  PRIMARY KEY (id_note, id_topic),
  FOREIGN KEY (id_note) REFERENCES note(id) ON DELETE CASCADE,
  FOREIGN KEY (id_topic) REFERENCES topic(id) ON DELETE CASCADE
);

-- Tabla para auditar cambios simples
CREATE TABLE audit_log (
  id INT AUTO_INCREMENT PRIMARY KEY,
  quien VARCHAR(80),
  accion VARCHAR(20),
  tabla VARCHAR(50),
  fila_id INT,
  ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices sencillos para consultas frecuentes
CREATE INDEX idx_prd_sku ON prd(sku);
CREATE INDEX idx_cli_email ON cli(email);

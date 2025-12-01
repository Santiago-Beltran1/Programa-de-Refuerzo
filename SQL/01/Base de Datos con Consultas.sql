CREATE DATABASE SantiagoGames;

-- USE SantiagoGames; este code solo se pone si estamos en mysql si estamos en postgres no es necesario

-- Comenzamos con la creación de las tablas para las bases de datos: 

-- Desarrolladores:
CREATE TABLE Devs (
    id_dev SERIAL PRIMARY KEY, -- Si fuera en mysql sería INT AUTO_INCREMENT PRIMARY KEY para definir llave primaria
    nombre_dev VARCHAR(100) NOT NULL UNIQUE,
    pais VARCHAR(50)
);


-- Distribuidoras:
CREATE TABLE Dists (
    id_dist SERIAL PRIMARY KEY,
    nombre_dist VARCHAR(100) NOT NULL UNIQUE,
    contacto VARCHAR(255)
);


-- Plataformas:
CREATE TABLE Plats (
    id_plat SERIAL PRIMARY KEY,
    nombre_plat VARCHAR(50) NOT NULL UNIQUE
);


-- Juegos:
CREATE TABLE Games (
    id_game SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    fecha_lanz DATE,
    precio NUMERIC(10,2) NOT NULL CHECK (precio >= 0),

    id_dev INTEGER NOT NULL REFERENCES Devs(id_dev),  -- O si fuera en mysql sería: FOREIGN KEY (id_dev) REFERENCES Devs(id_dev)
    id_dist INTEGER REFERENCES Dists(id_dist)
);


CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre_cliente VARCHAR(100) NOT NULL, -- NOT NULL es que el campo se tiene que llenar si o si no puede estar vacio
    email VARCHAR(100) UNIQUE, -- UNIQUE es que no hayan duplicados
    direccion VARCHAR(255)
);


CREATE TABLE Empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre_empleado VARCHAR(100) NOT NULL,
    puesto VARCHAR(50)
);


-- Stock por juego y plataforma:
CREATE TABLE Game_Plat (
    id_game INTEGER NOT NULL REFERENCES Games(id_game),
    id_plat INTEGER NOT NULL REFERENCES Plats(id_plat),

    stock INTEGER NOT NULL CHECK (stock >= 0), -- Revisa que el stock sea si o si mayor o igual a 0, que no sea negativo

    PRIMARY KEY (id_game, id_plat)
);

CREATE TABLE Ventas (
    id_venta SERIAL PRIMARY KEY,
    fecha_venta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- TIMESTAMP registra fecha + hora exacta de la venta.
    monto_total NUMERIC(10,2) NOT NULL CHECK (monto_total >= 0), -- Numeric abarca el (número máximo, cantidad de decimales)

    id_cliente INTEGER REFERENCES Clientes(id_cliente),
    id_empleado INTEGER NOT NULL REFERENCES Empleados(id_empleado)
);


CREATE TABLE Detalle_Venta (
    id_venta INTEGER NOT NULL REFERENCES Ventas(id_venta),
    id_game INTEGER NOT NULL,
    id_plat INTEGER NOT NULL,

    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unit NUMERIC(10,2) NOT NULL CHECK (precio_unit >= 0),

    FOREIGN KEY (id_game, id_plat)
        REFERENCES Game_Plat(id_game, id_plat),

    PRIMARY KEY (id_venta, id_game, id_plat)
);

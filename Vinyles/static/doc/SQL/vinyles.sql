-- Eliminar Base de Datos
DROP DATABASE vinyles;

-- Crear Base de Datos
CREATE DATABASE vinyles;

-- Ingresar BD
USE vinyles;

-- Crear tabla Ciudad
CREATE TABLE Pais (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los países',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombres de los países'
) COMMENT = 'Esta es la tabla que almacena los países de los pedidos';

-- Crear tabla Departamento
CREATE TABLE departamento (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Departamentos',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombres de los Departamentos',
	idPais INT NOT NULL COMMENT 'ID, y Llave Foránea de los Países, que llamará la id de la tabla pais',
    FOREIGN KEY (idPais) REFERENCES pais(id)
) COMMENT = 'Esta es la tabla que almacena los Departamentos de los pedidos';

-- Crear tabla Pais
CREATE TABLE ciudad (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de las Ciudades',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombres de las Ciudades',
    idDepartamento INT NOT NULL COMMENT 'ID, y Llave Foránea de los Departamentos, que llamará la id de la tabla departamentos',
    FOREIGN KEY (idDepartamento) REFERENCES departamento(id)
) COMMENT = 'Esta es la tabla que almacena las Ciudades de los pedidos';

-- Crear Tabla de Cliente
CREATE TABLE cliente (
	id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'ID de los Clientes',
    numeroDocumento INT NOT NULL COMMENT 'Número de Documento de los Clientes',
    usuario VARCHAR(100) NOT NULL COMMENT 'Usuario de los Clientes',
    contrasena VARCHAR(100) NOT NULL COMMENT 'Contraseña de los Clientes',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombres de los Clientes',
    apellido VARCHAR(100) NOT NULL COMMENT 'Apellidos de los Clientes',
    email VARCHAR(100) NOT NULL COMMENT 'Email de los Clientes',
    celular INT NOT NULL COMMENT 'Celular de los Clientes',
    direccion VARCHAR(255) NOT NULL COMMENT 'Dirección de los Clientes'
) COMMENT = 'Esta es la tabla que almacena la información de los Clientes';

-- Crear tabla Medio de pago
CREATE TABLE medioDePago (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Medios de Pago',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombres de los Medios de Pago'
) COMMENT = 'Esta es la tabla que almacena la información de los Medios de Pago de los clientes';

-- Crear tabla Pedido
CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Pedidos',
    fecha DATE NOT NULL COMMENT 'Fecha de los Pedidos',
    total DECIMAL(10, 2) NOT NULL COMMENT 'Total de los Pedidos',
    direccionEnvio VARCHAR(255) NOT NULL COMMENT 'Direccion de Envío de los Pedidos',
    idCiudad INT NOT NULL COMMENT 'ID, y Llave Foránea de las Ciudades, que llamará la id de la tabla ciudad',
    idCliente INT NOT NULL COMMENT 'ID, y Llave Foránea de los Clientes, que llamará la id de la tabla cliente',
    idMedioDePago INT NOT NULL COMMENT 'ID, y Llave Foránea de los Medios de Pago, que llamará la id de la tabla mediosDePago',
    FOREIGN KEY (idCiudad) REFERENCES ciudad(id),
    FOREIGN KEY (idCliente) REFERENCES cliente(id),
    FOREIGN KEY (idMedioDePago) REFERENCES medioDePago(id)
) COMMENT = 'Esta es la tabla que almacena la información de los Pedidos de los clientes';

-- Crear tabla Artista
CREATE TABLE artista (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Artistas',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombre de los Artistas',
    informacion VARCHAR(100) NOT NULL COMMENT 'Información relevante de los Artistas'
) COMMENT = 'Esta es la tabla que almacena la información de los Artistas';

-- Crear tabla Género
CREATE TABLE genero (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Géneros',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombre de los Géneros'
) COMMENT = 'Esta es la tabla que almacena los Géneros Musicales';

-- Crear tabla Canción
CREATE TABLE cancion (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de las Canciones',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombre de las Canciones',
    idArtista INT NOT NULL COMMENT 'ID, y Llave Foránea de los Artistas, que llamará la id de la tabla artista',
    idGenero INT NOT NULL COMMENT 'ID, y Llave Foránea de los Géneros musicales, que llamará la id de la tabla genero',
    FOREIGN KEY (idArtista) REFERENCES artista(id),
    FOREIGN KEY (idGenero) REFERENCES genero(id)
) COMMENT = 'Esta es la tabla que almacena la información de las Canciones';

-- Crear tabla Productos
CREATE TABLE producto (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Productos',
    nombre VARCHAR(2000) NOT NULL COMMENT 'Nombre de los Productos',
    stock INT NOT NULL COMMENT 'Stock o Cantidad Existente de los Productos',
    discografica VARCHAR(2000) NOT NULL COMMENT 'Compañía Discográfica de los Productos',
    lanzamiento DATE NOT NULL COMMENT 'Fecha de Lanzamiento de los Productos',
    idCancion INT NOT NULL COMMENT 'ID, y Llave Foránea de las Canciones, que llamará la id de la tabla cancion',
    FOREIGN KEY (idCancion) REFERENCES cancion(id)
) COMMENT = 'Esta es la tabla que almacena los Productos comerciables';

-- Crear tabla Pedidos de Productos
CREATE TABLE pedidoProducto (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Productos de cada Pedido',
    cantidad INT NOT NULL COMMENT 'Cantidad de los Productos de cada Pedido',
    valorUnitario DECIMAL(10, 2) NOT NULL COMMENT 'Valor Unitario de los Productos de cada Pedido',
    idPedido INT NOT NULL COMMENT 'ID, y Llave Foránea de los Pedidos, que llamará la id de la tabla pedido',
    idProducto INT NOT NULL COMMENT 'ID, y Llave Foránea de los Productos comerciables, que llamará la id de la tabla producto',
    FOREIGN KEY (idPedido) REFERENCES pedido(id),
    FOREIGN KEY (idProducto) REFERENCES producto(id)
) COMMENT = 'Esta es la tabla que almacena la información de los Productos de cada Pedido';

-- Crear tabla Soporte
CREATE TABLE soporte (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID de los Casos de nuestro Soporte Técnico',
    descripcion VARCHAR(2000) NOT NULL COMMENT 'Descripción de los Casos de nuestro Soporte Técnico',
    estado VARCHAR(20) NOT NULL COMMENT 'Estado de los Casos de nuestro Soporte Técnico',
    idCliente INT NOT NULL COMMENT 'ID, y Llave Foránea de los Clientes, que llamará la id de la tabla cliente',
    FOREIGN KEY (idCliente) REFERENCES cliente(id)
) COMMENT = 'Esta es la tabla que almacena la información de los Casos de nuestro Soporte Técnico';

-- Crear tabla Cliente Medio de Pago
CREATE TABLE clienteMedioDePago (
	idCliente INT NOT NULL COMMENT 'ID, y Llave Foránea de los Clientes, que llamará la id de la tabla cliente',
	idMedioDePago INT NOT NULL COMMENT 'ID, y Llave Foránea de los Medios de Pago, que llamará la id de la tabla mediosDePago',
	PRIMARY KEY (idCliente, idMedioDePago),
	FOREIGN KEY (idCliente) REFERENCES cliente(id),
	FOREIGN KEY (idMedioDePago) REFERENCES medioDePago (id)
) COMMENT = 'Esta es la tabla que almacena la información de los Medios de Pago de los Clientes';
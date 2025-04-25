-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-04-2025 a las 07:25:58
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hotel_saturday`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bedroom`
--

CREATE TABLE `bedroom` (
  `id_bedroom` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bedroom`
--

INSERT INTO `bedroom` (`id_bedroom`, `type`, `price`, `capacity`, `description`, `status`) VALUES
(1, 'Individual', 110000, 1, 'Habitación individual con cama sencilla, baño privado y Wi-Fi gratis', 1),
(2, 'Individual', 125000, 1, 'Habitación sencilla con escritorio y televisión por cable', 1),
(3, 'Doble', 180000, 2, 'Habitación doble con dos camas individuales, aire acondicionado y baño privado', 0),
(4, 'Doble', 190000, 2, 'Habitación doble con balcón y vista al jardín', 0),
(5, 'Matrimonial', 210000, 2, 'Habitación con cama matrimonial, TV y baño privado con agua caliente', 0),
(6, 'Matrimonial', 225000, 2, 'Habitación con cama queen, minibar y aire acondicionado', 0),
(7, 'Triple', 260000, 3, 'Habitación triple con tres camas individuales y mesa de trabajo', 0),
(8, 'Triple', 275000, 3, 'Habitación espaciosa con minibar, TV y vista a la ciudad', 0),
(9, 'Familiar', 310000, 4, 'Habitación familiar con dos camas dobles, ideal para niños', 1),
(10, 'Familiar', 330000, 4, 'Habitación con litera y cama doble, baño amplio y aire acondicionado', 0),
(11, 'Suite', 450000, 2, 'Suite con cama king, jacuzzi, minibar y sala de estar', 1),
(12, 'Suite Ejecutiva', 480000, 2, 'Suite con escritorio ejecutivo, sofá, Wi-Fi y baño de lujo', 1),
(13, 'Premium', 500000, 2, 'Habitación premium con terraza privada y desayuno incluido', 1),
(14, 'Deluxe', 550000, 2, 'Habitación deluxe con decoración moderna y acceso al spa', 1),
(15, 'Penthouse', 750000, 2, 'Penthouse con vista panorámica, sala privada y servicios VIP', 0),
(16, 'Regular', 100000, 2, 'Normal', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `booking`
--

CREATE TABLE `booking` (
  `id_booking` int(11) NOT NULL,
  `id_guest` int(11) NOT NULL,
  `id_bedroom` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `booking`
--

INSERT INTO `booking` (`id_booking`, `id_guest`, `id_bedroom`, `start_date`, `end_date`, `total`) VALUES
(1, 10323, 15, '2025-12-03', '2025-12-09', 0),
(2, 174938275, 10, '2025-03-20', '2025-03-27', 0),
(3, 1789453621, 8, '2025-02-10', '2025-02-17', 0),
(4, 1789453621, 2, '2025-02-02', '2025-02-06', 0),
(5, 1857369401, 14, '2025-02-05', '2025-02-12', 0),
(6, 198374652, 1, '2025-03-04', '2025-03-09', 0),
(7, 1857392045, 12, '2025-02-02', '2025-02-08', 3024500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `booking_optionalservice`
--

CREATE TABLE `booking_optionalservice` (
  `id_booking` int(11) NOT NULL,
  `id_optionalService` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `booking_optionalservice`
--

INSERT INTO `booking_optionalservice` (`id_booking`, `id_optionalService`) VALUES
(1, 1),
(1, 3),
(1, 5),
(1, 8),
(2, 1),
(2, 2),
(2, 3),
(2, 5),
(2, 7),
(2, 8),
(3, 1),
(3, 2),
(3, 3),
(3, 5),
(3, 8),
(4, 1),
(4, 3),
(5, 1),
(5, 4),
(5, 5),
(5, 8),
(6, 1),
(6, 2),
(6, 5),
(6, 8),
(7, 1),
(7, 3),
(7, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `status` int(11) NOT NULL DEFAULT 1,
  `rol` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `employee`
--

INSERT INTO `employee` (`id`, `name`, `last_name`, `phone`, `email`, `password`, `status`, `rol`) VALUES
(1033, 'r', 'a', '1323123', 'r@', '2', 1, 'administrador'),
(1012345678, 'María', 'Gómez', '3101234567', 'maria.gomez@hotelxyz.com', 'pass123', 1, 'Recepcionista'),
(1098765432, 'Carlos', 'Ramírez', '3202345678', 'carlos.ramirez@hotelxyz.com', 'hotel2025', 1, 'Ama de llaves'),
(1122334455, 'Ana', 'López', '3113456789', 'ana.lopez@hotelxyz.com', 'clave321', 1, 'Gerente'),
(1234567890, 'Fernando', 'Martínez', '3154567890', 'fernando.martinez@hotelxyz.com', 'chef123', 1, 'Chef'),
(1357924680, 'Luisa', 'Fernández', '3145678901', 'luisa.fernandez@hotelxyz.com', 'mante1', 1, 'Mantenimiento');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `guest`
--

CREATE TABLE `guest` (
  `id_guest` int(11) NOT NULL,
  `name` varchar(55) NOT NULL,
  `last_name` varchar(55) NOT NULL,
  `phone` varchar(14) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(20) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `origin` varchar(70) NOT NULL,
  `occupation` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `guest`
--

INSERT INTO `guest` (`id_guest`, `name`, `last_name`, `phone`, `email`, `password`, `status`, `origin`, `occupation`) VALUES
(10323, 'r', 'r', '2', 'r@', '2', 1, 'ru', 'no'),
(19847263, 'Carlos', 'Ramírez', '3001234567', 'carlos@example.com', 'clave123', 1, 'Colombia', 'Ingeniero'),
(174938275, 'María', 'Gómez', '3112345678', 'maria@example.com', 'password456', 1, 'México', 'Doctora'),
(192385740, 'Ana', 'Torres', '3105566778', 'ana.torres@example.com', 'ana123', 1, 'Ecuador', 'Psicóloga'),
(192847561, 'Luisa', 'Martínez', '3100001122', 'luisa@example.com', 'luisa321', 1, 'Chile', 'Abogada'),
(198374652, 'Roberto', 'Santos', '3145678901', 'roberto.s@example.com', 'robpass', 1, 'Uruguay', 'Profesor'),
(1033183372, 'roger', 'arenas', '32182222', 'roger@gmail.com', '1234', 1, 'medellin', 'estudiante'),
(1682739452, 'Pedro', 'López', '3156789012', 'pedro@example.com', 'pedropass', 1, 'Perú', 'Contador'),
(1693847203, 'Diana', 'Castillo', '3156789013', 'diana.c@example.com', 'dianapass', 1, 'Bolivia', 'Arquitecta'),
(1789453621, 'Laura', 'Mendoza', '3134567890', 'laura.m@example.com', 'lauram', 1, 'España', 'Enfermera'),
(1857369401, 'Juan', 'Pérez', '3129876543', 'juan@example.com', 'juanpass', 1, 'Argentina', 'Diseñador'),
(1857392045, 'Miguel', 'Herrera', '3123456789', 'miguelh@example.com', 'migpass', 1, 'Colombia', 'Chef');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mandatoryservice`
--

CREATE TABLE `mandatoryservice` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mandatoryservice`
--

INSERT INTO `mandatoryservice` (`id`, `name`, `description`, `price`) VALUES
(1, 'Desayuno', 'Desayuno continental servido de 7:00 a 10:00 AM', 0),
(2, 'Limpieza diaria', 'Servicio de limpieza de habitación todos los días', 0),
(3, 'WiFi', 'Acceso a Internet de alta velocidad en todo el hotel', 0),
(4, 'Check-in 24h', 'Recepción disponible para check-in las 24 horas', 0),
(5, 'Caja fuerte', 'Caja fuerte individual en cada habitación', 0),
(6, 'Estacionamiento', 'Parqueadero privado para huéspedes', 12000),
(7, 'Acceso a gimnasio', 'Uso del gimnasio del hotel', 4000),
(8, 'Agua embotellada', 'Botella de agua diaria por huésped', 3500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `optionalservice`
--

CREATE TABLE `optionalservice` (
  `id_optionalService` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `optionalservice`
--

INSERT INTO `optionalservice` (`id_optionalService`, `name`, `description`, `price`) VALUES
(1, 'Spa', 'Acceso al spa con jacuzzi, sauna y masajes', 45000),
(2, 'Lavandería', 'Servicio de lavado y planchado de ropa', 16000),
(3, 'Minibar', 'Consumo del minibar dentro de la habitación', 50000),
(4, 'Transporte al aeropuerto', 'Traslado ida o vuelta al aeropuerto', 15000),
(5, 'Tour local', 'Excursión guiada por los puntos turísticos de la ciudad', 30000),
(6, 'Alquiler de bicicletas', 'Bicicletas disponibles para recorrer la ciudad', 9000),
(7, 'Desayuno premium', 'Desayuno buffet con opciones gourmet y café especial', 24000),
(8, 'Room Service', 'Servicio a la habitación disponible 24 horas', 20000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bedroom`
--
ALTER TABLE `bedroom`
  ADD PRIMARY KEY (`id_bedroom`);

--
-- Indices de la tabla `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id_booking`),
  ADD KEY `id_guest` (`id_guest`),
  ADD KEY `id_bedroom` (`id_bedroom`);

--
-- Indices de la tabla `booking_optionalservice`
--
ALTER TABLE `booking_optionalservice`
  ADD PRIMARY KEY (`id_booking`,`id_optionalService`),
  ADD KEY `id_optionalService` (`id_optionalService`);

--
-- Indices de la tabla `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `guest`
--
ALTER TABLE `guest`
  ADD PRIMARY KEY (`id_guest`);

--
-- Indices de la tabla `mandatoryservice`
--
ALTER TABLE `mandatoryservice`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `optionalservice`
--
ALTER TABLE `optionalservice`
  ADD PRIMARY KEY (`id_optionalService`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `bedroom`
--
ALTER TABLE `bedroom`
  MODIFY `id_bedroom` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `booking`
--
ALTER TABLE `booking`
  MODIFY `id_booking` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `mandatoryservice`
--
ALTER TABLE `mandatoryservice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `optionalservice`
--
ALTER TABLE `optionalservice`
  MODIFY `id_optionalService` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`id_guest`) REFERENCES `guest` (`id_guest`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`id_bedroom`) REFERENCES `bedroom` (`id_bedroom`);

--
-- Filtros para la tabla `booking_optionalservice`
--
ALTER TABLE `booking_optionalservice`
  ADD CONSTRAINT `booking_optionalservice_ibfk_1` FOREIGN KEY (`id_booking`) REFERENCES `booking` (`id_booking`),
  ADD CONSTRAINT `booking_optionalservice_ibfk_2` FOREIGN KEY (`id_optionalService`) REFERENCES `optionalservice` (`id_optionalService`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

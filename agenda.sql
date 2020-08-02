-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 02-08-2020 a las 01:18:43
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda`
--
DROP DATABASE IF EXISTS `agenda`;
CREATE DATABASE IF NOT EXISTS `agenda` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `agenda`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libreta`
--

DROP TABLE IF EXISTS `libreta`;
CREATE TABLE IF NOT EXISTS `libreta` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `apellidos` varchar(30) NOT NULL,
  `nombres` varchar(30) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `libreta`
--

INSERT INTO `libreta` (`id`, `apellidos`, `nombres`, `direccion`, `telefono`, `email`) VALUES
(1, 'Abad Abad', 'Luis Antonio', 'Cdla. Samanes 7 Mz 345 Villa 18', '042-854345', 'luis.abad36@hotmail.com'),
(2, 'Abad Castro', 'Jose Fernando', 'Cdla. Sauces 4 Mz 236 Villa 23', '042-238564', 'abad40@yahoo.es'),
(3, 'Andrade Castro', 'Carlos Jose', 'Cdla. Sauces 7 Mz 234 Villa 23', '042-237865', 'castro2@yahoo.com'),
(4, 'Andrade Veliz', 'Josue Alejandro', 'Cdla. Martha de Roldos', '042-256895', 'josue48@gmail.com'),
(7, 'Frugone Jaramillo', 'Jose Fernando', 'Cdla. Sauces 2 Mz F50 Villa 12', '0992826240', 'frugonejose1970@gmail.com');
--
-- Base de datos: `master_python`
--
DROP DATABASE IF EXISTS `master_python`;
CREATE DATABASE IF NOT EXISTS `master_python` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `master_python`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

DROP TABLE IF EXISTS `vehiculos`;
CREATE TABLE IF NOT EXISTS `vehiculos` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `marca` varchar(40) NOT NULL,
  `modelo` varchar(40) NOT NULL,
  `precio` float(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`id`, `marca`, `modelo`, `precio`) VALUES
(10, 'mazda', '4X4', 90000.00),
(9, 'volvo', 'san', 85000.00),
(8, 'seat', 'León', 56000.00),
(7, 'Opel', 'Astra', 45000.00),
(12, 'Citroen', 'Sazo', 65000.00);
--
-- Base de datos: `test`
--
DROP DATABASE IF EXISTS `test`;
CREATE DATABASE IF NOT EXISTS `test` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `test`;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

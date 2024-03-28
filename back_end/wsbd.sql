-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 28-03-2024 a las 21:34:41
-- Versión del servidor: 11.0.5-MariaDB-1:11.0.5+maria~ubu2204
-- Versión de PHP: 8.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `wsdb`
--
CREATE DATABASE IF NOT EXISTS `wsdb` DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci;
USE `wsdb`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `result`
--

DROP TABLE IF EXISTS `result`;
CREATE TABLE IF NOT EXISTS `result` (
  `row_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url_data` varchar(500) NOT NULL,
  `cat1` tinytext NOT NULL,
  `cat2` tinytext DEFAULT NULL,
  `cat3` tinytext DEFAULT NULL,
  `cat4` tinytext DEFAULT NULL,
  `cat5` tinytext DEFAULT NULL,
  `spare1` varchar(500) DEFAULT NULL,
  `spare2` varchar(500) DEFAULT NULL,
  `spare3` varchar(500) DEFAULT NULL,
  `spare4` varchar(500) DEFAULT NULL,
  `spare5` varchar(500) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `last_edit_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `lat-edit_comment` varchar(500) DEFAULT NULL,
  `user_id` varchar(100) NOT NULL,
  PRIMARY KEY (`url_data`),
  UNIQUE KEY `IX_userid` (`user_id`),
  KEY `IX_rowid` (`row_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='webscrapping results from ML api';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_name`
--

DROP TABLE IF EXISTS `user_name`;
CREATE TABLE IF NOT EXISTS `user_name` (
  `row_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) NOT NULL,
  `user_desc` varchar(500) DEFAULT NULL,
  `encrypt_pw` varchar(254) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `spare1` varchar(500) DEFAULT NULL,
  `spare2` varchar(500) DEFAULT NULL,
  `spare3` varchar(500) DEFAULT NULL,
  `spare4` varchar(500) DEFAULT NULL,
  `spare5` varchar(500) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `last_edit_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `last_edit_comment` text DEFAULT NULL,
  PRIMARY KEY (`row_id`),
  UNIQUE KEY `IXU_userid` (`user_id`),
  KEY `IX_rowid` (`row_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user_name`
--

INSERT INTO `user_name` (`row_id`, `user_id`, `user_desc`, `encrypt_pw`, `active`, `spare1`, `spare2`, `spare3`, `spare4`, `spare5`, `created_at`, `last_edit_at`, `last_edit_comment`) VALUES
(1, 'yoniliman galvis', 'ygalves', '*8AFC0CA0F7C50F936718A34CE1C071D51F646074', 1, NULL, NULL, NULL, NULL, NULL, '2024-03-26 21:12:41', '2024-03-26 21:12:41', 'first test'),
(2, 'guillermo zapata', 'gzapata', '*8AFC0CA0F7C50F936718A34CE1C071D51F646074', 1, NULL, NULL, NULL, NULL, NULL, '2024-03-26 21:13:24', '2024-03-26 21:13:24', 'second test'),
(3, 'jairo velez', 'jvelez', '*8AFC0CA0F7C50F936718A34CE1C071D51F646074', 1, NULL, NULL, NULL, NULL, NULL, '2024-03-26 21:14:16', '2024-03-26 21:14:16', 'third test');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `result`
--
ALTER TABLE `result`
  ADD CONSTRAINT `result_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_name` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

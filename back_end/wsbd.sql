-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 31-03-2024 a las 01:16:33
-- Versión del servidor: 11.0.5-MariaDB-1:11.0.5+maria~ubu2204
-- Versión de PHP: 8.2.17

--
-- UAO IA SPECIALIST 
-- WEBSCRAPPING DATABASE CREATING 
--  IA TASKFORCE - 2024
-- V: 3.0.0
-- Create List table, update db structure and set user_name trigger to create default global list

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
-- Estructura de tabla para la tabla `user_name`
--

DROP TABLE IF EXISTS `user_name`;
CREATE TABLE `user_name` (
  `row_id` bigint(20) NOT NULL,
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
  `last_edit_comment` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Disparadores `user_name`
--
DROP TRIGGER IF EXISTS `TRG_list`;
DELIMITER $$
CREATE TRIGGER `TRG_list_usrn` AFTER INSERT ON `user_name` FOR EACH ROW INSERT INTO `list`(`list_name`, `user_id`, `last_edit_comment`) VALUES ('global',NEW.row_id,'root')
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `list`
--

DROP TABLE IF EXISTS `list`;
CREATE TABLE `list` (
  `row_id` bigint(20) NOT NULL,
  `list_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `spare1` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `spare2` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `spare3` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `spare4` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `spare5` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `last_edit_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `last_edit_comment` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `result`
--

DROP TABLE IF EXISTS `result`;
CREATE TABLE `result` (
  `row_id` bigint(20) NOT NULL,
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
  `last_edit_comment` varchar(500) DEFAULT NULL,
  `list_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='webscrapping results from ML api';

-- --------------------------------------------------------

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `list`
--
ALTER TABLE `list`
  ADD PRIMARY KEY (`row_id`) USING BTREE,
  ADD UNIQUE KEY `IX_list_user_lst` (`list_name`,`user_id`) USING BTREE,
  ADD KEY `IX_userid_lst` (`user_id`);

--
-- Indices de la tabla `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`row_id`) USING BTREE,
  ADD KEY `IX_user_url_rslt` (`user_id`,`url_data`) USING BTREE,
  ADD KEY `IX_list_url_rslt` (`list_id`,`url_data`) USING BTREE;

--
-- Indices de la tabla `user_name`
--
ALTER TABLE `user_name`
  ADD PRIMARY KEY (`row_id`),
  ADD UNIQUE KEY `IX_userid_usrn` (`user_id`),
  ADD KEY `IX_rowid_usrn` (`row_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `list`
--
ALTER TABLE `list`
  MODIFY `row_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de la tabla `result`
--
ALTER TABLE `result`
  MODIFY `row_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de la tabla `user_name`
--
ALTER TABLE `user_name`
  MODIFY `row_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `list`
--
ALTER TABLE `list`
  ADD CONSTRAINT `list_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_name` (`row_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `result`
--
ALTER TABLE `result`
  ADD CONSTRAINT `result_ibfk_1` FOREIGN KEY (`list_id`) REFERENCES `list` (`row_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `result_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_name` (`row_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
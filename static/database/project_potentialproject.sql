-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 28, 2013 at 08:48 PM
-- Server version: 5.5.32
-- PHP Version: 5.3.10-1ubuntu3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `inventionlog`
--

-- --------------------------------------------------------

--
-- Table structure for table `project_potentialproject`
--

CREATE TABLE IF NOT EXISTS `project_potentialproject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(50) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `number` int(11) NOT NULL,
  `patent_file` varchar(100) NOT NULL,
  `client_name` varchar(50) NOT NULL,
  `client_email` varchar(75) DEFAULT NULL,
  `client_phone` varchar(13) DEFAULT NULL,
  `assigned` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_name` (`project_name`),
  KEY `project_potentialproject_f52cfca0` (`slug`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `project_potentialproject`
--

INSERT INTO `project_potentialproject` (`id`, `project_name`, `slug`, `number`, `patent_file`, `client_name`, `client_email`, `client_phone`, `assigned`) VALUES
(1, 'Android OS', 'android-os', 12345678, 'pics/patents/idea.png', 'Will Huffmyer', 'williehuffmyer@gmail.com', '412-496-1545', 0),
(2, 'Ubuntu OS', 'ubuntu-os', 87654321, 'pics/patents/Ubuntu-logo.png', 'Brant Meier', 'youngwebking@gmail.com', '724-923-3829', 0),
(3, 'Google Chrome', 'google-chrome', 12348765, 'pics/patents/chrome-logo.png', 'Google', 'google@gmail.com', '', 0),
(4, 'Firefox OS', 'firefox-os', 97531246, 'pics/patents/firefox-logo.png', 'Firefox ', 'fire@fox.com', '', 0),
(5, '20x20 Rubik''s Cube', '20x20-rubiks-cube', 74853984, 'pics/patents/20x20cube.jpg', 'Brant Meier', 'youngwebking@gmail.com', '724-923-3829', 0),
(6, 'Mecha Battle Suit', 'mecha-battle-suit', 83694328, 'pics/patents/avatar_ampsuit.jpg', 'Brant Meier', 'youngwebking@gmail.com', '724-923-3829', 0),
(7, 'Metroid Prime', 'metroid-prime', 33333333, 'pics/patents/TallonMetroid.png', 'Chad Meier', 'chadragon@gmail.com', '724-923-3829', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

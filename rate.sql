-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 25 Ağu 2020, 15:19:19
-- Sunucu sürümü: 5.7.31
-- PHP Sürümü: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `exchange`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `rate`
--

DROP TABLE IF EXISTS `rate`;
CREATE TABLE IF NOT EXISTS `rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `urunkodu` int(11) NOT NULL,
  `maliyet` int(11) NOT NULL,
  `satis` int(11) NOT NULL,
  `kur` float NOT NULL,
  `sonuc` float NOT NULL,
  `kar` int(11) NOT NULL,
  `kod` int(11) NOT NULL,
  `dolarkuru` int(11) NOT NULL,
  `sonuc2` int(11) NOT NULL,
  `netkar` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=latin5;

--
-- Tablo döküm verisi `rate`
--

INSERT INTO `rate` (`id`, `urunkodu`, `maliyet`, `satis`, `kur`, `sonuc`, `kar`, `kod`, `dolarkuru`, `sonuc2`, `netkar`) VALUES
(33, 123456, 20, 60, 5, 200, 40, 123456, 6, 240, 40),
(34, 147258, 40, 90, 5.89, 294, 50, 147258, 7, 342, 47),
(35, 147258, 40, 90, 5.89, 294, 50, 147258, 3, 156, -138),
(36, 20, 30, 60, 5.78, 173, 30, 20, 8, 241, 67),
(37, 23, 5, 20, 5.65, 84, 15, 23, 3, 46, -38),
(38, 147258, 20, 80, 5.87, 352, 60, 147258, 6, 354, 1),
(39, 147258, 20, 80, 5.87, 352, 60, 147258, 6, 358, 6),
(40, 147258, 20, 40, 5.87, 117, 20, 147258, 6, 119, 1),
(41, 147258, 20, 40, 8.05, 161, 20, 147258, 5, 107, -54),
(42, 147258, 20, 40, 6.12, 122, 20, 147258, 7, 143, 20);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

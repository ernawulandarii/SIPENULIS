-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Jul 2020 pada 14.53
-- Versi server: 10.1.37-MariaDB
-- Versi PHP: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_skripsi`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `collect_data`
--

CREATE TABLE `collect_data` (
  `id_user` int(11) DEFAULT NULL,
  `number_1` text,
  `number_2` text,
  `number_3` text,
  `number_4` text,
  `number_5` text,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `collect_data`
--


-- --------------------------------------------------------

--
-- Struktur dari tabel `rabinkarp_score`
--

CREATE TABLE `rabinkarp_score` (
  `id_user` int(11) NOT NULL,
  `score_1` float NOT NULL,
  `hr_1` int(11) NOT NULL,
  `acc_1` float NOT NULL,
  `score_2` float NOT NULL,
  `hr_2` int(11) NOT NULL,
  `acc_2` float NOT NULL,
  `score_3` float NOT NULL,
  `hr_3` int(11) NOT NULL,
  `acc_3` float NOT NULL,
  `score_4` float NOT NULL,
  `hr_4` int(11) NOT NULL,
  `acc_4` float NOT NULL,
  `score_5` float NOT NULL,
  `hr_5` int(11) NOT NULL,
  `acc_5` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `score`
--

CREATE TABLE `score` (
  `id_user` int(11) NOT NULL,
  `score` float DEFAULT NULL,
  `human_rater` int(11) NOT NULL,
  `accuracy_rk` float DEFAULT NULL,
  `exec_time` float DEFAULT NULL,
  `submitted` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `sentence`
--

CREATE TABLE `sentence` (
  `id_sentence` int(11) NOT NULL,
  `jap_sentence` varchar(150) DEFAULT NULL,
  `array_token_sur` text,
  `array_token_pro` text,
  `sum_token` int(11) DEFAULT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `role` varchar(20) NOT NULL,
  `name` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `last_login` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id_user`, `role`, `name`, `username`, `password`, `last_login`) VALUES
(1, 'default', 'Mahasiswa1', 'student1', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 11:10:28'),
(2, 'default', 'Mahasiswa2', 'student2', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 11:15:30'),
(3, 'default', 'Mahasiswa3', 'student3', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 11:34:47'),
(4, 'default', 'Mahasiswa4', 'student4', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 11:43:15'),
(5, 'default', 'Mahasiswa5', 'student5', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 12:29:39'),
(6, 'default', 'Mahasiswa6', 'student6', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 23:05:11'),
(7, 'default', 'Mahasiswa7', 'student7', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 20:36:04'),
(8, 'default', 'Mahasiswa8', 'student8', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 20:52:07'),
(9, 'default', 'Mahasiswa9', 'student9', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 21:10:54'),
(10, 'default', 'Mahasiswa10', 'student10', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 23:08:18'),
(11, 'default', 'Mahasiswa11', 'student11', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 23:28:41'),
(12, 'default', 'Mahasiswa12', 'student12', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 18:56:32'),
(13, 'default', 'Mahasiswa13', 'student13', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 21:38:42'),
(14, 'default', 'Mahasiswa14', 'student14', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 21:44:53'),
(15, 'default', 'Mahasiswa15', 'student15', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 23:19:39'),
(16, 'default', 'Mahasiswa16', 'student16', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 19:30:01'),
(17, 'default', 'Mahasiswa17', 'student17', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 19:36:25'),
(18, 'default', 'Mahasiswa18', 'student18', '6df45266031e8d03f3e2458b9f634c7b', '2020-06-28 03:03:57'),
(19, 'default', 'Mahasiswa19', 'student19', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 16:22:15'),
(20, 'default', 'Mahasiswa20', 'student20', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 22:30:56'),
(21, 'default', 'Mahasiswa21', 'student21', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 17:38:55'),
(22, 'default', 'Mahasiswa22', 'student22', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-03 23:46:24'),
(23, 'default', 'Mahasiswa23', 'student23', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 22:00:02'),
(24, 'default', 'Mahasiswa24', 'student24', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 01:25:00'),
(25, 'default', 'Mahasiswa25', 'student25', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 01:12:46'),
(26, 'default', 'Mahasiswa26', 'student26', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 15:04:40'),
(27, 'default', 'Mahasiswa27', 'student27', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:54:04'),
(28, 'default', 'Mahasiswa28', 'student28', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-04 16:49:34'),
(29, 'default', 'Mahasiswa29', 'student29', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(30, 'default', 'Mahasiswa30', 'student30', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(31, 'default', 'Mahasiswa31', 'student31', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(32, 'default', 'Mahasiswa32', 'student32', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(33, 'default', 'Mahasiswa33', 'student33', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(34, 'default', 'Mahasiswa34', 'student34', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(35, 'default', 'Mahasiswa35', 'student35', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(36, 'default', 'Mahasiswa36', 'student36', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(37, 'default', 'Mahasiswa37', 'student37', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(38, 'default', 'Mahasiswa38', 'student38', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(39, 'default', 'Mahasiswa39', 'student39', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(40, 'default', 'Mahasiswa40', 'student40', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(41, 'default', 'Mahasiswa41', 'student41', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(43, 'default', 'Mahasiswa42', 'student42', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:49:14'),
(42, 'default', 'Mahasiswa43', 'student43', '6df45266031e8d03f3e2458b9f634c7b', '2020-07-05 00:45:43');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `rabinkarp_score`
--
ALTER TABLE `rabinkarp_score`
  ADD PRIMARY KEY (`id_user`);

--
-- Indeks untuk tabel `score`
--
ALTER TABLE `score`
  ADD PRIMARY KEY (`id_user`);

--
-- Indeks untuk tabel `sentence`
--
ALTER TABLE `sentence`
  ADD PRIMARY KEY (`id_sentence`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

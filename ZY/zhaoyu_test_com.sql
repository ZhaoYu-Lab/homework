-- phpMyAdmin SQL Dump
-- version 4.0.10.19
-- https://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2019-12-08 19:15:32
-- 服务器版本: 5.5.62-log
-- PHP 版本: 5.4.45

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `zhaoyu_test_com`
--

-- --------------------------------------------------------

--
-- 表的结构 `classes`
--

CREATE TABLE IF NOT EXISTS `classes` (
  `classNum` varchar(20) NOT NULL,
  `classLat` double NOT NULL,
  `classLon` double NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `classes`
--

INSERT INTO `classes` (`classNum`, `classLat`, `classLon`) VALUES
('8号J101', 251.365245123, 93.6547982134);

-- --------------------------------------------------------

--
-- 表的结构 `counsellorinfo`
--

CREATE TABLE IF NOT EXISTS `counsellorinfo` (
  `Account` varchar(20) NOT NULL,
  `Pwd` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `counsellorinfo`
--

INSERT INTO `counsellorinfo` (`Account`, `Pwd`) VALUES
('4020152434', '123456');

-- --------------------------------------------------------

--
-- 表的结构 `courses`
--

CREATE TABLE IF NOT EXISTS `courses` (
  `courseNum` varchar(20) NOT NULL,
  `courseName` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `courses`
--

INSERT INTO `courses` (`courseNum`, `courseName`) VALUES
('11111111', '软件工程');

-- --------------------------------------------------------

--
-- 表的结构 `sign`
--

CREATE TABLE IF NOT EXISTS `sign` (
  `_id` int(11) NOT NULL AUTO_INCREMENT,
  `signTime` datetime NOT NULL,
  `studentNum` varchar(20) NOT NULL,
  `courseNum` varchar(20) NOT NULL,
  `teacherNum` varchar(20) NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  `studentClass` varchar(20) NOT NULL,
  `studentDepart` varchar(20) NOT NULL,
  `classState` varchar(20) NOT NULL,
  `IMEI` varchar(20) NOT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `sign`
--

INSERT INTO `sign` (`_id`, `signTime`, `studentNum`, `courseNum`, `teacherNum`, `startTime`, `endTime`, `studentClass`, `studentDepart`, `classState`, `IMEI`) VALUES
(1, '2019-11-10 09:00:00', '15090087', '11111111', '25090087', '2019-11-10 08:00:00', '2019-11-10 10:00:00', '15智72', '计算机学院', '正常', '0254123658956');

-- --------------------------------------------------------

--
-- 表的结构 `studentbind`
--

CREATE TABLE IF NOT EXISTS `studentbind` (
  `studentNum` varchar(20) NOT NULL,
  `stuAccount` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `studentbind`
--

INSERT INTO `studentbind` (`studentNum`, `stuAccount`) VALUES
('15090087', '3020152434');

-- --------------------------------------------------------

--
-- 表的结构 `studentinfo`
--

CREATE TABLE IF NOT EXISTS `studentinfo` (
  `Account` varchar(20) NOT NULL,
  `Pwd` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `studentinfo`
--

INSERT INTO `studentinfo` (`Account`, `Pwd`) VALUES
('3020152434', '123456');

-- --------------------------------------------------------

--
-- 表的结构 `students`
--

CREATE TABLE IF NOT EXISTS `students` (
  `studentNum` varchar(20) NOT NULL,
  `studentName` varchar(20) NOT NULL,
  `studentSex` varchar(20) NOT NULL,
  `studentClass` varchar(20) NOT NULL,
  `studentDepart` varchar(20) NOT NULL,
  `studentMail` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `students`
--

INSERT INTO `students` (`studentNum`, `studentName`, `studentSex`, `studentClass`, `studentDepart`, `studentMail`) VALUES
('15090087', 'zzz', '男', '15智72', '计算机学院', '2413101243@qq.com');

-- --------------------------------------------------------

--
-- 表的结构 `supervisorinfo`
--

CREATE TABLE IF NOT EXISTS `supervisorinfo` (
  `Account` varchar(20) NOT NULL,
  `Pwd` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `supervisorinfo`
--

INSERT INTO `supervisorinfo` (`Account`, `Pwd`) VALUES
('5020152434', '123456');

-- --------------------------------------------------------

--
-- 表的结构 `teachers`
--

CREATE TABLE IF NOT EXISTS `teachers` (
  `teacherNum` varchar(20) NOT NULL,
  `teacherName` varchar(20) NOT NULL,
  `teacherSex` varchar(20) NOT NULL,
  `teacherDepart` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `teachers`
--

INSERT INTO `teachers` (`teacherNum`, `teacherName`, `teacherSex`, `teacherDepart`) VALUES
('25090087', 'yyy', '女', '计算机学院');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

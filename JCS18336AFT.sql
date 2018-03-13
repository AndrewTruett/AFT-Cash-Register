-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 13, 2018 at 06:49 PM
-- Server version: 10.2.7-MariaDB
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `JCS18336AFT`
--

-- --------------------------------------------------------

--
-- Table structure for table `AgeRestrictedItem`
--

CREATE TABLE `AgeRestrictedItem` (
  `Name` varchar(64) NOT NULL,
  `Stock` varchar(64) NOT NULL,
  `Price` int(64) NOT NULL,
  `Sale Price` int(64) NOT NULL,
  `Required Age` int(64) NOT NULL,
  `UPC` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Cashier`
--

CREATE TABLE `Cashier` (
  `employeeID` int(32) NOT NULL,
  `Name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `General Item`
--

CREATE TABLE `General Item` (
  `Item Name` varchar(64) NOT NULL,
  `Stock` varchar(64) NOT NULL,
  `Price` int(64) NOT NULL,
  `Sale Price` int(64) NOT NULL,
  `Member Price` int(64) NOT NULL,
  `UPC` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Manager`
--

CREATE TABLE `Manager` (
  `employeeID` int(11) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Pin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Member`
--

CREATE TABLE `Member` (
  `MemberId` int(64) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Total Points` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Produce`
--

CREATE TABLE `Produce` (
  `Name` varchar(64) NOT NULL,
  `Stock` varchar(64) NOT NULL,
  `Price` int(64) NOT NULL,
  `Sale Price` int(64) NOT NULL,
  `Member Price` int(64) NOT NULL,
  `PLU` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `AgeRestrictedItem`
--
ALTER TABLE `AgeRestrictedItem`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `Cashier`
--
ALTER TABLE `Cashier`
  ADD PRIMARY KEY (`employeeID`);

--
-- Indexes for table `General Item`
--
ALTER TABLE `General Item`
  ADD PRIMARY KEY (`Item Name`);

--
-- Indexes for table `Manager`
--
ALTER TABLE `Manager`
  ADD PRIMARY KEY (`employeeID`);

--
-- Indexes for table `Member`
--
ALTER TABLE `Member`
  ADD PRIMARY KEY (`MemberId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Cashier`
--
ALTER TABLE `Cashier`
  MODIFY `employeeID` int(32) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Manager`
--
ALTER TABLE `Manager`
  MODIFY `employeeID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Member`
--
ALTER TABLE `Member`
  MODIFY `MemberId` int(64) NOT NULL AUTO_INCREMENT;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

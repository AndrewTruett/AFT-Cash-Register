-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 29, 2018 at 06:54 PM
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
  `MemberId` int(11) NOT NULL,
  `Price` decimal(64,2) NOT NULL,
  `Required Age` int(64) NOT NULL,
  `UPC` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `AgeRestrictedItem`
--

INSERT INTO `AgeRestrictedItem` (`Name`, `MemberId`, `Price`, `Required Age`, `UPC`) VALUES
('Benson & Hedges', 15, '26.99', 21, 123097),
('Cider', 1, '16.99', 21, 123675),
('Cognac & Brandy', 11, '21.88', 21, 123980),
('Coors Light 6 pack', 3, '4.00', 21, 999258),
('Dunhill', 5, '17.77', 19, 123076),
('Gin & Rum', 25, '34.55', 21, 123789),
('L & M Cigarette', 34, '12.99', 19, 123976),
('Marlboro Light', 1, '14.99', 18, 999123),
('Newport', 23, '18.77', 19, 123087),
('Pall Mall Cigarette Packs', 21, '13.88', 19, 123865),
('Rose Wine', 27, '34.99', 21, 123567),
('Sparkling Wine', 15, '45.88', 21, 123408),
('Tequila', 6, '24.88', 21, 123465),
('Vermouth', 31, '34.88', 21, 123987),
('Vodka', 7, '33.88', 21, 123454),
('Whiskey', 13, '28.77', 21, 123786),
('White Wine', 4, '76.88', 21, 123409),
('Winston Cigarette', 16, '14.66', 19, 123986);

-- --------------------------------------------------------

--
-- Table structure for table `Cashier`
--

CREATE TABLE `Cashier` (
  `employeeID` int(32) NOT NULL,
  `Name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Cashier`
--

INSERT INTO `Cashier` (`employeeID`, `Name`) VALUES
(261729, 'Antonio Griezzman'),
(543212, 'Sarah Evans'),
(673451, 'Syed Neaz'),
(675400, 'Mark Fisher'),
(745872, 'John Holt');

-- --------------------------------------------------------

--
-- Table structure for table `Categories`
--

CREATE TABLE `Categories` (
  `CtaegoryId` int(11) NOT NULL,
  `Category name` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Categories`
--

INSERT INTO `Categories` (`CtaegoryId`, `Category name`) VALUES
(1, 'Bakery'),
(2, 'Pastries'),
(3, 'Seafood'),
(4, 'Meat & Poultry'),
(5, 'Frozen'),
(6, 'Dairy'),
(7, 'Vegetables'),
(8, 'Meals'),
(9, 'Cheese'),
(10, 'Beverages');

-- --------------------------------------------------------

--
-- Table structure for table `General Item`
--

CREATE TABLE `General Item` (
  `CategoryId` int(64) NOT NULL,
  `Item Name` varchar(64) NOT NULL,
  `Price` double(64,2) NOT NULL,
  `UPC` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `General Item`
--

INSERT INTO `General Item` (`CategoryId`, `Item Name`, `Price`, `UPC`) VALUES
(9, 'American ', 1.88, 111287),
(8, 'Appetizers', 3.77, 222452),
(7, 'Avocados', 5.88, 333564),
(1, 'Bagels', 1.00, 2356),
(2, 'Baking Kits', 3.00, 666056),
(7, 'Beans & Peas', 4.99, 333564),
(4, 'Beef', 7.98, 555443),
(6, 'Biscuits & Doughs', 5.88, 444567),
(9, 'Blue', 0.88, 111098),
(1, 'Breads', 1.00, 2660),
(8, 'Breakfast', 3.77, 222098),
(5, 'Breakfast Food', 5.49, 777564),
(9, 'Brie & Camemebert', 1.88, 111876),
(7, 'Brocolli', 4.77, 333674),
(6, 'Butter & Cream Cheese', 4.99, 444898),
(7, 'Cabage', 6.88, 333452),
(2, 'Cakes & Cupcakes', 5.00, 666076),
(7, 'Carrots', 3.77, 333212),
(9, 'Cheddar & Jack', 2.88, 111298),
(9, 'Cheese Plates', 2.45, 111665),
(4, 'Chicken', 7.88, 555454),
(10, 'Coke', 1.88, 234),
(2, 'Cookies & Bars', 1.00, 2367),
(7, 'Corns', 2.88, 333452),
(3, 'Crabs', 10.00, 888767),
(1, 'Croissants & Danish', 2.00, 999212),
(10, 'Crush Orange', 2.17, 875),
(7, 'Cucumbers', 8.66, 333412),
(8, 'Desi Salads', 10.55, 222359),
(5, 'Desserts & Toppings', 8.49, 777060),
(1, 'Donuts', 1.00, 999098),
(4, 'Duck', 9.76, 555432),
(8, 'Easter Diners', 7.66, 222343),
(7, 'EggPlants', 7.66, 333010),
(6, 'Eggs', 2.88, 444565),
(8, 'Entees', 8.77, 222134),
(10, 'Fantas', 1.66, 976),
(9, 'Feta', 3.77, 111298),
(5, 'Fish', 8.00, 1267),
(3, 'Fish Steaks', 19.00, 888909),
(7, 'Fresh Herbs', 3.88, 333456),
(10, 'Gingerale', 1.77, 877),
(9, 'Gouda', 1.78, 111765),
(8, 'Green Salads', 4.77, 222198),
(4, 'Ground Patties & Sausage', 9.49, 555897),
(6, 'Hummus', 4.99, 444321),
(5, 'Ice Creams', 25.49, 777453),
(10, 'Juices', 3.88, 764),
(4, 'Lamb', 8.98, 555676),
(3, 'Lobsters', 28.49, 888565),
(6, 'Milk', 3.47, 444678),
(9, 'Mozzarella', 3.64, 111200),
(2, 'Muffins', 2.00, 666356),
(3, 'Mussels & Clams', 34.55, 888978),
(7, 'Onions & Garlics', 3.99, 333098),
(5, 'Pastas', 6.88, 777651),
(2, 'Pies & Tarts', 4.00, 666987),
(4, 'Pork', 7.88, 555123),
(2, 'Puddings', 4.00, 666878),
(1, 'Rolls & Buns', 1.00, 999333),
(3, 'Salmons', 20.00, 888765),
(6, 'Salsa & Goucamole', 8.49, 444120),
(8, 'Sandwiches & Wraps', 4.99, 222876),
(9, 'Sheep', 4.88, 111786),
(8, 'Sides', 3.66, 222764),
(10, 'Smoothies', 2.88, 786),
(6, 'Snacks Packs', 5.23, 444126),
(5, 'Soup & Broth', 5.99, 777867),
(8, 'Soup & Chili', 8.99, 222096),
(6, 'Soy & Vegeterian', 7.66, 444532),
(10, 'Sprite', 2.17, 986),
(8, 'Sushi', 7.55, 222197),
(9, 'Swiss', 1.66, 111245),
(4, 'Turkey', 19.77, 555039),
(3, 'Wild cod Filet', 16.00, 888654),
(6, 'Yogurt', 5.77, 444565);

-- --------------------------------------------------------

--
-- Table structure for table `Manager`
--

CREATE TABLE `Manager` (
  `employeeID` int(11) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Pin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Manager`
--

INSERT INTO `Manager` (`employeeID`, `Name`, `Pin`) VALUES
(354521, 'David Fox', 2580);

-- --------------------------------------------------------

--
-- Table structure for table `Member`
--

CREATE TABLE `Member` (
  `MemberId` int(64) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Total Points` int(64) NOT NULL,
  `Age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Member`
--

INSERT INTO `Member` (`MemberId`, `Name`, `Total Points`, `Age`) VALUES
(1, 'Eliza William', 3443, 22),
(2, 'Mark Wayne', 240, 33),
(3, 'Carrie Fisher', 467, 19),
(4, 'Aaron Hank', 2221, 43),
(5, 'Edward Abbey', 211, 31),
(6, 'Henry Adams', 3000, 55),
(7, 'Alfred Adler', 2887, 25),
(8, 'Khalil Ahmed', 988, 23),
(9, 'Steven Smith', 321, 21),
(10, 'Jessica Alba', 2981, 33),
(11, 'Irina Jay', 2198, 22),
(12, 'Tom Aryana', 2188, 28),
(13, 'Fiona Thomas', 3221, 21),
(14, 'Bean Roy', 2144, 22),
(15, 'Eric Berne', 8876, 43),
(16, 'Frank Biondo', 2100, 54),
(17, 'David Bohm', 500, 65),
(18, 'Omar Bradley', 288, 32),
(19, 'Rachel Carson', 277, 32),
(20, 'Yun Zang', 988, 41),
(21, 'Jim Crase', 165, 21),
(22, 'John Dean', 962, 77),
(23, 'Joe Burns', 217, 44),
(24, 'Diana Wales', 123, 43),
(25, 'Dave Edward', 654, 24),
(26, 'Paul Elwiard', 543, 17),
(27, 'Bob Ezrin', 3217, 32),
(28, 'Peter Gabriel', 298, 55),
(29, 'Samir Khan', 212, 66),
(30, 'Eric Gill', 765, 55),
(31, 'Leo Ray', 129, 29),
(32, 'Wein Hyat', 541, 32),
(33, 'Wiiliam Golding', 776, 32),
(34, 'Gunter Grass', 123, 38),
(35, 'Priyanka Chopra', 543, 45),
(36, 'Paul Hervey', 257, 51),
(37, 'Mitch Marsh', 786, 30),
(38, 'Shaun Payne', 886, 20);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `AgeRestrictedItem`
--
ALTER TABLE `AgeRestrictedItem`
  ADD PRIMARY KEY (`Name`),
  ADD KEY `bought_member` (`MemberId`);

--
-- Indexes for table `Cashier`
--
ALTER TABLE `Cashier`
  ADD PRIMARY KEY (`employeeID`);

--
-- Indexes for table `Categories`
--
ALTER TABLE `Categories`
  ADD PRIMARY KEY (`CtaegoryId`);

--
-- Indexes for table `General Item`
--
ALTER TABLE `General Item`
  ADD PRIMARY KEY (`Item Name`),
  ADD KEY `CategoryId` (`CategoryId`),
  ADD KEY `CategoryId_2` (`CategoryId`);

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
-- AUTO_INCREMENT for table `AgeRestrictedItem`
--
ALTER TABLE `AgeRestrictedItem`
  MODIFY `MemberId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT for table `Cashier`
--
ALTER TABLE `Cashier`
  MODIFY `employeeID` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=745873;
--
-- AUTO_INCREMENT for table `Categories`
--
ALTER TABLE `Categories`
  MODIFY `CtaegoryId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `Member`
--
ALTER TABLE `Member`
  MODIFY `MemberId` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `AgeRestrictedItem`
--
ALTER TABLE `AgeRestrictedItem`
  ADD CONSTRAINT `AgeRestrictedItem_ibfk_1` FOREIGN KEY (`MemberId`) REFERENCES `Member` (`MemberId`) ON UPDATE CASCADE;

--
-- Constraints for table `General Item`
--
ALTER TABLE `General Item`
  ADD CONSTRAINT `General Item_ibfk_1` FOREIGN KEY (`CategoryId`) REFERENCES `Categories` (`CtaegoryId`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2024 at 07:00 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hrms`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `A_Id` int(255) NOT NULL,
  `F_Name` varchar(255) NOT NULL,
  `L_name` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Attendance` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`A_Id`, `F_Name`, `L_name`, `Date`, `Attendance`) VALUES
(1, 'Roy', 'Souz', '2024-10-15', 'P'),
(2, 'Royal', 'Rodrigues', '2024-10-15', 'P'),
(3, 'Royal', 'Rodrigues', '2024-10-16', 'P');

-- --------------------------------------------------------

--
-- Table structure for table `employees_details`
--

CREATE TABLE `employees_details` (
  `E_Id` int(255) NOT NULL,
  `F_Name` varchar(255) NOT NULL,
  `M_Name` varchar(255) NOT NULL,
  `L_Name` varchar(255) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email_Address` varchar(255) NOT NULL,
  `Contact_no` int(255) NOT NULL,
  `Joining_date` date NOT NULL,
  `Designation` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Salary` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees_details`
--

INSERT INTO `employees_details` (`E_Id`, `F_Name`, `M_Name`, `L_Name`, `DOB`, `Address`, `Email_Address`, `Contact_no`, `Joining_date`, `Designation`, `Department`, `Salary`) VALUES
(1, 'Roy', 'Joy', 'Souz', '2002-09-06', 'Andheri', 'weare@123', 2147483647, '2024-09-09', 'Accountant', 'Finance', 20000),
(2, 'Royal', 'Albert', 'Rodrigues', '2003-08-31', 'Jogeshwari', 'royal@123', 2147483647, '2024-10-09', 'Data Analyst', 'IT', 25000);

-- --------------------------------------------------------

--
-- Table structure for table `leave`
--

CREATE TABLE `leave` (
  `L_Id` int(255) NOT NULL,
  `F_Name` varchar(255) NOT NULL,
  `L_Name` varchar(255) NOT NULL,
  `Reason` varchar(255) NOT NULL,
  `From_date` date NOT NULL,
  `To_date` date NOT NULL,
  `Days` int(255) NOT NULL,
  `Status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `leave`
--

INSERT INTO `leave` (`L_Id`, `F_Name`, `L_Name`, `Reason`, `From_date`, `To_date`, `Days`, `Status`) VALUES
(1, 'Roy', 'Souz', 'Family Function', '2024-10-15', '2024-10-20', 6, 'Approved'),
(2, 'Royal', 'Rodrigues', 'Reason for a leave is I am be Attending mu cousin wedding.', '2024-12-26', '2024-12-29', 4, 'Reject');

-- --------------------------------------------------------

--
-- Table structure for table `salary_record`
--

CREATE TABLE `salary_record` (
  `Reciept_Id` int(255) NOT NULL,
  `F_Name` varchar(255) NOT NULL,
  `L_Name` varchar(255) NOT NULL,
  `Payment_date` date NOT NULL,
  `Amount` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `salary_record`
--

INSERT INTO `salary_record` (`Reciept_Id`, `F_Name`, `L_Name`, `Payment_date`, `Amount`) VALUES
(1, 'Roy', 'Souz', '2024-10-01', 20000),
(2, 'Roe', 'Fernando', '2024-10-01', 20000),
(3, 'Royal', 'Rodrigues', '2024-10-30', 25000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`A_Id`);

--
-- Indexes for table `employees_details`
--
ALTER TABLE `employees_details`
  ADD PRIMARY KEY (`E_Id`);

--
-- Indexes for table `leave`
--
ALTER TABLE `leave`
  ADD PRIMARY KEY (`L_Id`);

--
-- Indexes for table `salary_record`
--
ALTER TABLE `salary_record`
  ADD PRIMARY KEY (`Reciept_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `A_Id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `employees_details`
--
ALTER TABLE `employees_details`
  MODIFY `E_Id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `leave`
--
ALTER TABLE `leave`
  MODIFY `L_Id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `salary_record`
--
ALTER TABLE `salary_record`
  MODIFY `Reciept_Id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

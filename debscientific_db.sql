-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 13, 2019 at 10:18 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `debscientific_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add admin user', 7, 'add_adminuser'),
(26, 'Can change admin user', 7, 'change_adminuser'),
(27, 'Can delete admin user', 7, 'delete_adminuser'),
(28, 'Can view admin user', 7, 'view_adminuser'),
(29, 'Can add admin email', 8, 'add_adminemail'),
(30, 'Can change admin email', 8, 'change_adminemail'),
(31, 'Can delete admin email', 8, 'delete_adminemail'),
(32, 'Can view admin email', 8, 'view_adminemail'),
(33, 'Can add slider', 9, 'add_slider'),
(34, 'Can change slider', 9, 'change_slider'),
(35, 'Can delete slider', 9, 'delete_slider'),
(36, 'Can view slider', 9, 'view_slider'),
(37, 'Can add about', 10, 'add_about'),
(38, 'Can change about', 10, 'change_about'),
(39, 'Can delete about', 10, 'delete_about'),
(40, 'Can view about', 10, 'view_about'),
(41, 'Can add gallery', 11, 'add_gallery'),
(42, 'Can change gallery', 11, 'change_gallery'),
(43, 'Can delete gallery', 11, 'delete_gallery'),
(44, 'Can view gallery', 11, 'view_gallery'),
(45, 'Can add contact us', 12, 'add_contactus'),
(46, 'Can change contact us', 12, 'change_contactus'),
(47, 'Can delete contact us', 12, 'delete_contactus'),
(48, 'Can view contact us', 12, 'view_contactus'),
(49, 'Can add valuable customer', 13, 'add_valuablecustomer'),
(50, 'Can change valuable customer', 13, 'change_valuablecustomer'),
(51, 'Can delete valuable customer', 13, 'delete_valuablecustomer'),
(52, 'Can view valuable customer', 13, 'view_valuablecustomer'),
(53, 'Can add category', 14, 'add_category'),
(54, 'Can change category', 14, 'change_category'),
(55, 'Can delete category', 14, 'delete_category'),
(56, 'Can view category', 14, 'view_category'),
(57, 'Can add video', 15, 'add_video'),
(58, 'Can change video', 15, 'change_video'),
(59, 'Can delete video', 15, 'delete_video'),
(60, 'Can view video', 15, 'view_video'),
(61, 'Can add faq', 16, 'add_faq'),
(62, 'Can change faq', 16, 'change_faq'),
(63, 'Can delete faq', 16, 'delete_faq'),
(64, 'Can view faq', 16, 'view_faq'),
(65, 'Can add brand', 17, 'add_brand'),
(66, 'Can change brand', 17, 'change_brand'),
(67, 'Can delete brand', 17, 'delete_brand'),
(68, 'Can view brand', 17, 'view_brand'),
(69, 'Can add policy', 18, 'add_policy'),
(70, 'Can change policy', 18, 'change_policy'),
(71, 'Can delete policy', 18, 'delete_policy'),
(72, 'Can view policy', 18, 'view_policy'),
(73, 'Can add product', 19, 'add_product'),
(74, 'Can change product', 19, 'change_product'),
(75, 'Can delete product', 19, 'delete_product'),
(76, 'Can view product', 19, 'view_product'),
(77, 'Can add product_image', 20, 'add_product_image'),
(78, 'Can change product_image', 20, 'change_product_image'),
(79, 'Can delete product_image', 20, 'delete_product_image'),
(80, 'Can view product_image', 20, 'view_product_image'),
(81, 'Can add product_download_image', 21, 'add_product_download_image'),
(82, 'Can change product_download_image', 21, 'change_product_download_image'),
(83, 'Can delete product_download_image', 21, 'delete_product_download_image'),
(84, 'Can view product_download_image', 21, 'view_product_download_image'),
(85, 'Can add product_image_resize', 22, 'add_product_image_resize'),
(86, 'Can change product_image_resize', 22, 'change_product_image_resize'),
(87, 'Can delete product_image_resize', 22, 'delete_product_image_resize'),
(88, 'Can view product_image_resize', 22, 'view_product_image_resize'),
(89, 'Can add user_cart_item', 23, 'add_user_cart_item'),
(90, 'Can change user_cart_item', 23, 'change_user_cart_item'),
(91, 'Can delete user_cart_item', 23, 'delete_user_cart_item'),
(92, 'Can view user_cart_item', 23, 'view_user_cart_item'),
(93, 'Can add banner', 24, 'add_banner'),
(94, 'Can change banner', 24, 'change_banner'),
(95, 'Can delete banner', 24, 'delete_banner'),
(96, 'Can view banner', 24, 'view_banner'),
(97, 'Can add user_wish_list', 25, 'add_user_wish_list'),
(98, 'Can change user_wish_list', 25, 'change_user_wish_list'),
(99, 'Can delete user_wish_list', 25, 'delete_user_wish_list'),
(100, 'Can view user_wish_list', 25, 'view_user_wish_list'),
(101, 'Can add countries', 26, 'add_countries'),
(102, 'Can change countries', 26, 'change_countries'),
(103, 'Can delete countries', 26, 'delete_countries'),
(104, 'Can view countries', 26, 'view_countries'),
(105, 'Can add billing_address', 27, 'add_billing_address'),
(106, 'Can change billing_address', 27, 'change_billing_address'),
(107, 'Can delete billing_address', 27, 'delete_billing_address'),
(108, 'Can view billing_address', 27, 'view_billing_address'),
(109, 'Can add order_address', 28, 'add_order_address'),
(110, 'Can change order_address', 28, 'change_order_address'),
(111, 'Can delete order_address', 28, 'delete_order_address'),
(112, 'Can view order_address', 28, 'view_order_address'),
(113, 'Can add user_address', 29, 'add_user_address'),
(114, 'Can change user_address', 29, 'change_user_address'),
(115, 'Can delete user_address', 29, 'delete_user_address'),
(116, 'Can view user_address', 29, 'view_user_address'),
(117, 'Can add enquiry', 30, 'add_enquiry'),
(118, 'Can change enquiry', 30, 'change_enquiry'),
(119, 'Can delete enquiry', 30, 'delete_enquiry'),
(120, 'Can view enquiry', 30, 'view_enquiry'),
(121, 'Can add order', 31, 'add_order'),
(122, 'Can change order', 31, 'change_order'),
(123, 'Can delete order', 31, 'delete_order'),
(124, 'Can view order', 31, 'view_order'),
(125, 'Can add order_details', 32, 'add_order_details'),
(126, 'Can change order_details', 32, 'change_order_details'),
(127, 'Can delete order_details', 32, 'delete_order_details'),
(128, 'Can view order_details', 32, 'view_order_details'),
(129, 'Can add review', 33, 'add_review'),
(130, 'Can change review', 33, 'change_review'),
(131, 'Can delete review', 33, 'delete_review'),
(132, 'Can view review', 33, 'view_review'),
(133, 'Can add product_enquiry', 34, 'add_product_enquiry'),
(134, 'Can change product_enquiry', 34, 'change_product_enquiry'),
(135, 'Can delete product_enquiry', 34, 'delete_product_enquiry'),
(136, 'Can view product_enquiry', 34, 'view_product_enquiry');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_about`
--

CREATE TABLE `debadmin_about` (
  `id` int(11) NOT NULL,
  `title` longtext DEFAULT NULL,
  `content` longtext DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_about`
--

INSERT INTO `debadmin_about` (`id`, `title`, `content`, `image`, `created_by`, `created_date`) VALUES
(1, '<p>About The <span class=\"text_color\">Business</span></p>', '<p>It has been over 25 years we are supplying equipment and instruments in various field of medical, research &amp; education. As an authorized distributor of some of the leading manufacturers, we can provide a comprehensive array of quality products.<br />Our goal is to supply superior quality products to the customer and provide complete support to them during the lifespan of our supplied product. We encourage every customers to provide us with their valuable feedback so that we can serve them better.</p>', 'about/ab1.apng', 1, '2019-10-29');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_adminemail`
--

CREATE TABLE `debadmin_adminemail` (
  `id` int(11) NOT NULL,
  `receive_email` varchar(255) NOT NULL,
  `from_email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_adminemail`
--

INSERT INTO `debadmin_adminemail` (`id`, `receive_email`, `from_email`) VALUES
(1, 'receive@gmail.com', 'from111@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_adminuser`
--

CREATE TABLE `debadmin_adminuser` (
  `id` int(11) NOT NULL,
  `user_type_id` int(11) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `login_password` varchar(255) NOT NULL,
  `login_email` varchar(255) NOT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_date` date DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `pin_code` varchar(255) DEFAULT NULL,
  `profile_image` varchar(100) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `landmark` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_adminuser`
--

INSERT INTO `debadmin_adminuser` (`id`, `user_type_id`, `full_name`, `login_password`, `login_email`, `phone_number`, `status`, `created_date`, `address`, `city`, `country`, `pin_code`, `profile_image`, `state`, `created_by`, `modified_by`, `modified_date`, `landmark`) VALUES
(1, 1, 'Deb Admin', 'admin@123', 'admin@gmail.com', '8597485925', '', '0000-00-00', '', '', '', '', '', '', 0, 0, '0000-00-00', NULL),
(2, 2, 'Suman Guria', '123456', 'suman@gmail.com', '8597485925', 'active', '2019-10-23', 'Kolkata, baguiati', 'kolkata', 'India', '784512', 'user_profile/images.jpeg', 'West Bengal', 0, 2, '2019-11-13', 'School'),
(4, 2, 'Jayanta', '123456', 'jayanta@gmail.com', '7845895641', 'active', '2019-10-23', 'airport kolkata', 'kolkata', 'India', '748574', 'user_profile/man.jpeg', 'wb', 0, 4, '2019-11-07', 'None'),
(5, 2, 'Jack Ryan', '123456', 'jack@gmail.com', '7845125623', 'active', '2019-11-05', 'Baguiati, Jora Mandir, Kolkata', 'Kolkata', 'West Bengal', '784589', 'user_profile/Koala.jpg', 'West Bengal', NULL, 5, '2019-11-05', 'Near School');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_banner`
--

CREATE TABLE `debadmin_banner` (
  `id` int(11) NOT NULL,
  `title_1` varchar(255) DEFAULT NULL,
  `title_2` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `banner_image` varchar(100) DEFAULT NULL,
  `banner_type` varchar(255) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `title_3` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_banner`
--

INSERT INTO `debadmin_banner` (`id`, `title_1`, `title_2`, `link`, `banner_image`, `banner_type`, `created_date`, `modified_date`, `title_3`) VALUES
(1, 'Car Audio', 'Super Natural Sound', '#', 'banner/p-1.jpg', 'first_row', '2019-11-01', '2019-11-13', NULL),
(2, 'All - New', 'Perfomance Parts', '#', 'banner/p-2.jpg', 'first_row', '2019-11-01', '2019-11-01', NULL),
(3, 'Automotive  Microscope', 'Consectetur Adipisicing ', '#', 'banner/back_1.jpg', 'second_row', '2019-11-01', '2019-11-01', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_billing_address`
--

CREATE TABLE `debadmin_billing_address` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile_number` varchar(255) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `landmark` varchar(255) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_billing_address`
--

INSERT INTO `debadmin_billing_address` (`id`, `user_id`, `order_id`, `full_name`, `email`, `mobile_number`, `pincode`, `country`, `state`, `city`, `landmark`, `address`, `created_date`, `created_by`) VALUES
(1, 2, NULL, 'Suman Guria', 'suman@gmail.com', '8597485925', 784512, 'West Bengal', 'West Bengal', 'kolkata', '', 'Kolkata, baguiati', '2019-11-04', 2),
(2, 2, NULL, 'Suman Guria', 'suman@gmail.com', '8597485925', 784512, 'West Bengal', 'West Bengal', 'kolkata', '', 'Kolkata, baguiati', '2019-11-05', 2),
(3, 2, 4, 'Suman Guria', 'suman@gmail.com', '8597485925', 784512, 'West Bengal', 'West Bengal', 'kolkata', '', 'Kolkata, baguiati', '2019-11-05', 2),
(4, 5, NULL, 'Jack Ryan', 'jack@gmail.com', '7845125623', 123456, 'India', 'West Bengal', 'Kolkata', 'school', 'kolkata', '2019-11-05', 5),
(5, 5, NULL, 'Jack Ryan', 'jack@gmail.com', '7845125623', 123456, 'India', 'West Bengal', 'Kolkata', 'school', 'kolkata', '2019-11-05', 5),
(6, 5, 5, 'Jack Ryan', 'jack@gmail.com', '7845125623', 784589, 'India', 'West Bengal', 'Kolkata', 'School', 'Kolkata, baguiati', '2019-11-05', 5),
(7, 4, NULL, 'Jayanta', 'jayanta@gmail.com', '7845895641', 33333, 'india', 'scscsdcd', 'cx s ds', 'sdsas', 'dsfsdfsdfs', '2019-11-05', 4),
(8, 5, 6, 'Jack Ryan', 'jack@gmail.com', '7845125623', 784589, 'West Bengal', 'West Bengal', 'Kolkata', 'Near School', 'Baguiati, Jora Mandir, Kolkata', '2019-11-05', 5),
(9, 5, 7, 'Jack Ryan', 'jack@gmail.com', '7845125623', 784589, 'West Bengal', 'West Bengal', 'Kolkata', 'Near School', 'Baguiati, Jora Mandir, Kolkata', '2019-11-05', 5),
(10, 2, 8, 'Suman Guria', 'suman@gmail.com', '8597485925', 784512, 'West Bengal', 'West Bengal', 'kolkata', 'School', 'Kolkata, baguiati', '2019-11-06', 2),
(11, 2, NULL, 'Suman Guria', 'suman@gmail.com', '8597485925', 784512, 'West Bengal', 'West Bengal', 'kolkata', 'School', 'Kolkata, baguiati', '2019-11-07', 2),
(12, 2, NULL, 'Suman Guria', 'suman@gmail.com', '8597485925', 784512, 'India', 'West Bengal', 'kolkata', 'School', 'Kolkata, baguiati', '2019-11-13', 2);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_brand`
--

CREATE TABLE `debadmin_brand` (
  `id` int(11) NOT NULL,
  `brand_name` varchar(255) DEFAULT NULL,
  `brand_image` varchar(100) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL,
  `status` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_brand`
--

INSERT INTO `debadmin_brand` (`id`, `brand_name`, `brand_image`, `created_date`, `created_by`, `modified_date`, `modified_by`, `status`) VALUES
(12, 'brand1', 'brand/b1.png', '2019-10-31', 1, '2019-11-13', 1, 'active'),
(13, 'brand2', 'brand/b5_M1HJYTl.png', '2019-10-31', 1, '2019-11-13', 1, 'active'),
(14, 'brand3', 'brand/b1_LfbCyO3.png', '2019-10-31', 1, NULL, NULL, 'active'),
(15, 'brand4', 'brand/b5.png', '2019-10-31', 1, '2019-11-13', 1, 'active'),
(16, 'brand5', 'brand/b1_1AFjHpF.png', '2019-10-31', 1, NULL, NULL, 'active');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_category`
--

CREATE TABLE `debadmin_category` (
  `id` int(11) NOT NULL,
  `parent_category` int(11) DEFAULT NULL,
  `category_name` varchar(255) DEFAULT NULL,
  `category_slug` varchar(255) DEFAULT NULL,
  `category_image` varchar(100) DEFAULT NULL,
  `category_status` varchar(8) NOT NULL,
  `description` longtext DEFAULT NULL,
  `category_commission_fixed` varchar(255) DEFAULT NULL,
  `category_commission_percent` varchar(255) DEFAULT NULL,
  `category_meta_title` varchar(255) DEFAULT NULL,
  `category_meta_description` longtext DEFAULT NULL,
  `category_meta_keyword` varchar(255) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_category`
--

INSERT INTO `debadmin_category` (`id`, `parent_category`, `category_name`, `category_slug`, `category_image`, `category_status`, `description`, `category_commission_fixed`, `category_commission_percent`, `category_meta_title`, `category_meta_description`, `category_meta_keyword`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(1, 0, 'Microscope', 'microscope', NULL, 'active', '<p>Microscope</p>', NULL, NULL, 'microscope', '<p>Microscope</p>', 'Microscope', '2019-10-25', 1, '2019-11-06', 1),
(3, 0, 'Photo Electric Instruments', 'photo-electric-instruments', '', 'active', '', NULL, NULL, 'photo-electric-instruments', '', '', '2019-10-25', 1, '2019-11-06', 1),
(6, 0, 'Centrifuges', 'Centrifuges', '', 'active', '', NULL, NULL, 'Centrifuges', '', '', '2019-10-25', 1, NULL, NULL),
(7, 0, 'Shakers and Stirrers', 'Shakers-and Stirrers', '', 'active', '', NULL, NULL, 'Shakers-and Stirrers', '', '', '2019-10-25', 1, NULL, NULL),
(8, 0, 'Histology Products', 'Histology-Products', '', 'active', '', NULL, NULL, 'Histology-Products', '', '', '2019-10-25', 1, NULL, NULL),
(9, 1, 'Labomed', 'labomed', '', 'active', '', NULL, NULL, 'labomed', '', '', '2019-10-25', 1, '2019-11-06', 1),
(10, 1, 'Micaps cameras for microscopy', 'micaps-cameras-for-microscopy', '', 'active', '', NULL, NULL, 'micaps-cameras-for-microscopy', '', '', '2019-10-25', 1, '2019-11-06', 1),
(11, 1, 'Labovision Student Microscopes', 'Labovision-Student Microscopes', '', 'active', '', NULL, NULL, 'Labovision-Student Microscopes', '', '', '2019-10-25', 1, NULL, NULL),
(12, 1, 'SMARTPHONE ADAPTER FOR MICROSCOPE', 'SMARTPHONE-ADAPTER FOR MICROSCOPE', '', 'active', '', NULL, NULL, 'SMARTPHONE-ADAPTER FOR MICROSCOPE', '', '', '2019-10-25', 1, NULL, NULL),
(13, 3, 'AIMIL', 'AIMIL', '', 'active', '', NULL, NULL, 'AIMIL', '', '', '2019-10-25', 1, NULL, NULL),
(14, 3, 'Flame Photometer', 'Flame-Photometer', '', 'active', '', NULL, NULL, 'Flame-Photometer', '', '', '2019-10-25', 1, NULL, NULL),
(15, 3, 'Spectrophotometers (Visible)', 'Spectrophotometers-(Visible)', '', 'active', '', NULL, NULL, 'Spectrophotometers-(Visible)', '', '', '2019-10-25', 1, '2019-10-25', 1),
(16, 3, 'Semi Automatic Bio Chemistry Analyzer', 'Semi-Automatic Bio Chemistry Analyzer', '', 'active', '', NULL, NULL, 'Semi-Automatic Bio Chemistry Analyzer', '', '', '2019-10-25', 1, NULL, NULL),
(17, 6, 'Medico Centrifuge', 'Medico-Centrifuge', '', 'active', '', NULL, NULL, 'Medico-Centrifuge', '', '', '2019-10-25', 1, NULL, NULL),
(18, 6, 'Laboratory & Micro Centrifuge (R-8C & RM-12C)', 'Laboratory-& Micro Centrifuge (R-8C & RM-12C)', '', 'active', '', NULL, NULL, 'Laboratory-& Micro Centrifuge (R-8C & RM-12C)', '', '', '2019-10-25', 1, NULL, NULL),
(19, 6, 'REMI NEYA 4 & 6', 'REMI-NEYA 4 & 6', '', 'active', '', NULL, NULL, 'REMI-NEYA 4 & 6', '', '', '2019-10-25', 1, NULL, NULL),
(20, 7, 'Geared Stirrers', 'Geared-Stirrers', '', 'active', '', NULL, NULL, 'Geared-Stirrers', '', '', '2019-10-25', 1, NULL, NULL),
(21, 7, 'Emulsifiers & Homogenizers', 'Emulsifiers-& Homogenizers', '', 'active', '', NULL, NULL, 'Emulsifiers-& Homogenizers', '', '', '2019-10-25', 1, NULL, NULL),
(22, 7, 'Direct Drive Stirrers', 'Direct-Drive Stirrers', '', 'active', '', NULL, NULL, 'Direct-Drive Stirrers', '', '', '2019-10-25', 1, NULL, NULL),
(23, 8, 'FNAC Handle', 'fnac-handle', '', 'active', '', NULL, NULL, 'fnac-handle', '', '', '2019-10-25', 1, '2019-11-06', 1),
(24, 8, 'Metal Base Molds', 'metal-base-molds', '', 'active', '', NULL, NULL, 'metal-base-molds', '', '', '2019-10-25', 1, '2019-11-06', 1),
(25, 8, 'Tissue Embedding Cassettes', 'tissue-embedding-cassettes', '', 'active', '', NULL, NULL, 'tissue-embedding-cassettes', '', '', '2019-10-25', 1, '2019-11-06', 1);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_contactus`
--

CREATE TABLE `debadmin_contactus` (
  `id` int(11) NOT NULL,
  `address` longtext DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `map_address` longtext DEFAULT NULL,
  `footer_content` longtext DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `contact_number` varchar(255) DEFAULT NULL,
  `land_line_number` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_contactus`
--

INSERT INTO `debadmin_contactus` (`id`, `address`, `mail`, `map_address`, `footer_content`, `created_date`, `created_by`, `contact_number`, `land_line_number`) VALUES
(1, '<p>DEB SCIENTIFIC 112 CHITTARANJAN AVENUE, KOLKATA -700073 (BESIDE ALL INDIA INSTITUTE OF HYGIENE PUBLIC HEALTH)</p>', 'debscientific@gmail.com', '<p><iframe style=\"border: 0;\" src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3684.0971537285086!2d88.35785901511328!3d22.57546938518131!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xcea422b902f519!2sDeb%20Scientific!5e0!3m2!1sen!2sin!4v1571919291771!5m2!1sen!2sin\" width=\"600\" height=\"450\" frameborder=\"0\" allowfullscreen=\"allowfullscreen\"></iframe></p>', '<p>We are a team of designers and developers that create high quality Magento, Prestashop, Opencart...</p>', '2019-11-01', 1, '9038723411', ' 033-22194265 / 033-22412456');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_enquiry`
--

CREATE TABLE `debadmin_enquiry` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `message` longtext DEFAULT NULL,
  `created_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_enquiry`
--

INSERT INTO `debadmin_enquiry` (`id`, `name`, `email`, `phone_number`, `message`, `created_date`) VALUES
(9, 'test Now', 'test@gmail.com', '9988998899', 'testing', '2019-11-12'),
(10, 'abhay', 'abhay@gmail.com', '9563887730', 'testing enquiry', '2019-11-12');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_faq`
--

CREATE TABLE `debadmin_faq` (
  `id` int(11) NOT NULL,
  `question` longtext DEFAULT NULL,
  `answer` longtext DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_faq`
--

INSERT INTO `debadmin_faq` (`id`, `question`, `answer`, `status`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(1, 'FAQ header text', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id erat sagittis, faucibus metus malesuada, eleifend turpis. Mauris semper augue id nisl aliquet, a porta lectus mattis. Nulla at tortor augue. In eget enim diam. Donec gravida tortor sem, ac fermentum nibh rutrum sit amet. Nulla convallis mauris vitae congue consequat. Donec interdum nunc purus, vitae vulputate arcu fringilla quis. Vivamus iaculis euismod dui.', 'active', '2019-10-25', 1, '2019-10-25', 1),
(2, '                           Lorem ipsum dolor sit amet?                            ', 'Donec mattis finibus elit ut tristique. Nullam tempus nunc eget arcu vulputate, eu porttitor tellus commodo. Aliquam erat volutpat. Aliquam consectetur lorem eu viverra lobortis. Morbi gravida, nisi id fringilla ultricies, elit lorem eleifend lorem', 'active', '2019-10-25', 1, NULL, NULL),
(3, '                          Aenean elit orci, efficitur quis nisl at, accumsan?                            ', 'Donec mattis finibus elit ut tristique. Nullam tempus nunc eget arcu vulputate, eu porttitor tellus commodo. Aliquam erat volutpat. Aliquam consectetur lorem eu viverra lobortis. Morbi gravida, nisi id fringilla ultricies, elit lorem eleifend lorem', 'active', '2019-10-25', 1, NULL, NULL),
(4, '                          Pellentesque habitant morbi tristique senectus et netus?                            ', 'Donec mattis finibus elit ut tristique. Nullam tempus nunc eget arcu vulputate, eu porttitor tellus commodo. Aliquam erat volutpat. Aliquam consectetur lorem eu viverra lobortis. Morbi gravida, nisi id fringilla ultricies, elit lorem eleifend lorem', 'active', '2019-10-25', 1, NULL, NULL),
(5, '                          Nam pellentesque aliquam metus?                            ', 'Donec mattis finibus elit ut tristique. Nullam tempus nunc eget arcu vulputate, eu porttitor tellus commodo. Aliquam erat volutpat. Aliquam consectetur lorem eu viverra lobortis. Morbi gravida, nisi id fringilla ultricies, elit lorem eleifend lorem', 'active', '2019-10-25', 1, NULL, NULL),
(6, '                         Aenean elit orci, efficitur quis nisl at?                            ', 'Donec mattis finibus elit ut tristique. Nullam tempus nunc eget arcu vulputate, eu porttitor tellus commodo. Aliquam erat volutpat. Aliquam consectetur lorem eu viverra lobortis. Morbi gravida, nisi id fringilla ultricies, elit lorem eleifend lorem', 'active', '2019-10-25', 1, NULL, NULL),
(8, '                          Aenean elit orci, efficitur quis nisl at, accumsan?                            ', 'Donec mattis finibus elit ut tristique. Nullam tempus nunc eget arcu vulputate, eu porttitor tellus commodo. Aliquam erat volutpat. Aliquam consectetur lorem eu viverra lobortis. Morbi gravida, nisi id fringilla ultricies, elit lorem eleifend lorem', 'active', '2019-10-25', 1, '2019-10-25', 1);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_gallery`
--

CREATE TABLE `debadmin_gallery` (
  `id` int(11) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_gallery`
--

INSERT INTO `debadmin_gallery` (`id`, `image`, `status`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(10, 'gallery/zoom1.jpg', 'active', '2019-10-24', 1, '2019-11-13', 1),
(11, 'gallery/zoom2.jpg', 'active', '2019-10-24', 1, '2019-11-13', 1),
(17, 'gallery/zoom3.jpg', 'active', '2019-11-13', 1, '2019-11-13', 1),
(18, 'gallery/zoom4.jpg', 'active', '2019-11-13', 1, '2019-11-13', 1);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_order`
--

CREATE TABLE `debadmin_order` (
  `id` int(11) NOT NULL,
  `order_unique_id` varchar(256) DEFAULT NULL,
  `order_track_id` varchar(256) DEFAULT NULL,
  `order_customer_id` int(11) DEFAULT NULL,
  `order_total_price` decimal(12,2) DEFAULT NULL,
  `order_discount` decimal(12,2) DEFAULT NULL,
  `order_sub_total_price` decimal(12,2) DEFAULT NULL,
  `order_shipping_charge` decimal(12,2) DEFAULT NULL,
  `order_status` varchar(20) NOT NULL,
  `payment_method` varchar(8) NOT NULL,
  `payment_status` varchar(8) NOT NULL,
  `order_created_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_order`
--

INSERT INTO `debadmin_order` (`id`, `order_unique_id`, `order_track_id`, `order_customer_id`, `order_total_price`, `order_discount`, `order_sub_total_price`, `order_shipping_charge`, `order_status`, `payment_method`, `payment_status`, `order_created_date`) VALUES
(3, 'DEB_2155363', '9BAFE2', 2, '1330.00', '82.00', '1412.00', '0.00', 'Delivered', 'cod', 'unpaid', '2019-11-05'),
(4, 'DEB-4869346501-4', '70734e577b', 2, '840.00', '60.00', '900.00', '0.00', 'Pending', 'cod', 'unpaid', '2019-11-05'),
(5, 'DEB-835288a801-5', '1871eb065d', 5, '420.00', '30.00', '450.00', '0.00', 'Pending', 'cod', 'unpaid', '2019-11-05'),
(6, 'DEB-718467e377-6', 'f7752d0e85', 5, '420.00', '30.00', '450.00', '0.00', 'Confirmed', 'cod', 'unpaid', '2019-11-05'),
(7, 'DEB-6502887bca-7', 'e3e461505f', 5, '420.00', '30.00', '450.00', '0.00', 'Pending', 'cod', 'unpaid', '2019-11-05'),
(8, 'DEB-699270c46d-8', 'f44067a158', 2, '245.00', '11.00', '256.00', '0.00', 'Pending', 'cod', 'unpaid', '2019-11-06');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_order_address`
--

CREATE TABLE `debadmin_order_address` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `deli_address_id` int(11) DEFAULT NULL,
  `bill_address_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_order_address`
--

INSERT INTO `debadmin_order_address` (`id`, `user_id`, `order_id`, `deli_address_id`, `bill_address_id`) VALUES
(1, 2, 3, 1, 2),
(2, 2, 4, 1, 3),
(3, 5, 5, 2, 6),
(4, 5, 6, 2, 8),
(5, 5, 7, 2, 9),
(6, 2, 8, 1, 10);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_order_details`
--

CREATE TABLE `debadmin_order_details` (
  `id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `order_product_id` int(11) DEFAULT NULL,
  `product_seller_id` int(11) DEFAULT NULL,
  `order_product_mrp` decimal(12,2) DEFAULT NULL,
  `order_product_discount` decimal(12,2) DEFAULT NULL,
  `order_product_price` decimal(12,2) DEFAULT NULL,
  `order_product_qty` int(11) DEFAULT NULL,
  `order_product_status` varchar(20) NOT NULL,
  `order_created_date` date DEFAULT NULL,
  `cancel_date` date DEFAULT NULL,
  `cancel_reason` longtext DEFAULT NULL,
  `deliver_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `return_reason` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_order_details`
--

INSERT INTO `debadmin_order_details` (`id`, `order_id`, `customer_id`, `order_product_id`, `product_seller_id`, `order_product_mrp`, `order_product_discount`, `order_product_price`, `order_product_qty`, `order_product_status`, `order_created_date`, `cancel_date`, `cancel_reason`, `deliver_date`, `return_date`, `return_reason`) VALUES
(1, 2, 2, 1, 1, '256.00', '4.30', '245.00', 2, 'Pending', '2019-11-04', NULL, NULL, NULL, NULL, NULL),
(2, 2, 2, 12, 1, '450.00', '6.67', '420.00', 2, 'Pending', '2019-11-04', NULL, NULL, NULL, NULL, NULL),
(3, 3, 2, 1, 1, '256.00', '4.30', '245.00', 2, 'Delivered', '2019-11-05', NULL, NULL, NULL, NULL, NULL),
(4, 3, 2, 12, 1, '450.00', '6.67', '420.00', 2, 'Delivered', '2019-11-05', NULL, NULL, NULL, NULL, NULL),
(5, 4, 2, 12, 1, '450.00', '6.67', '420.00', 2, 'Pending', '2019-11-05', NULL, NULL, NULL, NULL, NULL),
(6, 5, 5, 12, 1, '450.00', '6.67', '420.00', 1, 'Pending', '2019-11-05', NULL, NULL, NULL, NULL, NULL),
(7, 6, 5, 12, 1, '450.00', '6.67', '420.00', 1, 'Confirmed', '2019-11-05', NULL, NULL, NULL, NULL, NULL),
(8, 7, 5, 12, 1, '450.00', '6.67', '420.00', 1, 'Pending', '2019-11-05', NULL, NULL, NULL, NULL, NULL),
(9, 8, 2, 1, 1, '256.00', '4.30', '245.00', 1, 'Pending', '2019-11-06', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_policy`
--

CREATE TABLE `debadmin_policy` (
  `id` int(11) NOT NULL,
  `privacy_policy` longtext DEFAULT NULL,
  `return_policy` longtext DEFAULT NULL,
  `terms_of_use` longtext DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_policy`
--

INSERT INTO `debadmin_policy` (`id`, `privacy_policy`, `return_policy`, `terms_of_use`, `status`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(1, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>', '<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>\r\n<div class=\"right-icon\">&nbsp;</div>\r\n<ul>\r\n<li>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</li>\r\n</ul>', 'active', '2019-10-25', 1, '2019-10-25', 1);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_product`
--

CREATE TABLE `debadmin_product` (
  `id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `product_slug` varchar(255) DEFAULT NULL,
  `product_desc` longtext DEFAULT NULL,
  `compositions` varchar(255) DEFAULT NULL,
  `styles` varchar(255) DEFAULT NULL,
  `properties` varchar(255) DEFAULT NULL,
  `available_qty` int(11) DEFAULT NULL,
  `mrp_price` decimal(12,2) DEFAULT NULL,
  `discount` decimal(12,2) DEFAULT NULL,
  `sell_price` decimal(12,2) DEFAULT NULL,
  `meta_title` varchar(255) DEFAULT NULL,
  `meta_keyword` varchar(255) DEFAULT NULL,
  `meta_description` longtext DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `product_status` varchar(8) NOT NULL,
  `shipping_dimension_class` varchar(255) DEFAULT NULL,
  `shipping_product_height` double DEFAULT NULL,
  `shipping_product_length` double DEFAULT NULL,
  `shipping_product_width` double DEFAULT NULL,
  `avg_rating` int(11) DEFAULT NULL,
  `remaining_rating` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_product`
--

INSERT INTO `debadmin_product` (`id`, `category_id`, `brand_id`, `product_name`, `product_slug`, `product_desc`, `compositions`, `styles`, `properties`, `available_qty`, `mrp_price`, `discount`, `sell_price`, `meta_title`, `meta_keyword`, `meta_description`, `created_by`, `created_date`, `modified_by`, `modified_date`, `product_status`, `shipping_dimension_class`, `shipping_product_height`, `shipping_product_length`, `shipping_product_width`, `avg_rating`, `remaining_rating`) VALUES
(1, 10, 13, 'LABOMED VISION 2000 LED', 'labomed-vision-2000-led', '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam fringilla augue nec est tristique auctor. Donec non est at libero vulputate rutrum. Morbi ornare lectus quis justo gravida semper. Nulla tellus mi, vulputate adipiscing cursus eu, suscipit id nulla.</p>\r\n<p>Pellentesque aliquet, sem eget laoreet ultrices, ipsum metus feugiat sem, quis fermentum turpis eros eget velit. Donec ac tempus ante. Fusce ultricies massa massa. Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in accumsan elit odio quis mi. Cras neque metus, consequat et blandit et, luctus a nunc. Etiam gravida vehicula tellus, in imperdiet ligula euismod eget.</p>', 'Polyester', 'Girly', 'Short Dress', 17, '256.00', '4.30', '245.00', 'labomed-vision-2000-led', 'labomed-vision-2000-led', '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam fringilla augue nec est tristique auctor. Donec non est at libero vulputate rutrum. Morbi ornare lectus quis justo gravida semper. Nulla tellus mi, vulputate adipiscing cursus eu, suscipit id nulla.</p>\r\n<p>Pellentesque aliquet, sem eget laoreet ultrices, ipsum metus feugiat sem, quis fermentum turpis eros eget velit. Donec ac tempus ante. Fusce ultricies massa massa. Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in accumsan elit odio quis mi. Cras neque metus, consequat et blandit et, luctus a nunc. Etiam gravida vehicula tellus, in imperdiet ligula euismod eget.</p>', NULL, NULL, 1, '2019-11-13', 'active', 'Centemeter', 10, 15, 13, 4, 1),
(12, 9, 14, 'Micaps cameras for microscopy', 'micaps-cameras-for-microscopy', '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam fringilla augue nec est tristique auctor. Donec non est at libero vulputate rutrum. Morbi ornare lectus quis justo gravida semper. Nulla tellus mi, vulputate adipiscing cursus eu, suscipit id nulla.</p>\r\n<p>Pellentesque aliquet, sem eget laoreet ultrices, ipsum metus feugiat sem, quis fermentum turpis eros eget velit. Donec ac tempus ante. Fusce ultricies massa massa. Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in accumsan elit odio quis mi. Cras neque metus, consequat et blandit et, luctus a nunc. Etiam gravida vehicula tellus, in imperdiet ligula euismod eget.</p>', 'Polyester', 'Girly', 'Short Dress', 25, '450.00', '6.67', '420.00', 'micaps-cameras-for-microscopy', 'micaps-cameras-for-microscopy', '<p>micaps-cameras-for-microscopy</p>', 1, '2019-10-31', 1, '2019-11-06', 'active', 'Centemeter', 12, 10, 11, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_product_download_image`
--

CREATE TABLE `debadmin_product_download_image` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `download_image` varchar(100) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `modified_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_product_download_image`
--

INSERT INTO `debadmin_product_download_image` (`id`, `product_id`, `download_image`, `created_date`, `modified_date`) VALUES
(3, 1, 'product_download_image/pdf3.jpeg', '2019-10-29', NULL),
(4, 2, 'product_download_image/pdf1_xao2f9A.jpeg', '2019-10-29', NULL),
(5, 2, 'product_download_image/pdf2_iP56Q6U.jpeg', '2019-10-29', NULL),
(6, 2, 'product_download_image/pdf3_vod8XQ8.jpeg', '2019-10-29', NULL),
(7, 2, 'product_download_image/pdf4.jpeg', '2019-10-29', NULL),
(8, 3, 'product_download_image/pdf3_gUUZz3F.jpeg', '2019-10-29', NULL),
(9, 4, 'product_download_image/pdf2_gIf3MF7.jpeg', '2019-10-29', NULL),
(10, 5, 'product_download_image/pdf3_Nsnt8LS.jpeg', '2019-10-29', NULL),
(11, 11, 'product_download_image/pdf3_XWmV2qd.jpeg', '2019-10-29', NULL),
(13, 12, 'product_download_image/pdf2.jpg.jpeg', '2019-10-31', NULL),
(14, 12, 'product_download_image/pdf3.jpg.jpeg', '2019-10-31', NULL),
(15, 12, 'product_download_image/pdf1_j0qa667.jpg', '2019-10-31', '2019-11-13'),
(16, 12, 'product_download_image/pdf4.jpg', '2019-10-31', '2019-11-13'),
(18, 1, 'product_download_image/cart2.png', '2019-10-31', NULL),
(19, 1, 'product_download_image/pdf1.jpg', '2019-11-05', NULL),
(20, 1, 'product_download_image/pdf2.jpg', '2019-11-05', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_product_enquiry`
--

CREATE TABLE `debadmin_product_enquiry` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `web_address` varchar(255) DEFAULT NULL,
  `message` longtext DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_product_enquiry`
--

INSERT INTO `debadmin_product_enquiry` (`id`, `product_id`, `full_name`, `email`, `phone_number`, `web_address`, `message`, `date`) VALUES
(1, 12, 'Ramen', 'pythondeveloper.exprolab@gmail.com', '3333444455', 'google.com', 'testing', '2019-11-07'),
(12, 12, 'Ramen', 'pythondeveloper.exprolab@gmail.com', '9563887730', 'google.com', 'sss', '2019-11-08'),
(19, 12, 'Adani', 'pythondeveloper.exprolab@gmail.com', '9563887730', 'google.com', 'terrt', '2019-11-08'),
(21, 12, 'nancy', 'amin@GMAIL.COM', '3333444455', 'yellowbox.in', 'derere', '2019-11-08');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_product_image`
--

CREATE TABLE `debadmin_product_image` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `product_details` varchar(100) DEFAULT NULL,
  `product_list` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_product_image`
--

INSERT INTO `debadmin_product_image` (`id`, `product_id`, `created_date`, `modified_date`, `product_details`, `product_list`) VALUES
(50, 1, '2019-10-31', '2019-11-05', 'product_details/zoom1.jpg', 'product_list/zoom1.jpg'),
(53, 12, '2019-10-31', NULL, 'product_details/zoom4.jpg', 'product_list/zoom4.jpg'),
(55, 12, '2019-11-05', NULL, 'product_details/zoom1_2iOzBmP.jpg', 'product_list/zoom1_nRJwRVV.jpg'),
(56, 12, '2019-11-05', '2019-11-13', 'product_details/zoom3_HvMIF9a.jpg', 'product_list/zoom3.jpg'),
(57, 12, '2019-11-05', '2019-11-13', 'product_details/zoom2_IBid3lV.jpg', 'product_list/zoom2_DID6zb5.jpg'),
(58, 1, '2019-11-05', NULL, 'product_details/zoom2_Wd0cGcv.jpg', 'product_list/zoom2_C1V3jew.jpg'),
(59, 1, '2019-11-05', '2019-11-13', 'product_details/zoom2_94DUvLy.jpg', 'product_list/zoom2.jpg'),
(60, 1, '2019-11-05', NULL, 'product_details/zoom4_JRjmoWh.jpg', 'product_list/zoom4_j7xmHCo.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_review`
--

CREATE TABLE `debadmin_review` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `message` longtext DEFAULT NULL,
  `date` date DEFAULT NULL,
  `remaining_rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_review`
--

INSERT INTO `debadmin_review` (`id`, `user_id`, `product_id`, `rating`, `message`, `date`, `remaining_rating`) VALUES
(6, 2, 12, 3, 'Test product', '2019-11-07', 2),
(7, 2, 12, 2, 'test2', '2019-11-07', 3),
(9, 2, 1, 3, 'test', '2019-11-07', 2),
(12, 2, 1, 4, 'testy', '2019-11-07', 1),
(13, 4, 1, 5, 'this is good product', '2019-11-08', 0),
(14, 2, 1, 5, 'hello', '2019-11-12', 0);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_slider`
--

CREATE TABLE `debadmin_slider` (
  `id` int(11) NOT NULL,
  `title_1` varchar(255) DEFAULT NULL,
  `title_2` varchar(255) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_slider`
--

INSERT INTO `debadmin_slider` (`id`, `title_1`, `title_2`, `image`, `link`, `status`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(1, 'Special  Offer', 'Organisation for Health Care Solution', 'slider/banner-4_FHOe5IX.jpg', 'test.com', 'active', '2019-10-23', 1, '2019-11-13', 1),
(2, 'Hight Quality', 'Organisation for Health Care Solution', 'slider/banner-1.jpg', 'test.in', 'active', '2019-10-23', 1, '2019-10-31', 1),
(3, 'HP Racer Skutex', 'Organisation for Health Care Solution', 'slider/banner-3.jpg', 'test.com', 'active', '2019-10-23', 1, '2019-10-31', 1),
(4, 'HP Racer Skutex', 'Feel The Greatest Oil Power With Best One Oil', 'slider/banner-2.jpg', 'test.com', 'active', '2019-10-23', 1, '2019-11-13', 1),
(5, 'HP Racer Skutex', 'Feel The Greatest Oil Power With Best One Oil', 'slider/banner-5.jpg', 'test.com', 'active', '2019-10-23', 1, '2019-10-31', 1);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_user_address`
--

CREATE TABLE `debadmin_user_address` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile_number` varchar(255) DEFAULT NULL,
  `alt_mobile_number` varchar(255) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `landmark` varchar(255) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `address_type` varchar(8) NOT NULL,
  `is_default` varchar(8) NOT NULL,
  `post_office` varchar(255) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_user_address`
--

INSERT INTO `debadmin_user_address` (`id`, `user_id`, `full_name`, `email`, `mobile_number`, `alt_mobile_number`, `pincode`, `country`, `state`, `city`, `landmark`, `address`, `address_type`, `is_default`, `post_office`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(1, 2, 'Suman Guria', 'suman@gmail.com', '8597485925', 'None', 784512, 'India', 'West Bengal', 'kolkata', 'School', 'Kolkata, baguiati, Kali Mandir', 'office', 'no', 'None', '2019-11-04', 2, '2019-11-07', 2),
(2, 5, 'Jacky', 'jack@gmail.com', '7845125623', NULL, 784589, 'West Bengal', 'West Bengal', 'Kolkata', 'Near School', 'Baguiati, Jora Mandir, Kolkata', 'home', 'yes', NULL, '2019-11-05', 5, '2019-11-05', 5),
(4, 4, 'nancy', 'abhay@gmail.com', '9563887730', '', 748574, 'India', 'wb', 'kol', 'wb', 'swastik house delhi 3', 'office', 'no', 'nimta', '2019-11-06', 4, '2019-11-13', 4),
(6, 2, 'Suman Guria', 'sumanguria.exprolab@gmail.com', '7894561230', '', 784589, 'India', 'West Bengal', 'Kolkata', 'hospital', 'Kolkata, baguiati', 'home', 'yes', 'Chinarpark', '2019-11-07', 2, '2019-11-13', 2),
(7, 4, 'Ramen', 'aaa@gmail.com', '9563887730', '', 748574, 'India', 'wb', 'kol', 'tea shop', '5/2 loknath pally', 'home', 'yes', 'lalgarh', '2019-11-07', 4, '2019-11-13', 4),
(9, 4, 'Arun', 'arun@yahoo.in', '8877445533', '', 748574, 'India', 'wb', 'kolkata', '', 'howrah wb 45', 'home', 'no', '', '2019-11-07', 4, '2019-11-13', 4),
(10, 4, 'Adani', 'adani@yahoo.in', '9852451230', '', 748574, 'India', 'wb', 'kolkata', 'wb', 'chiner park airpot kolkata', 'office', 'no', '', '2019-11-07', 4, '2019-11-13', 4);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_user_cart_item`
--

CREATE TABLE `debadmin_user_cart_item` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `cart_item_id` int(11) DEFAULT NULL,
  `cart_mrp_price` decimal(12,2) DEFAULT NULL,
  `cart_discount` decimal(12,2) DEFAULT NULL,
  `cart_sell_price` decimal(12,2) DEFAULT NULL,
  `cart_item_qty` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_user_cart_item`
--

INSERT INTO `debadmin_user_cart_item` (`id`, `user_id`, `cart_item_id`, `cart_mrp_price`, `cart_discount`, `cart_sell_price`, `cart_item_qty`) VALUES
(20, 5, 1, '256.00', '4.30', '245.00', 1),
(34, 4, 1, '256.00', '4.30', '245.00', 1),
(42, 2, 1, '256.00', '4.30', '245.00', 4);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_user_wish_list`
--

CREATE TABLE `debadmin_user_wish_list` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_user_wish_list`
--

INSERT INTO `debadmin_user_wish_list` (`id`, `user_id`, `product_id`) VALUES
(3, 5, 1),
(9, 5, 12);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_valuablecustomer`
--

CREATE TABLE `debadmin_valuablecustomer` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `customer_image` varchar(100) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_valuablecustomer`
--

INSERT INTO `debadmin_valuablecustomer` (`id`, `customer_name`, `customer_image`, `status`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(3, 'Pitam Mukherjee', 'valuable_customer/man.jpeg', 'active', '2019-10-24', 1, '2019-10-25', 1),
(6, 'Pitam Mukherjee', 'valuable_customer/cus_2_ATBWlpK.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(7, 'Sayan Banerjee', 'valuable_customer/cus_3.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(8, 'Binay Das', 'valuable_customer/cus_2.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(9, 'Ramen Pal', 'valuable_customer/cus_MSiTklW.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(10, 'Ratan Pal', 'valuable_customer/cus_jwCB1ve.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(11, 'Rahul Pal', 'valuable_customer/cus_E0QUJT8.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(12, 'Kamal Kundu', 'valuable_customer/cus_3_mhm3h1R.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(13, 'Kamal Hasan', 'valuable_customer/cus_epQKwBR.jpeg', 'active', '2019-10-25', 1, '2019-10-25', 1),
(14, 'Loknath Nath', 'valuable_customer/cus_CesvR1P.jpeg', 'active', '2019-10-25', 1, '2019-10-29', 1),
(15, 'Ritesh Dani', 'valuable_customer/cus_2_CcjmHC6.jpeg', 'active', '2019-10-25', 1, '2019-10-29', 1),
(16, 'Tishav Sori', 'valuable_customer/cus_2_awwD4Oq.jpeg', 'active', '2019-10-25', 1, '2019-10-29', 1);

-- --------------------------------------------------------

--
-- Table structure for table `debadmin_video`
--

CREATE TABLE `debadmin_video` (
  `id` int(11) NOT NULL,
  `link` varchar(255) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  `modified_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `debadmin_video`
--

INSERT INTO `debadmin_video` (`id`, `link`, `status`, `created_date`, `created_by`, `modified_date`, `modified_by`) VALUES
(1, 'https://youtube.com/embed/lo2aC_m2vyo', 'active', '2019-10-25', 1, '2019-11-01', 1),
(3, 'https://youtube.com/embed/SUo2fHZaZCU', 'active', '2019-10-25', 1, '2019-11-01', 1),
(4, 'https://youtube.com/embed/SUo2fHZaZCU', 'active', '2019-10-25', 1, '2019-10-31', 1),
(5, 'https://youtube.com/embed/lo2aC_m2vyo', 'active', '2019-10-25', 1, '2019-10-31', 1),
(6, 'https://youtube.com/embed/nDGfHaswVZg', 'active', '2019-10-25', 1, '2019-10-31', 1),
(7, 'https://youtube.com/embed/SUo2fHZaZCU', 'active', '2019-10-25', 1, '2019-10-31', 1),
(8, 'https://youtube.com/embed/SUo2fHZaZCU', 'active', '2019-10-25', 1, '2019-10-31', 1),
(9, 'https://youtube.com/embed/nDGfHaswVZg', 'active', '2019-10-25', 1, '2019-10-31', 1),
(10, 'https://youtube.com/embed/lo2aC_m2vyo', 'active', '2019-10-25', 1, '2019-10-31', 1),
(11, 'https://youtube.com/embed/SUo2fHZaZCU', 'active', '2019-10-25', 1, '2019-10-31', 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'debadmin', 'about'),
(8, 'debadmin', 'adminemail'),
(7, 'debadmin', 'adminuser'),
(24, 'debadmin', 'banner'),
(27, 'debadmin', 'billing_address'),
(17, 'debadmin', 'brand'),
(14, 'debadmin', 'category'),
(12, 'debadmin', 'contactus'),
(26, 'debadmin', 'countries'),
(30, 'debadmin', 'enquiry'),
(16, 'debadmin', 'faq'),
(11, 'debadmin', 'gallery'),
(31, 'debadmin', 'order'),
(28, 'debadmin', 'order_address'),
(32, 'debadmin', 'order_details'),
(18, 'debadmin', 'policy'),
(19, 'debadmin', 'product'),
(21, 'debadmin', 'product_download_image'),
(34, 'debadmin', 'product_enquiry'),
(20, 'debadmin', 'product_image'),
(22, 'debadmin', 'product_image_resize'),
(33, 'debadmin', 'review'),
(9, 'debadmin', 'slider'),
(29, 'debadmin', 'user_address'),
(23, 'debadmin', 'user_cart_item'),
(25, 'debadmin', 'user_wish_list'),
(13, 'debadmin', 'valuablecustomer'),
(15, 'debadmin', 'video'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-10-22 06:18:36.943359'),
(2, 'auth', '0001_initial', '2019-10-22 06:18:39.253906'),
(3, 'admin', '0001_initial', '2019-10-22 06:18:50.456054'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-10-22 06:18:53.363281'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-10-22 06:18:53.594726'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-10-22 06:18:54.454101'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-10-22 06:18:55.253906'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-10-22 06:18:55.560546'),
(9, 'auth', '0004_alter_user_username_opts', '2019-10-22 06:18:55.638671'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-10-22 06:18:56.256835'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-10-22 06:18:56.284179'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-10-22 06:18:56.327148'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-10-22 06:18:56.435546'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-10-22 06:18:56.581054'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-10-22 06:18:56.723632'),
(16, 'auth', '0011_update_proxy_permissions', '2019-10-22 06:18:56.760742'),
(17, 'sessions', '0001_initial', '2019-10-22 06:18:57.483398'),
(18, 'debadmin', '0001_initial', '2019-10-22 06:29:41.462890'),
(19, 'debadmin', '0002_adminemail', '2019-10-22 10:59:52.902343'),
(20, 'debadmin', '0003_auto_20191023_1028', '2019-10-23 04:58:24.802734'),
(21, 'debadmin', '0004_auto_20191023_1117', '2019-10-23 05:47:53.604492'),
(22, 'debadmin', '0005_auto_20191023_1122', '2019-10-23 06:06:13.901367'),
(23, 'debadmin', '0006_auto_20191023_1129', '2019-10-23 06:06:16.954101'),
(24, 'debadmin', '0007_adminuser_created_date', '2019-10-23 06:06:17.212890'),
(25, 'debadmin', '0008_auto_20191023_1135', '2019-10-23 06:06:17.552734'),
(26, 'debadmin', '0009_auto_20191023_1140', '2019-10-23 06:10:53.433593'),
(27, 'debadmin', '0010_auto_20191023_1153', '2019-10-23 06:23:44.421875'),
(28, 'debadmin', '0011_auto_20191023_1212', '2019-10-23 06:42:43.828125'),
(29, 'debadmin', '0012_auto_20191023_1213', '2019-10-23 06:43:59.642578'),
(30, 'debadmin', '0013_auto_20191023_1907', '2019-10-23 13:38:11.226562'),
(31, 'debadmin', '0014_auto_20191024_1047', '2019-10-24 05:18:07.024414'),
(32, 'debadmin', '0015_delete_about', '2019-10-24 05:20:17.117187'),
(33, 'debadmin', '0016_about', '2019-10-24 05:20:48.470703'),
(34, 'debadmin', '0017_auto_20191024_1058', '2019-10-24 05:29:16.336914'),
(35, 'debadmin', '0018_auto_20191024_1059', '2019-10-24 05:29:16.539062'),
(36, 'debadmin', '0019_gallery', '2019-10-24 05:57:32.029296'),
(37, 'debadmin', '0020_auto_20191024_1438', '2019-10-24 09:08:42.551757'),
(38, 'debadmin', '0021_contactus', '2019-10-24 09:53:15.614257'),
(39, 'debadmin', '0022_remove_contactus_map_address2', '2019-10-24 09:54:27.435546'),
(40, 'debadmin', '0023_auto_20191024_1613', '2019-10-24 10:43:37.179687'),
(41, 'debadmin', '0024_delete_contactus', '2019-10-24 11:12:31.209961'),
(42, 'debadmin', '0025_contactus', '2019-10-24 11:13:11.801757'),
(43, 'debadmin', '0026_valuablecustomer', '2019-10-24 12:34:35.947265'),
(44, 'debadmin', '0027_auto_20191024_1909', '2019-10-24 13:39:58.834961'),
(45, 'debadmin', '0028_category_video', '2019-10-25 06:33:13.737304'),
(46, 'debadmin', '0029_remove_category_sub_category', '2019-10-25 07:29:46.583007'),
(47, 'debadmin', '0030_auto_20191025_1306', '2019-10-25 07:36:14.050781'),
(48, 'debadmin', '0031_auto_20191025_1307', '2019-10-25 07:37:38.718750'),
(49, 'debadmin', '0032_auto_20191025_1311', '2019-10-25 07:42:03.273437'),
(50, 'debadmin', '0033_auto_20191025_1312', '2019-10-25 07:42:42.402343'),
(51, 'debadmin', '0034_auto_20191025_1314', '2019-10-25 07:44:24.965820'),
(52, 'debadmin', '0035_auto_20191025_1321', '2019-10-25 07:52:26.822265'),
(53, 'debadmin', '0036_auto_20191025_1524', '2019-10-25 09:54:36.958984'),
(54, 'debadmin', '0037_policy', '2019-10-25 10:38:03.901367'),
(55, 'debadmin', '0038_product_product_image', '2019-10-26 06:48:07.922851'),
(56, 'debadmin', '0039_auto_20191026_1338', '2019-10-26 08:08:38.347656'),
(57, 'debadmin', '0040_auto_20191029_1115', '2019-10-29 05:45:22.768421'),
(58, 'debadmin', '0041_auto_20191029_1116', '2019-10-29 05:46:31.845570'),
(59, 'debadmin', '0042_auto_20191029_1308', '2019-10-29 07:38:16.327992'),
(60, 'debadmin', '0043_auto_20191029_1700', '2019-10-29 11:30:43.585804'),
(61, 'debadmin', '0044_auto_20191030_1049', '2019-10-30 05:20:05.956054'),
(62, 'debadmin', '0045_auto_20191030_1052', '2019-10-30 05:22:48.718750'),
(63, 'debadmin', '0046_product_image_resize', '2019-10-30 05:40:23.463867'),
(64, 'debadmin', '0047_auto_20191030_1850', '2019-10-30 13:20:55.743164'),
(65, 'debadmin', '0048_auto_20191031_1041', '2019-10-31 05:11:46.739257'),
(66, 'debadmin', '0049_delete_product_image_resize', '2019-10-31 05:49:28.591796'),
(67, 'debadmin', '0050_auto_20191031_1538', '2019-10-31 10:08:32.918945'),
(68, 'debadmin', '0051_brand_status', '2019-10-31 10:18:44.660156'),
(69, 'debadmin', '0052_auto_20191031_1609', '2019-10-31 10:39:31.735351'),
(70, 'debadmin', '0053_auto_20191031_1618', '2019-10-31 10:48:54.838867'),
(71, 'debadmin', '0054_auto_20191031_1626', '2019-10-31 10:56:39.948242'),
(72, 'debadmin', '0055_banner', '2019-11-01 07:53:19.213867'),
(73, 'debadmin', '0056_banner_title_3', '2019-11-01 10:04:19.683593'),
(74, 'debadmin', '0057_user_wish_list', '2019-11-01 10:43:13.887695'),
(75, 'debadmin', '0058_countries', '2019-11-01 11:17:18.229492'),
(76, 'debadmin', '0059_delete_countries', '2019-11-01 11:20:49.934570'),
(77, 'debadmin', '0060_billing_address_order_address_user_address', '2019-11-01 13:20:22.852539'),
(78, 'debadmin', '0061_auto_20191104_1113', '2019-11-04 05:43:43.277343'),
(79, 'debadmin', '0062_enquiry_order_order_details', '2019-11-04 10:12:17.755859'),
(80, 'debadmin', '0063_adminuser_landmark', '2019-11-05 06:51:30.918945'),
(81, 'debadmin', '0064_product_avg_rating', '2019-11-06 09:28:30.875976'),
(82, 'debadmin', '0065_review', '2019-11-07 08:51:39.646484'),
(83, 'debadmin', '0066_review_user_name', '2019-11-07 09:04:42.920898'),
(84, 'debadmin', '0067_auto_20191107_1503', '2019-11-07 09:33:19.727539'),
(85, 'debadmin', '0068_review_remaining_rating', '2019-11-07 10:01:33.863281'),
(86, 'debadmin', '0069_remove_review_user_name', '2019-11-07 10:37:34.441406'),
(87, 'debadmin', '0070_auto_20191107_1631', '2019-11-07 11:01:24.056640'),
(88, 'debadmin', '0071_product_remaining_rating', '2019-11-07 11:12:27.752929'),
(89, 'debadmin', '0072_auto_20191107_1857', '2019-11-07 13:27:08.377929'),
(90, 'debadmin', '0073_auto_20191107_1907', '2019-11-07 13:37:44.099609'),
(91, 'debadmin', '0074_auto_20191107_1914', '2019-11-07 13:44:12.820312'),
(92, 'debadmin', '0075_auto_20191108_1225', '2019-11-08 06:55:23.690429'),
(93, 'debadmin', '0076_remove_user_cart_item_cart_session_id', '2019-11-08 13:04:48.655273');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2z13w0z41eo9trwtljm6yb6ivq9ywsj5', 'NGM2MWFmMmZmOTYxMWJmODA2ZmYyMjUyYjZmMWQyNjdlNzZkN2VjYTp7InVzZXJfc2Vzc2lvbl9pZCI6MiwiYWRtaW5fc2Vzc2lvbl9pZCI6MSwiYWRtaW5fc2Vzc2lvbl9uYW1lIjoiRGViIEFkbWluIn0=', '2019-11-20 10:53:06.713867'),
('371uwiqnxzdobs7luna6gjqamx644m8k', 'ODkwNzhkYjhhODY2YjU2YjNlMWVjYWFlYThjNDUyNWRlMGE2MmRhZjp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiJ9', '2019-11-07 07:44:28.867187'),
('80usk93ldpyw5p25o4j7htc32wtc638h', 'ODc2ZDYzODY2ZGVlZWIwMzA5NjY0M2ZlYTNlMGJjNTU0MDBjZWI2MDp7InVzZXJfc2Vzc2lvbl9pZCI6Mn0=', '2019-11-14 07:45:29.412109'),
('90ui1bd4jkfwdqo1dxpfynb4c1tx750f', 'MTg2NzkyNDY4N2QwNGQ0NDdmODZmZDNkZTRkMmQwODEzZWMwZTBlODp7ImRlYnNjaWVudGlmaWNfdXNlcl9pZCI6MiwiZGVic2NpZW50aWZpY191c2VyX3Nlc3Npb25faWQiOjIsInVzZXJfc2Vzc2lvbl9pZCI6MiwiYWRtaW5fc2Vzc2lvbl9pZCI6MSwiYWRtaW5fc2Vzc2lvbl9uYW1lIjoiRGViIEFkbWluIn0=', '2019-11-07 07:31:14.106445'),
('9awrax8tslnx7noj5mcikucdweedwnn7', 'ODkwNzhkYjhhODY2YjU2YjNlMWVjYWFlYThjNDUyNWRlMGE2MmRhZjp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiJ9', '2019-11-07 10:25:51.425781'),
('a0wwr65eszdz3lq48ntvl8331odh54ln', 'NWMyMzVhZjlkZDRhYWNkYzU2MmJhODkyNjU4M2QyMTVlOTZjOWJjMjp7fQ==', '2019-11-07 07:30:47.538085'),
('kai40tc3e0ud41yksd960a9iqi1lnhwn', 'NWQwZjkxYjZjMTY1NGVmODQ2YTc0NGExMjRiYmUxMTI3Mzg4ZDJlNjp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiIsInVzZXJfc2Vzc2lvbl9pZCI6Mn0=', '2019-11-14 08:38:53.252929'),
('lcljvrgdlw8zi9vrsrddlgnek978h61l', 'ZGEyNzUyN2Q5NWI2NTZlOTAwYTViNGEwNTQ0YmU0ZmExODJjZTkyZDp7InVzZXJfc2Vzc2lvbl9pZCI6MiwiYmlsbF9hZGRyZXNzX3Nlc3Npb25faWQiOjExLCJhZG1pbl9zZXNzaW9uX2lkIjoxLCJhZG1pbl9zZXNzaW9uX25hbWUiOiJEZWIgQWRtaW4ifQ==', '2019-11-21 12:19:41.247070'),
('mamelp0tpx9bmtzn5o8g7yk3efimk7v0', 'NWQwZjkxYjZjMTY1NGVmODQ2YTc0NGExMjRiYmUxMTI3Mzg4ZDJlNjp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiIsInVzZXJfc2Vzc2lvbl9pZCI6Mn0=', '2019-11-15 12:18:26.361328'),
('p3qp8rf0ahvuenvw0uu3p17q8qzz7hhg', 'OTMyZjY0MjcyNDAzOTQ5YmZlNWVkYjA0OWU1ZDcwOTg5NTM4NWM1NTp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiIsImJpbGxfYWRkcmVzc19zZXNzaW9uX2lkIjo3LCJ1c2VyX3Nlc3Npb25faWQiOjR9', '2019-11-21 13:58:25.755859'),
('tpus8w7vcuif92ep9206yn89st6ybivi', 'NDQ2NjExZDRjN2UxYWEyOTQyODYyNjQ3NTVlNmUxNmE0OWFmYmZhNDp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiIsImRlYl9jYXJ0X2l0ZW0iOnsiMSI6MX0sInVzZXJfc2Vzc2lvbl9pZCI6MiwiYmlsbF9hZGRyZXNzX3Nlc3Npb25faWQiOjEyfQ==', '2019-11-27 06:18:46.549804'),
('u6x51hw0hcjqi5u5pku39yf2ayc89htv', 'NWQwZjkxYjZjMTY1NGVmODQ2YTc0NGExMjRiYmUxMTI3Mzg4ZDJlNjp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiIsInVzZXJfc2Vzc2lvbl9pZCI6Mn0=', '2019-11-14 07:45:51.854492'),
('u9s2pqp0kzplksgk883us0tz1uo9hl8x', 'MzIwNzlkYmY4ZjQzNzllNDdlMTNlMTAzMDFmYjk0NTA2NDU1MTE4Mjp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiIsInVzZXJfc2Vzc2lvbl9pZCI6NX0=', '2019-11-19 11:09:13.697265'),
('up341d855xa2zi8rpk7npcs3vyp7a2o7', 'MjNmOWNkOGQ3NWNmMDEwMTk3YTAyOGIyMTQ2Y2U1Yzk5YWRjZTFiYTp7ImFkbWluX3Nlc3Npb25faWQiOjEsImFkbWluX3Nlc3Npb25fbmFtZSI6IkRlYiBBZG1pbiIsInVzZXJfc2Vzc2lvbl9pZCI6MiwiYmlsbF9hZGRyZXNzX3Nlc3Npb25faWQiOjEsImRlbGlfYWRkcmVzc19zZXNzaW9uX2lkIjoxfQ==', '2019-11-18 05:53:22.027343');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `debadmin_about`
--
ALTER TABLE `debadmin_about`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_adminemail`
--
ALTER TABLE `debadmin_adminemail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_adminuser`
--
ALTER TABLE `debadmin_adminuser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_banner`
--
ALTER TABLE `debadmin_banner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_billing_address`
--
ALTER TABLE `debadmin_billing_address`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_brand`
--
ALTER TABLE `debadmin_brand`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_category`
--
ALTER TABLE `debadmin_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_contactus`
--
ALTER TABLE `debadmin_contactus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_enquiry`
--
ALTER TABLE `debadmin_enquiry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_faq`
--
ALTER TABLE `debadmin_faq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_gallery`
--
ALTER TABLE `debadmin_gallery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_order`
--
ALTER TABLE `debadmin_order`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_order_address`
--
ALTER TABLE `debadmin_order_address`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_order_details`
--
ALTER TABLE `debadmin_order_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_policy`
--
ALTER TABLE `debadmin_policy`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_product`
--
ALTER TABLE `debadmin_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_product_download_image`
--
ALTER TABLE `debadmin_product_download_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_product_enquiry`
--
ALTER TABLE `debadmin_product_enquiry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_product_image`
--
ALTER TABLE `debadmin_product_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_review`
--
ALTER TABLE `debadmin_review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_slider`
--
ALTER TABLE `debadmin_slider`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_user_address`
--
ALTER TABLE `debadmin_user_address`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_user_cart_item`
--
ALTER TABLE `debadmin_user_cart_item`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_user_wish_list`
--
ALTER TABLE `debadmin_user_wish_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_valuablecustomer`
--
ALTER TABLE `debadmin_valuablecustomer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debadmin_video`
--
ALTER TABLE `debadmin_video`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=137;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `debadmin_about`
--
ALTER TABLE `debadmin_about`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `debadmin_adminemail`
--
ALTER TABLE `debadmin_adminemail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `debadmin_adminuser`
--
ALTER TABLE `debadmin_adminuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `debadmin_banner`
--
ALTER TABLE `debadmin_banner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `debadmin_billing_address`
--
ALTER TABLE `debadmin_billing_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `debadmin_brand`
--
ALTER TABLE `debadmin_brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `debadmin_category`
--
ALTER TABLE `debadmin_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `debadmin_contactus`
--
ALTER TABLE `debadmin_contactus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `debadmin_enquiry`
--
ALTER TABLE `debadmin_enquiry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `debadmin_faq`
--
ALTER TABLE `debadmin_faq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `debadmin_gallery`
--
ALTER TABLE `debadmin_gallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `debadmin_order`
--
ALTER TABLE `debadmin_order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `debadmin_order_address`
--
ALTER TABLE `debadmin_order_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `debadmin_order_details`
--
ALTER TABLE `debadmin_order_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `debadmin_policy`
--
ALTER TABLE `debadmin_policy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `debadmin_product`
--
ALTER TABLE `debadmin_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `debadmin_product_download_image`
--
ALTER TABLE `debadmin_product_download_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `debadmin_product_enquiry`
--
ALTER TABLE `debadmin_product_enquiry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `debadmin_product_image`
--
ALTER TABLE `debadmin_product_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `debadmin_review`
--
ALTER TABLE `debadmin_review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `debadmin_slider`
--
ALTER TABLE `debadmin_slider`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `debadmin_user_address`
--
ALTER TABLE `debadmin_user_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `debadmin_user_cart_item`
--
ALTER TABLE `debadmin_user_cart_item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `debadmin_user_wish_list`
--
ALTER TABLE `debadmin_user_wish_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `debadmin_valuablecustomer`
--
ALTER TABLE `debadmin_valuablecustomer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `debadmin_video`
--
ALTER TABLE `debadmin_video`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

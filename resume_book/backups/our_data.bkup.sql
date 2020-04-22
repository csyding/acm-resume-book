-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: wftuqljwesiffol6.cbetxkdyhwsb.us-east-1.rds.amazonaws.com    Database: jpwp4titsovtkppo
-- ------------------------------------------------------
-- Server version	5.7.23-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED='';

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add student',1,'add_student'),(2,'Can change student',1,'change_student'),(3,'Can delete student',1,'delete_student'),(4,'Can view student',1,'view_student'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add user',5,'add_user'),(18,'Can change user',5,'change_user'),(19,'Can delete user',5,'delete_user'),(20,'Can view user',5,'view_user'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session'),(29,'Can add student group',8,'add_studentgroup'),(30,'Can change student group',8,'change_studentgroup'),(31,'Can delete student group',8,'delete_studentgroup'),(32,'Can view student group',8,'view_studentgroup'),(33,'Can add company',11,'add_company'),(34,'Can change company',11,'change_company'),(35,'Can delete company',11,'delete_company'),(36,'Can view company',11,'view_company'),(37,'Can add resume',10,'add_resume'),(38,'Can change resume',10,'change_resume'),(39,'Can delete resume',10,'delete_resume'),(40,'Can view resume',10,'view_resume'),(41,'Can add internship',12,'add_internship'),(42,'Can change internship',12,'change_internship'),(43,'Can delete internship',12,'delete_internship'),(44,'Can view internship',12,'view_internship'),(45,'Can add recruiter',9,'add_recruiter'),(46,'Can change recruiter',9,'change_recruiter'),(47,'Can delete recruiter',9,'delete_recruiter'),(48,'Can view recruiter',9,'view_recruiter');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$MqeZbIc60R0q$5BJrbd+rmvp3u51vHC5hEOoTgTZW+jaGvjmC2iHFjf0=','2020-04-22 10:48:12.053535',1,'degeneraskis','','','scottk3@illinois.edu',1,1,'2020-03-23 22:08:45.820851'),(2,'pbkdf2_sha256$150000$vbddaqudIVyP$Sajjizcp6stSLHM6/P3+5SMPZ8E77vvtU4hRjBwFdOA=','2020-04-10 06:42:15.300402',0,'testuser','','','',1,1,'2020-03-23 22:20:24.000000'),(3,'pbkdf2_sha256$150000$d5yEJKO7i64R$dFkcC8YjWhITTWr3IlLE5vvf4ULwjnOmYWen7o1nO1g=',NULL,0,'testuser2','','','',0,1,'2020-04-22 10:50:11.698503');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-03-23 22:20:24.978767','2','testuser',1,'[{\"added\": {}}]',5,1),(2,'2020-03-23 22:21:01.646475','2','testuser',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',5,1),(3,'2020-03-23 22:21:24.861191','2','testuser',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',5,1),(4,'2020-03-23 22:22:08.958291','scottk3','Netid is: scottk3',1,'[{\"added\": {}}]',1,2),(5,'2020-03-23 22:24:30.046524','cding20','Netid is: cding20',1,'[{\"added\": {}}]',1,2),(6,'2020-03-23 22:25:11.236219','myc2','Netid is: myc2',1,'[{\"added\": {}}]',1,2),(7,'2020-03-23 22:25:55.108285','mkhan259','Netid is: mkhan259',1,'[{\"added\": {}}]',1,2),(8,'2020-03-23 22:31:23.005202','cding20','Netid is: cding20',2,'[{\"changed\": {\"fields\": [\"interests\"]}}]',1,2),(9,'2020-03-23 22:56:04.246913','cding20','Netid is: cding20',2,'[]',1,2),(10,'2020-03-23 22:56:08.478750','mkhan259','Netid is: mkhan259',2,'[]',1,2),(11,'2020-03-23 22:56:10.928078','cding20','Netid is: cding20',2,'[]',1,2),(12,'2020-03-23 22:56:13.681628','myc2','Netid is: myc2',2,'[]',1,2),(13,'2020-03-23 22:56:16.711835','scottk3','Netid is: scottk3',2,'[]',1,2),(14,'2020-03-23 22:56:19.608388','mkhan259','Netid is: mkhan259',2,'[]',1,2),(15,'2020-04-06 12:56:07.703113','ACM ICPC','Student Group: ACM ICPC',1,'[{\"added\": {}}]',8,1),(16,'2020-04-06 12:59:07.919825','ASME Competitions','Student Group: ASME Competitions',1,'[{\"added\": {}}]',8,1),(17,'2020-04-06 13:49:56.853618','ACM ICPC','Student Group: ACM ICPC',2,'[]',8,1),(18,'2020-04-07 01:24:45.759876','bangaru2','Student: bangaru2',1,'[{\"added\": {}}]',1,2),(19,'2020-04-07 01:25:36.461261','podar2','Student: podar2',1,'[{\"added\": {}}]',1,2),(20,'2020-04-07 01:26:13.245936','isanaka2','Student: isanaka2',1,'[{\"added\": {}}]',1,2),(21,'2020-04-07 01:26:33.124075','raghav3','Student: raghav3',1,'[{\"added\": {}}]',1,2),(22,'2020-04-07 01:27:00.343174','nikashw2','Student: nikashw2',1,'[{\"added\": {}}]',1,2),(23,'2020-04-07 01:27:25.157492','megharm2','Student: megharm2',1,'[{\"added\": {}}]',1,2),(24,'2020-04-07 01:28:23.519254','jcolla3','Student: jcolla3',1,'[{\"added\": {}}]',1,2),(25,'2020-04-07 01:29:38.093431','eshiafr2','Student: eshiafr2',1,'[{\"added\": {}}]',1,2),(26,'2020-04-07 01:30:33.201127','tincher2','Student: tincher2',1,'[{\"added\": {}}]',1,2),(27,'2020-04-07 02:47:16.488303','1','Resume: Student: bangaru2',1,'[{\"added\": {}}]',10,1),(28,'2020-04-07 02:49:19.007888','2','Resume: Student: podar2',1,'[{\"added\": {}}]',10,1),(29,'2020-04-07 02:51:08.685867','3','Resume: Student: isanaka2',1,'[{\"added\": {}}]',10,1),(30,'2020-04-07 02:51:28.575473','4','Resume: Student: tincher2',1,'[{\"added\": {}}]',10,1),(31,'2020-04-07 02:52:29.516415','5','Resume: Student: raghav3',1,'[{\"added\": {}}]',10,1),(32,'2020-04-07 02:54:38.812340','6','Resume: Student: mkhan259',1,'[{\"added\": {}}]',10,1),(33,'2020-04-07 02:55:37.317902','7','Resume: Student: myc2',1,'[{\"added\": {}}]',10,1),(34,'2020-04-07 02:55:48.416899','7','Resume: Student: myc2',2,'[]',10,1),(35,'2020-04-07 02:56:17.082053','8','Resume: Student: nikashw2',1,'[{\"added\": {}}]',10,1),(36,'2020-04-07 02:57:46.384444','9','Resume: Student: megharm2',1,'[{\"added\": {}}]',10,1),(37,'2020-04-07 02:58:25.238000','10','Resume: Student: eshiafr2',1,'[{\"added\": {}}]',10,1),(38,'2020-04-07 02:59:41.296694','11','Resume: Student: jcolla3',1,'[{\"added\": {}}]',10,1),(39,'2020-04-08 23:03:06.164355','tincher2','Student: tincher2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(40,'2020-04-08 23:27:03.035547','bangaru2','Student: bangaru2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\"]}}]',1,1),(41,'2020-04-09 02:08:15.620358','tincher2','Student: tincher2',2,'[{\"changed\": {\"fields\": [\"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(42,'2020-04-09 02:08:36.991094','tincher2','Student: tincher2',2,'[]',1,1),(43,'2020-04-09 02:10:53.260192','scottk3','Student: scottk3',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(44,'2020-04-09 02:13:00.311977','rthaker2','Student: rthaker2',1,'[{\"added\": {}}]',1,1),(45,'2020-04-09 02:13:55.586705','raghav3','Student: raghav3',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(46,'2020-04-09 02:14:46.667463','podar2','Student: podar2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(47,'2020-04-09 02:16:44.977773','nikashw2','Student: nikashw2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(48,'2020-04-09 02:18:44.706985','myc2','Student: myc2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(49,'2020-04-09 02:19:47.051949','mkhan259','Student: mkhan259',2,'[{\"changed\": {\"fields\": [\"name\", \"interests\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(50,'2020-04-09 02:20:45.939318','megharm2','Student: megharm2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(51,'2020-04-09 02:23:37.275070','jcolla3','Student: jcolla3',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(52,'2020-04-09 02:25:35.337422','isanaka2','Student: isanaka2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(53,'2020-04-09 02:26:49.029801','eshiafr2','Student: eshiafr2',2,'[{\"changed\": {\"fields\": [\"name\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(54,'2020-04-09 02:27:23.610409','bangaru2','Student: bangaru2',2,'[{\"changed\": {\"fields\": [\"interests\", \"gradYear\", \"courseWork\", \"projects\", \"experiences\"]}}]',1,1),(55,'2020-04-09 02:29:11.677449','myc2','Student: myc2',2,'[{\"changed\": {\"fields\": [\"name\", \"interests\"]}}]',1,1),(56,'2020-04-09 15:10:04.307026','Cool Kids Club','Student Group: Cool Kids Club',1,'[{\"added\": {}}]',8,1),(57,'2020-04-09 15:12:27.158763','Sgt. Pepper\'s Lonely','Student Group: Sgt. Pepper\'s Lonely',1,'[{\"added\": {}}]',8,1),(58,'2020-04-09 15:12:52.249482','ACM ICPC','Student Group: ACM ICPC',2,'[{\"changed\": {\"fields\": [\"members\"]}}]',8,1),(59,'2020-04-09 15:13:49.080175','ACM','Student Group: ACM',2,'[{\"changed\": {\"fields\": [\"name\", \"description\", \"members\"]}}]',8,1),(60,'2020-04-10 15:09:24.310035','Microsoft','Company: Microsoft',1,'[{\"added\": {}}]',11,1),(61,'2020-04-10 15:09:40.123408','Facebook','Company: Facebook',1,'[{\"added\": {}}]',11,1),(62,'2020-04-10 15:09:59.464889','UIUC','Company: UIUC',1,'[{\"added\": {}}]',11,1),(63,'2020-04-10 15:10:07.459297','State Farm','Company: State Farm',1,'[{\"added\": {}}]',11,1),(64,'2020-04-10 15:11:18.165070','Pure Storage','Company: Pure Storage',1,'[{\"added\": {}}]',11,1),(65,'2020-04-10 15:11:55.508498','1','Internship: Company: Microsoft',1,'[{\"added\": {}}]',12,1),(66,'2020-04-10 15:13:31.564550','2','Internship: Company: Pure Storage',1,'[{\"added\": {}}]',12,1),(67,'2020-04-10 15:14:05.084592','3','Internship: Company: Pure Storage',1,'[{\"added\": {}}]',12,1),(68,'2020-04-10 15:14:11.627607','3','Internship: Company: Pure Storage',3,'',12,1),(69,'2020-04-10 15:14:16.064949','2','Internship: Company: Pure Storage',2,'[]',12,1),(70,'2020-04-10 15:15:30.842477','4','Internship: Company: Pure Storage',1,'[{\"added\": {}}]',12,1),(71,'2020-04-10 15:15:49.562876','5','Internship: Company: State Farm',1,'[{\"added\": {}}]',12,1),(72,'2020-04-10 15:17:35.237508','6','Internship: Company: UIUC',1,'[{\"added\": {}}]',12,1),(73,'2020-04-10 15:18:50.904716','7','Internship: Company: Microsoft',1,'[{\"added\": {}}]',12,1),(74,'2020-04-10 15:18:51.169194','8','Internship: Company: Microsoft',1,'[{\"added\": {}}]',12,1),(75,'2020-04-10 16:20:59.412965','Tiffany Tan','Recruiter: Tiffany Tan',2,'[]',9,1),(76,'2020-04-22 10:50:12.924934','3','testuser2',1,'[{\"added\": {}}]',5,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(5,'auth','user'),(6,'contenttypes','contenttype'),(11,'resume_book','company'),(12,'resume_book','internship'),(9,'resume_book','recruiter'),(10,'resume_book','resume'),(1,'resume_book','student'),(8,'resume_book','studentgroup'),(7,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-03-23 22:00:12.421320'),(2,'auth','0001_initial','2020-03-23 22:00:13.702622'),(3,'admin','0001_initial','2020-03-23 22:00:14.770581'),(4,'admin','0002_logentry_remove_auto_add','2020-03-23 22:00:14.979300'),(5,'admin','0003_logentry_add_action_flag_choices','2020-03-23 22:00:15.056654'),(6,'contenttypes','0002_remove_content_type_name','2020-03-23 22:00:15.503915'),(7,'auth','0002_alter_permission_name_max_length','2020-03-23 22:00:15.749718'),(8,'auth','0003_alter_user_email_max_length','2020-03-23 22:00:15.893586'),(9,'auth','0004_alter_user_username_opts','2020-03-23 22:00:15.975174'),(10,'auth','0005_alter_user_last_login_null','2020-03-23 22:00:16.129094'),(11,'auth','0006_require_contenttypes_0002','2020-03-23 22:00:16.197547'),(12,'auth','0007_alter_validators_add_error_messages','2020-03-23 22:00:16.284231'),(13,'auth','0008_alter_user_username_max_length','2020-03-23 22:00:16.444855'),(14,'auth','0009_alter_user_last_name_max_length','2020-03-23 22:00:16.595816'),(15,'auth','0010_alter_group_name_max_length','2020-03-23 22:00:16.746122'),(16,'auth','0011_update_proxy_permissions','2020-03-23 22:00:16.917715'),(17,'resume_book','0001_initial','2020-03-23 22:00:17.144333'),(18,'sessions','0001_initial','2020-03-23 22:00:17.368529'),(19,'resume_book','0002_studentgroup','2020-04-06 12:44:18.260491'),(20,'resume_book','0003_company_internship_recruiter_resume','2020-04-07 02:43:37.961277'),(21,'resume_book','0004_resume_dateadded','2020-04-08 21:01:15.677167'),(22,'resume_book','0005_student_name','2020-04-08 22:58:04.970802'),(23,'resume_book','0006_auto_20200408_2257','2020-04-08 22:58:05.625095'),(24,'resume_book','0007_auto_20200409_0259','2020-04-09 06:50:55.417874'),(25,'resume_book','0007_auto_20200409_1450','2020-04-09 14:51:18.104265'),(26,'resume_book','0008_studentgroup_members','2020-04-09 15:02:46.353026'),(27,'resume_book','0009_auto_20200410_0509','2020-04-10 05:11:56.753435');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0krttv8kad42yt5uki03qzqgwll98rt1','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-24 15:09:10.575200'),('8em3ui6nef364c1i06qgc85jiwf6q665','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-22 23:25:37.889222'),('9i55es6q88b07hkde307mb8xk7wxt9wh','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-21 01:47:39.517191'),('bjev00rw2yj8nnwk41rvt45xnpu17vc1','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-20 12:46:46.882218'),('iwzhqaup8twakn2ycs0rve4ayqcxclj3','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-21 01:46:59.346225'),('k8e7ffyibq71pr0h4qv5hgu0d63yzetd','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-21 02:44:15.504590'),('m1o6u6vw456wcq1c7zphyzgwqp2yt97c','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-21 01:47:02.078526'),('rmnbi8ym5tyiugrscg0fu7ix3miml4z5','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-24 07:04:15.208064'),('rr7nnpy4mjaf73efvm34x2s40l7rh1my','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-06 23:23:07.383013'),('t1mbnyjlythn6wxsyt41bg4nh0aw4xmn','NDIxMzhmNGMxNjg1MWJkYWUyZWVhYjVlN2U3OTE0M2RkNmIxOTY4ZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxMTgxMzNkZGZhYjhmYTBkZDc3OTY5ZDU1YTEzMzgwMjkxY2E5MGNhIn0=','2020-04-06 22:55:51.941007'),('txh109m34vi70zi0x7pus0tjmltctg4y','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-05-06 10:48:13.414634'),('vkt8ag2s1uaviakjbbbyrcnzmx95xzor','NDIxMzhmNGMxNjg1MWJkYWUyZWVhYjVlN2U3OTE0M2RkNmIxOTY4ZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxMTgxMzNkZGZhYjhmYTBkZDc3OTY5ZDU1YTEzMzgwMjkxY2E5MGNhIn0=','2020-04-06 22:30:12.442384'),('x3ptbo4dvrca6i7jlnopv628453noz2k','OTc5MmM0ZjkyODBjOWMwNDU4OTQwZWIwYmM3MjY3ZWZlMGQ4ZmY5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWZlNzEwMmQ3ZWNiMmRmM2Y0YTE5MmQ3NTIyOTNhOTEwY2Y1MjE0In0=','2020-04-24 14:50:07.541301'),('y0wld3xo52072od236z81lsvyqmfkjej','NDIxMzhmNGMxNjg1MWJkYWUyZWVhYjVlN2U3OTE0M2RkNmIxOTY4ZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxMTgxMzNkZGZhYjhmYTBkZDc3OTY5ZDU1YTEzMzgwMjkxY2E5MGNhIn0=','2020-04-06 22:31:07.712932');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resume_book_company`
--

DROP TABLE IF EXISTS `resume_book_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resume_book_company` (
  `companyName` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `rating` int(11) DEFAULT NULL,
  `sponsorDate` date NOT NULL,
  PRIMARY KEY (`companyName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume_book_company`
--

LOCK TABLES `resume_book_company` WRITE;
/*!40000 ALTER TABLE `resume_book_company` DISABLE KEYS */;
INSERT INTO `resume_book_company` VALUES ('Facebook','',5,'2020-04-10'),('Microsoft','',5,'2020-04-10'),('Pure Storage','The purest storage of them all',10,'2020-04-10'),('State Farm','',5,'2020-04-10'),('Uber','Uber Technologies, Inc. operates as a technology platform for people and things mobility. The firm offers multi-modal people transportation, restaurant food delivery, and connecting freight carriers and shippers. It operates through the following segments: Rides, Eats, Freight, Other Bets and ATG and Other Technology Programs. The Rides segment refers to products that connect consumers with Rides Drivers who provide rides in a variety of vehicles, such as cars, auto rickshaws, motorbikes, minibu',5,'2019-09-04'),('UIUC','',5,'2020-04-10');
/*!40000 ALTER TABLE `resume_book_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resume_book_internship`
--

DROP TABLE IF EXISTS `resume_book_internship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resume_book_internship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numberRating` double DEFAULT NULL,
  `projectDescription` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `companyReview` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `companyName_id` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `netID_id` varchar(8) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resume_book_internsh_companyName_id_31fcdb27_fk_resume_bo` (`companyName_id`),
  KEY `resume_book_internsh_netID_id_151736ea_fk_resume_bo` (`netID_id`),
  CONSTRAINT `resume_book_internsh_companyName_id_31fcdb27_fk_resume_bo` FOREIGN KEY (`companyName_id`) REFERENCES `resume_book_company` (`companyName`),
  CONSTRAINT `resume_book_internsh_netID_id_151736ea_fk_resume_bo` FOREIGN KEY (`netID_id`) REFERENCES `resume_book_student` (`netID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume_book_internship`
--

LOCK TABLES `resume_book_internship` WRITE;
/*!40000 ALTER TABLE `resume_book_internship` DISABLE KEYS */;
INSERT INTO `resume_book_internship` VALUES (1,5,'Improved performance practices by 50% for azure.com using lazy loading and caching','Great company, would highly recommend to all ACM interns!','2019-05-01','2020-08-01','Microsoft','jcolla3'),(2,10,'Implementing a pipeline to generate diagnostic PDF reports','Very friendly and relaxed atmosphere in the Seattle office. It\'s nice being able to get to know everyone in the ~30 person office.','2018-06-07','2018-09-07','Pure Storage','scottk3'),(4,10,'Parallelize the downloading of files across a distributed system.','The larger Mountain View office is more lively than Seattle, but more difficult to get to know non-interns because of sheer size.','2019-06-07','2020-09-07','Pure Storage','scottk3'),(5,5,'Developing alternative statistical models for calculating premiums','Awesome company close to the UIUC campus, would highly recommend','2019-01-01','2020-04-10','State Farm','podar2'),(6,5,'Non-negative matrix factorization on cancer gene expression data in order to classify certain cancers with 85% accuracy','Overall great experience doing research with the university','2018-09-01','2019-09-01','UIUC','myc2'),(7,5,'Ideated, architected, and developed both a browser security web extension and slouch detection mechanism utilizing Azure face detection','Amazing experience','2018-06-01','2018-08-01','Microsoft','megharm2'),(8,5,'Ideated, architected, and developed both a browser security web extension and slouch detection mechanism utilizing Azure face detection','Amazing experience','2018-06-01','2018-08-01','Microsoft','megharm2');
/*!40000 ALTER TABLE `resume_book_internship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resume_book_recruiter`
--

DROP TABLE IF EXISTS `resume_book_recruiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resume_book_recruiter` (
  `recruiterName` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `companyName_id` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`recruiterName`),
  KEY `resume_book_recruite_companyName_id_2113bce3_fk_resume_bo` (`companyName_id`),
  CONSTRAINT `resume_book_recruite_companyName_id_2113bce3_fk_resume_bo` FOREIGN KEY (`companyName_id`) REFERENCES `resume_book_company` (`companyName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume_book_recruiter`
--

LOCK TABLES `resume_book_recruiter` WRITE;
/*!40000 ALTER TABLE `resume_book_recruiter` DISABLE KEYS */;
INSERT INTO `resume_book_recruiter` VALUES ('Tiffany Tan','Uber');
/*!40000 ALTER TABLE `resume_book_recruiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resume_book_student`
--

DROP TABLE IF EXISTS `resume_book_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resume_book_student` (
  `netID` varchar(8) COLLATE utf8_unicode_ci NOT NULL,
  `interests` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `courseWork` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `experiences` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `gradYear` int(11) NOT NULL,
  `projects` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`netID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume_book_student`
--

LOCK TABLES `resume_book_student` WRITE;
/*!40000 ALTER TABLE `resume_book_student` DISABLE KEYS */;
INSERT INTO `resume_book_student` VALUES ('bangaru2','tik toks','Shresta Bangaru','Software Design Studio, Discrete Structures, Applied Linear Algebra, Probabilit & Stats for CS, Data Structures','Course Assistant - CS 126 (Software Design Studio), Undergraduate Research Assistant - Tran Research Group, Software Engineering Intern - App47',2023,'Gaussian Process Regression for Eye Diagram, Text Interpreter, Predicting Planet Habitability'),('cding20','UI/UX, Full-Stack Development','Cecilia Ding','Data Structures, Psychology, Database Systems','Uber SWE Intern, ACM Chair',2021,'ACM Resume Book Revamp'),('eshiafr2','android apps','Eshia Rustagi','Software Design Studio, Discrete Structures, Numerical Methods','Student Teacher Ambassador at Girls Who Code Naperville',2023,'HackIlinois Android App, ASL Translator, Color Memory Game'),('isanaka2','powerlifting','Akhil Isanaka','Data structures, systems programming','Ferco Aerospace Intern',2022,'Red Alert Robotics'),('jcolla3','gym','Jocelyn Collado','Data structures, algorithms, systems programming, web programming','Microsoft Explore Intern, Argonne National Laboratory Co-op Student/Employee + Computer Science Internship, Google CodeU Participant + CSSI Participant',2020,'N/A'),('jdoe2000','that','jimmy','them','that',2000,'those'),('megharm2','perfection','Megha Mattikalli','Data structures, computer architecture, linear algebra, discrete structures, software design, calculus III','Project Manager/Develoepr Intern, Web Platform Media Team at Microsoft, Co-Founder and CTO at Plenare, Intern at Spiration Olympus',2023,'Advancing the Diagnosis of Lung Cancer Utilizing Visual Biomarkers'),('mkhan259','being yelled at, being momed','Omar Khan','Data Structures and Algorithms, Discrete Structures, Computer Architecture, Elements of Syntax, Elements of Semantics and Pragmatics, Database System','Electrophysiologys and Language Processing Lab, PrairieLearn, Cache Simulator/Engineering Education Paper, Course assistant for CS 233, Sail Director, ACM Reflections | Projections Conference Content + Diversity x Tech Chair',2022,'MedMonitor, Cache Simulator'),('myc2','being a mom, yelling,','Melissa Chen','Software Engineering Studio, Discrete Structures, Data Structures, Computer Architecture, Numerial Methods, Systems Programming, Database Systems, Bioinformatics','UIUC Undergraduate Researcher, Academia Sinica Institute of Information Sciences Summer Research Intern',2022,'Music Maker, Safeways, Non-negative matrix factorization on cancer gene expression data'),('nikashw2','geese, honk, memes','Nikash Walia','Intro to CS, Software Design Studio, Linear Algebra, Data Structures, Numerical Methods, Probability/Statistics for CS','Data Science Research Intern NASA Ames Research Center, Machine Learning/Computer Vision Research Intern, San Jose State University',2023,'Classifying Transit-like Signals with Odd and Even Data, Text to Feature Mapping without Guidance for Anomaly Detection, Autonomous UAV Forced Graffiti Detection and Removal System Based on Machine Learning'),('podar2','peak male form','Rishub Podar','Python for Everybody Specialization by University of Michigan (Coursera), Discrete Structures, Software Design Studio, CS Freshman Honors, Calculus III, Data Structures, Computer Architecture, Probability and Statistics for Computer Science, Fundamental Mathematics','State Farm Insurance, Kaaenaat, HashIn Technology',2021,'Assignment Prioritizer'),('raghav3','clowning, wendy\'s, taco bell','Raghav Saini','Introductio to Computer Programing in Java, Freshman Honors, Statistical Analysis, Multivariable Calculus, Software Design Studio, Discrete Structures, Kotlin Programming','CS 125, Mathnasium',2022,'HackIllinois 2020 Android App, ISS Locator Pro, Secure&Sure'),('rthaker2','engineering computer','Rajat Thaker','Data structures, Digital systems laboratory','Course Grader ECE 120, Course Assistant ECE 110, President Illini Muay Thai',2021,'zettabuy.com, Digital Signal Processing'),('scottk3','being a squid when coughing','Scott Kim','Artificial Intelligence, Data Structures, Systems Programming, Computer Architecture','Pure Storage Summer Internship',2020,'Block Stacking Simulator, Raytracer'),('tincher2','Quantum Computing','Bailey Tincher','Artificial Intelligence, Machine Learning, Data Structures, Web Programming, Algorithms, Systems Programming','State Farm Research and Development Center Software Engineering Intern, CS 125 Course Developer, Illinois Tool Works Data Analytics Intern',2021,'QUIUC, ADSA, Overheard App');
/*!40000 ALTER TABLE `resume_book_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resume_book_studentgroup`
--

DROP TABLE IF EXISTS `resume_book_studentgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resume_book_studentgroup` (
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume_book_studentgroup`
--

LOCK TABLES `resume_book_studentgroup` WRITE;
/*!40000 ALTER TABLE `resume_book_studentgroup` DISABLE KEYS */;
INSERT INTO `resume_book_studentgroup` VALUES ('AAAAAAAAAAAAAAAAA','oh hey look this is in alphabetical order'),('ACM','is it safe to assume everyone we have so far?'),('ACM ICPC','A student organization focused on teaching and solving competitive programming problems.'),('ASME Competitions','UIUC team to partake in the annual Student Professional Development Conference design competition, now known as E-Fest'),('Changed Group','hello this is a test of changing names :)'),('Cool Kids Club','Where all the cool kids hang out'),('Sgt. Pepper\'s Lonely','I couldn\'t fit the whole name in the name :( i guess I\'m sgt pepper\'s lonely'),('Test Group','hello nice to meet u this is test <3');
/*!40000 ALTER TABLE `resume_book_studentgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resume_book_studentgroup_members`
--

DROP TABLE IF EXISTS `resume_book_studentgroup_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resume_book_studentgroup_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentgroup_id` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `student_id` varchar(8) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resume_book_studentgroup_studentgroup_id_student__d352610a_uniq` (`studentgroup_id`,`student_id`),
  KEY `resume_book_studentg_student_id_a2072f9e_fk_resume_bo` (`student_id`),
  CONSTRAINT `resume_book_studentg_student_id_a2072f9e_fk_resume_bo` FOREIGN KEY (`student_id`) REFERENCES `resume_book_student` (`netID`),
  CONSTRAINT `resume_book_studentg_studentgroup_id_0728dbfa_fk_resume_bo` FOREIGN KEY (`studentgroup_id`) REFERENCES `resume_book_studentgroup` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume_book_studentgroup_members`
--

LOCK TABLES `resume_book_studentgroup_members` WRITE;
/*!40000 ALTER TABLE `resume_book_studentgroup_members` DISABLE KEYS */;
INSERT INTO `resume_book_studentgroup_members` VALUES (14,'ACM','bangaru2'),(11,'ACM','eshiafr2'),(17,'ACM','isanaka2'),(10,'ACM','jcolla3'),(9,'ACM','megharm2'),(13,'ACM','mkhan259'),(12,'ACM','myc2'),(15,'ACM','nikashw2'),(16,'ACM','podar2'),(8,'ACM','raghav3'),(21,'ACM','rthaker2'),(20,'ACM','scottk3'),(19,'ACM','tincher2'),(7,'ACM ICPC','scottk3'),(2,'Cool Kids Club','mkhan259'),(1,'Cool Kids Club','myc2'),(5,'Cool Kids Club','scottk3'),(4,'Cool Kids Club','tincher2'),(6,'Sgt. Pepper\'s Lonely','scottk3');
/*!40000 ALTER TABLE `resume_book_studentgroup_members` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-22 21:00:23

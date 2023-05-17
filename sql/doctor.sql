-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: doctor
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `doctor_info`
--

DROP TABLE IF EXISTS `doctor_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_info` (
  `name` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `id` int DEFAULT NULL,
  `gender` enum('male','female') DEFAULT NULL,
  `motto` varchar(255) DEFAULT NULL,
  `headshot` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_info`
--

LOCK TABLES `doctor_info` WRITE;
/*!40000 ALTER TABLE `doctor_info` DISABLE KEYS */;
INSERT INTO `doctor_info` VALUES ('John Doe',30,1,'male','Live life to the fullest.','https://th.bing.com/th/id/OIP.lYrJ4HRJhS2hmCB9gxcHyQAAAA?w=147&h=149&c=7&r=0&o=5&dpr=1.3&pid=1.7'),('Jane Smith',35,2,'female','Be the change you wish to see in the world.','https://img.wxcha.com/m00/65/4e/89433954b6fdfacab88ffcdb8e84158e.jpg');
/*!40000 ALTER TABLE `doctor_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_table`
--

DROP TABLE IF EXISTS `doctor_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_table` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `_openid` varchar(50) DEFAULT NULL,
  `account_id` varchar(50) DEFAULT NULL,
  `head_shot` varchar(255) DEFAULT NULL,
  `patient` json DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `motto` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `todo_id` int DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_table`
--

LOCK TABLES `doctor_table` WRITE;
/*!40000 ALTER TABLE `doctor_table` DISABLE KEYS */;
INSERT INTO `doctor_table` VALUES (3,'ofpkt49O5l_bjAefJdor03t7NClc','123','https://img.wxcha.com/m00/65/4e/89433954b6fdfacab88ffcdb8e84158e.jpg  ','{\"id\": [1]}','123','男','保持乐观心态','123456789','主任医师','神经内科',1,'张三'),(4,'\"ofpkt49O5l_bjAefJdor03t7NClc\"','\"ee\"','\"https://thirdwx.qlogo.cn/mmopen/vi_32/q13pI6KWje3BglQcTjw56blUnCqSb0wrQCNdia4XAB35vBOJncmSiarFuZ6iaVBPvNEz39TtlNnnicUsgvNQwzhaNQ/132\"','null','\"123\"','null','null','null','null','null',1,'null'),(5,'\"ofpkt49O5l_bjAefJdor03t7NClc\"','\"1233\"','\"https://thirdwx.qlogo.cn/mmopen/vi_32/q13pI6KWje3BglQcTjw56blUnCqSb0wrQCNdia4XAB35vBOJncmSiarFuZ6iaVBPvNEz39TtlNnnicUsgvNQwzhaNQ/132\"','null','\"123\"','null','null','null','null','null',1,'null');
/*!40000 ALTER TABLE `doctor_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info` (
  `id` int NOT NULL,
  `name` varchar(11) DEFAULT NULL,
  `gender` enum('男','女') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_records`
--

DROP TABLE IF EXISTS `medical_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_records` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int NOT NULL,
  `contact_info` varchar(50) NOT NULL,
  `condition_description` text,
  `medical_history` text,
  `allergy_history` text,
  `situation` text,
  `medical` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_records`
--

LOCK TABLES `medical_records` WRITE;
/*!40000 ALTER TABLE `medical_records` DISABLE KEYS */;
INSERT INTO `medical_records` VALUES (1,'张三','男',30,'13812345678','头痛、发热、咳嗽','无','无','看看看看看看','开'),(2,'李四','女',45,'13687654321','右手疼痛，伴有肿胀','高血压、糖尿病','对青霉素过敏','手疼','截肢'),(3,'王五','男',60,'13911112222','长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试长文本测试','胆囊切除术后','对花生过敏',NULL,NULL),(4,'张三','男',19,'182665623587','胸痛有放射性','对空气过敏','无',NULL,NULL);
/*!40000 ALTER TABLE `medical_records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `id_1` int NOT NULL,
  `id_2` int NOT NULL,
  `message` varchar(255) NOT NULL,
  `time` datetime NOT NULL,
  `state` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,3,'你好','2023-05-15 20:44:00',0),(2,1,2,'hello','2023-05-15 20:53:00',0),(3,3,3,'你好','2023-05-15 20:45:00',0),(4,3,3,'你好','2023-05-16 20:45:00',0),(5,3,3,'你好','2023-05-14 22:45:00',0),(6,3,3,'None','2023-05-16 22:31:43',1),(7,3,3,'None','2023-05-16 22:35:54',0),(8,3,3,'None','2023-05-16 22:36:53',0),(9,3,3,'None','2023-05-16 22:38:16',0),(10,3,3,'None','2023-05-16 22:38:31',0),(11,3,3,'None','2023-05-16 22:38:46',0),(12,3,3,'None','2023-05-16 22:39:02',0),(13,3,3,'None','2023-05-16 22:39:03',0),(14,3,3,'hello','2023-05-16 22:39:20',0),(15,3,3,'你好我是张三','2023-05-16 23:52:01',0),(16,3,3,'你好我是张三','2023-05-16 23:53:57',0),(17,3,3,'123','2023-05-16 23:54:36',0),(18,3,3,'123','2023-05-16 23:55:19',0),(19,3,3,'你好我是张三','2023-05-16 23:56:01',0),(20,3,3,'123','2023-05-16 23:58:00',0),(21,3,3,'123','2023-05-16 23:58:54',0),(22,3,3,'123','2023-05-16 23:59:06',0),(23,3,3,'你好我是张三,今天我有点不舒服','2023-05-16 23:56:01',1),(24,3,3,'你好我是张三,今天我有点不舒服','2023-05-16 23:56:01',1),(25,3,3,'你好我是张三,我可能有点感冒','2023-05-16 23:56:01',1),(26,3,3,'123','2023-05-17 00:03:28',0),(27,3,2,'你好我是张三,我可能有点感冒','2023-05-16 23:56:01',1),(28,3,5,'你好我是张三,我可能有点感冒','2023-05-16 23:56:01',1),(29,3,2,'你好医生我有病','2023-05-17 15:29:00',0),(30,3,2,'你好医生我有病','2023-05-17 15:29:00',1),(31,3,3,'123','2023-05-17 15:56:30',0),(32,3,3,'123','2023-05-17 15:57:17',0),(33,3,3,'123','2023-05-17 15:57:44',0);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_info`
--

DROP TABLE IF EXISTS `patient_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_info` (
  `patient_name` varchar(255) DEFAULT NULL,
  `patient_id` int DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `disease_info` varchar(255) DEFAULT NULL,
  `medical_history` varchar(255) DEFAULT NULL,
  `doctor_id` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_info`
--

LOCK TABLES `patient_info` WRITE;
/*!40000 ALTER TABLE `patient_info` DISABLE KEYS */;
INSERT INTO `patient_info` VALUES ('张三',10001,'12345678901','感冒','无','无'),('张三',10002,'12345678901','胃疼','无','无'),('李四',10002,'12345678901','玉玉症','无','无'),('李四',10003,'12345678903','玉玉症','无','无');
/*!40000 ALTER TABLE `patient_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todolist`
--

DROP TABLE IF EXISTS `todolist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `todolist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `todo_item` varchar(255) DEFAULT NULL,
  `_openid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todolist`
--

LOCK TABLES `todolist` WRITE;
/*!40000 ALTER TABLE `todolist` DISABLE KEYS */;
INSERT INTO `todolist` VALUES (1,'2023-05-04','完成Bing Chatbot项目','ofpkt49O5l_bjAefJdor03t7NClc'),(2,'2023-05-13','给病人检查','ofpkt49O5l_bjAefJdor03t7NClc'),(3,'2023-05-13','给病人开药','ofpkt49O5l_bjAefJdor03t7NClc'),(4,'2023-05-12','询问病人情况','ofpkt49O5l_bjAefJdor03t7NClc');
/*!40000 ALTER TABLE `todolist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-17 16:48:33

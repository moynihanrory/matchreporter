CREATE DATABASE  IF NOT EXISTS `analysis` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `analysis`;
-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: analysis
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `kpi`
--

DROP TABLE IF EXISTS `kpi`;
/*!50001 DROP VIEW IF EXISTS `kpi`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `kpi` AS SELECT 
 1 AS `id`,
 1 AS `name`,
 1 AS `metric_id`,
 1 AS `metric_type_id`,
 1 AS `metric_type_name`,
 1 AS `metric_group_id`,
 1 AS `metric_group_name`,
 1 AS `total_type_id`,
 1 AS `total_type_name`,
 1 AS `dummy_count`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `match`
--

DROP TABLE IF EXISTS `match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match` (
  `team1` text NOT NULL,
  `team2` text NOT NULL,
  `date` datetime NOT NULL,
  `venue` varchar(200) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `playedOn` datetime DEFAULT NULL,
  `source` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match`
--

LOCK TABLES `match` WRITE;
/*!40000 ALTER TABLE `match` DISABLE KEYS */;
/*!40000 ALTER TABLE `match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match_events`
--

DROP TABLE IF EXISTS `match_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event` text,
  `half` int DEFAULT NULL,
  `kpi` text NOT NULL,
  `location` text,
  `player` text,
  `rawtime` text,
  `sector` int DEFAULT NULL,
  `team` text NOT NULL,
  `time` int DEFAULT NULL,
  `match_id` int NOT NULL,
  `lColumn` int DEFAULT NULL,
  `lRow` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK1_idx` (`match_id`),
  CONSTRAINT `FK1` FOREIGN KEY (`match_id`) REFERENCES `match` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_events`
--

LOCK TABLES `match_events` WRITE;
/*!40000 ALTER TABLE `match_events` DISABLE KEYS */;
/*!40000 ALTER TABLE `match_events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match_plays`
--

DROP TABLE IF EXISTS `match_plays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_plays` (
  `id` int NOT NULL AUTO_INCREMENT,
  `endtime` int DEFAULT NULL,
  `events` text,
  `next` int DEFAULT NULL,
  `origin` text NOT NULL,
  `origin_attacks` int DEFAULT NULL,
  `origin_team` text NOT NULL,
  `outcome` text NOT NULL,
  `outcome_attacks` int DEFAULT NULL,
  `outcome_team` text NOT NULL,
  `previous` int DEFAULT NULL,
  `starttime` text,
  `match_id` int NOT NULL,
  `reduced_outcome` text,
  `playid` int NOT NULL,
  `reduced_origin` text,
  PRIMARY KEY (`id`),
  KEY `FK2_idx` (`match_id`),
  CONSTRAINT `FK2` FOREIGN KEY (`match_id`) REFERENCES `match` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_plays`
--

LOCK TABLES `match_plays` WRITE;
/*!40000 ALTER TABLE `match_plays` DISABLE KEYS */;
/*!40000 ALTER TABLE `match_plays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `metric`
--

DROP TABLE IF EXISTS `metric`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metric` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `metric_type_id` int NOT NULL,
  `count` int NOT NULL DEFAULT '1',
  `total_type_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `FK_1_idx` (`metric_type_id`),
  CONSTRAINT `FK_1` FOREIGN KEY (`metric_type_id`) REFERENCES `metric_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metric`
--

LOCK TABLES `metric` WRITE;
/*!40000 ALTER TABLE `metric` DISABLE KEYS */;
INSERT INTO `metric` VALUES (1,'goal',1,1,9),(2,'point',1,1,10),(3,'opp goal',1,1,9),(4,'opp point',1,1,10),(5,'wide',2,1,0),(6,'short',2,1,0),(7,'save',2,1,0),(8,'save out 65',2,1,0),(9,'off posts',2,1,0),(10,'opp wide',2,1,0),(11,'opp short',2,1,0),(12,'opp save',2,1,0),(13,'opp save out 65',2,1,0),(14,'opp off posts',2,1,0),(15,'65',4,1,0),(16,'out sl',4,1,0),(17,'opp 65',4,1,0),(18,'opp out sl',4,1,0),(19,'possession',5,1,0),(20,'opp possession',5,1,0),(21,'pos possession',5,1,0),(22,'neg possession',5,1,0),(23,'tackle',5,1,0),(24,'opp tackle',5,1,0),(25,'ruck won',5,1,0),(26,'ruck lost',5,1,0),(27,'attack',6,1,0),(28,'opp attack',6,1,0),(29,'goal chance',6,1,0),(30,'opp goal chance',6,1,0),(31,'throw in',6,1,0),(32,'own po won',3,1,0),(33,'own po lost',3,1,0),(34,'opp po won',3,1,0),(35,'opp po lost',3,1,0),(36,'own sl won',7,1,0),(37,'own sl lost',7,1,0),(38,'opp sl won',7,1,0),(39,'opp sl lost',7,1,0),(40,'free against',8,1,0),(41,'opp free against',8,1,0),(42,'to won',8,1,0),(43,'to lost',8,1,0);
/*!40000 ALTER TABLE `metric` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `metric_group`
--

DROP TABLE IF EXISTS `metric_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metric_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `metric_type_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metric_group`
--

LOCK TABLES `metric_group` WRITE;
/*!40000 ALTER TABLE `metric_group` DISABLE KEYS */;
INSERT INTO `metric_group` VALUES (0,'all',0),(2,'from play',1),(3,'from placed',1),(4,'from 65',1),(5,'from sideline',1),(6,'clean',3),(7,'break',3),(10,'from play',2),(11,'from placed',2),(12,'from 65',2),(13,'from sideline',2);
/*!40000 ALTER TABLE `metric_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `metric_type`
--

DROP TABLE IF EXISTS `metric_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metric_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metric_type`
--

LOCK TABLES `metric_type` WRITE;
/*!40000 ALTER TABLE `metric_type` DISABLE KEYS */;
INSERT INTO `metric_type` VALUES (1,'score'),(2,'shot'),(3,'puckout'),(4,'deadball'),(5,'individual'),(6,'inplay'),(7,'sideline'),(8,'transition'),(9,'goals'),(10,'points');
/*!40000 ALTER TABLE `metric_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pitch`
--

DROP TABLE IF EXISTS `pitch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pitch` (
  `shapeId` int DEFAULT NULL,
  `shapeType` text,
  `shapeLabel` text,
  `pointId` int DEFAULT NULL,
  `pX` int DEFAULT NULL,
  `pY` int DEFAULT NULL,
  `pathId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`pathId`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pitch`
--

LOCK TABLES `pitch` WRITE;
/*!40000 ALTER TABLE `pitch` DISABLE KEYS */;
INSERT INTO `pitch` VALUES (1,'path','p16',0,0,0,1),(1,'path','p16',1,0,90,2),(1,'path','p16',2,20,90,3),(1,'path','p16',3,20,0,4),(2,'path','p26',0,20,0,5),(2,'path','p26',1,20,90,6),(2,'path','p26',2,50,90,7),(2,'path','p26',3,50,0,8),(3,'path','p36',0,50,0,9),(3,'path','p36',1,50,90,10),(3,'path','p36',2,70,90,11),(3,'path','p36',3,70,0,12),(4,'path','p46',0,70,0,13),(4,'path','p46',1,70,90,14),(4,'path','p46',2,90,90,15),(4,'path','p46',3,90,0,16),(5,'path','p56',0,90,0,17),(5,'path','p56',1,90,90,18),(5,'path','p56',2,125,90,19),(5,'path','p56',3,125,0,20),(6,'path','p66',0,125,0,21),(6,'path','p66',1,125,90,22),(6,'path','p66',2,145,90,23),(6,'path','p66',3,145,0,24),(7,'point','pp16',0,10,45,25),(8,'point','pp26',0,35,45,26),(9,'point','pp36',0,60,45,27),(10,'point','pp46',0,80,45,28),(11,'point','pp56',0,110,45,29),(12,'point','pp66',0,135,45,30);
/*!40000 ALTER TABLE `pitch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `kpi`
--

/*!50001 DROP VIEW IF EXISTS `kpi`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `kpi` AS select `m`.`id` AS `id`,concat(`m`.`name`,' ',`mg`.`name`) AS `name`,`m`.`id` AS `metric_id`,`m`.`metric_type_id` AS `metric_type_id`,`mt`.`name` AS `metric_type_name`,`mg`.`id` AS `metric_group_id`,`mg`.`name` AS `metric_group_name`,`m`.`total_type_id` AS `total_type_id`,`mt2`.`name` AS `total_type_name`,`m`.`count` AS `dummy_count` from (((`metric` `m` join `metric_group` `mg`) join `metric_type` `mt`) left join `metric_type` `mt2` on((`m`.`total_type_id` = `mt2`.`id`))) where ((`m`.`metric_type_id` = `mg`.`metric_type_id`) and (`m`.`metric_type_id` = `mt`.`id`) and (`m`.`metric_type_id` in (1,2)) and (`mg`.`id` > 0)) union select `m`.`id` AS `id`,concat(`m`.`name`,' ',`mg`.`name`) AS `name`,`m`.`id` AS `metric_id`,`m`.`metric_type_id` AS `metric_type_id`,`mt`.`name` AS `metric_type_name`,`mg`.`id` AS `metric_group_id`,`mg`.`name` AS `metric_group_name`,`m`.`total_type_id` AS `total_type_id`,`mt2`.`name` AS `total_type_name`,`m`.`count` AS `dummy_count` from (((`metric` `m` join `metric_group` `mg`) join `metric_type` `mt`) left join `metric_type` `mt2` on((`m`.`total_type_id` = `mt2`.`id`))) where ((`m`.`metric_type_id` = `mg`.`metric_type_id`) and (`m`.`metric_type_id` = `mt`.`id`) and (`m`.`metric_type_id` = 3) and (`mg`.`id` > 0)) union select `m`.`id` AS `id`,`m`.`name` AS `name`,`m`.`id` AS `metric_id`,`m`.`metric_type_id` AS `metric_type_id`,`mt`.`name` AS `metric_type_name`,0 AS `metric_group_id`,`mt2`.`name` AS `metric_group_name`,`m`.`total_type_id` AS `total_type_id`,`mt2`.`name` AS `total_type_name`,`m`.`count` AS `dummy_count` from ((`metric` `m` join `metric_type` `mt`) left join `metric_type` `mt2` on((`m`.`total_type_id` = `mt2`.`id`))) where (`m`.`metric_type_id` = `mt`.`id`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-14 14:52:55

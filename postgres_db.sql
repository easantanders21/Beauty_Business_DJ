-- script that create database
-- cat postgres_db.sql|sudo -u postgres psql
\c bb_products;

--SET FOREIGN_KEY_CHECKS=0;
SET session_replication_role = 'replica';

--LOCK TABLES 'category' WRITE;
INSERT INTO category VALUES (1,'gel'),(2,'shampoo'),(3,'reparador'),(4,'otros');
--UNLOCK TABLES;

--LOCK TABLES 'mark' WRITE;
INSERT INTO mark VALUES (1,'marcell france'),(2,'bella'),(3,'natura'),(4,'men');
--UNLOCK TABLES;

--LOCK TABLES `products` WRITE;
INSERT INTO products VALUES (1,'shammpoo aguacate',2,1),
                              (2,'shammpoo caspa',2,3),
                              (3,'gel moco gorilla',1,4),
                              (4,'reparador puntas',3,2),
                              (5,'aceite de coco',3,2),
                              (6,'gel marcell france',1,1),
                              (7,'keratina cojin',3,3),
                              (8,'gel ego',1,4),
                              (9,'shammpoo tinte rojo',2,2),
                              (10,'monas nina',4,2);
--UNLOCK TABLES;

--LOCK TABLES `providers` WRITE;
INSERT INTO providers VALUES (1,'Surtibelleza',2123,'calle 1'),
                               (2,'Nelly Narvaez',5486,'calle 2'),
                               (3,'Casa del peluquero',5657,'calle 3'),
                               (4,'Spayzon',5456,'calle 4');
--UNLOCK TABLES;


--LOCK TABLES `purchases` WRITE;
INSERT INTO purchases VALUES (1,1,'2022-02-01 02:17:06','SB-01'),
                               (2,2,'2022-02-02 02:17:06','S-01'),
                               (3,2,'2022-03-01 02:17:06','S-01');

--UNLOCK TABLES;

--LOCK TABLES `stock` WRITE;
INSERT INTO stock VALUES (1,1,3,10000,13000,9,1),
                           (2,1,8,3000,5000,10,10),
                           (3,1,6,7000,10000,10,5),
                           (4,2,1,15000,20000,0,5),
                           (5,2,2,14000,19000,8,2),
                           (6,3,1,16000,21000,0,4);
--UNLOCK TABLES;

--LOCK TABLES `sales` WRITE;
INSERT INTO sales VALUES (1,'2022-02-05 02:17:06',4,2),
                           (2,'2022-02-08 02:17:06',1,1),
                           (3,'2022-02-09 02:17:06',3,3),
                           (4,'2022-02-09 02:50:06',4,2),
                           (5,'2022-02-15 02:17:06',2,5),
                           (6,'2022-02-18 02:17:06',5,2),
                           (7,'2022-02-25 02:17:06',4,1),
                           (8,'2022-03-02 02:17:06',2,5),
                           (9,'2022-03-10 02:17:06',6,7),
                           (10,'2022-02-10 02:17:06',3,2);
--UNLOCK TABLES;

--SET FOREIGN_KEY_CHECKS=1;
SET session_replication_role = 'origin';

SELECT * FROM category;
SELECT * FROM mark;
SELECT * FROM products;
SELECT * FROM providers; 
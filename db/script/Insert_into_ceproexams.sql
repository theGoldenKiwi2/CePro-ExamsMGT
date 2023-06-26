USE ceproexamsmgt;

INSERT INTO exam_type (id, code, name) VALUES
(1, 'EXAM', 'exam'),
(2, 'MT', 'Midterm'),
(3, 'MOCK', 'mock exam');

INSERT INTO service (id, code, description) VALUES
(1, 'SCAN_QR_PDF', 'Scan with QRCode to PDF'),
(2, 'SCAN_QR_JPG', 'Scan with QRCode to JPG'),
(3, 'ANS', 'Ans webapp plateform'),
(4, 'AMC', 'Auto-multiple-choice');

INSERT INTO exam_status (id, code, name) VALUES
(1, 'CANCELED', 'Canceled'),
(2, 'REGISTERED', 'Subscription for CePro Services registered'),
(3, 'PREP-TEACH', 'Preparation : teacher'),
(4, 'PREP-2COMPILE', 'Preparation : files to compile'),
(5, 'PREP-2CHECK', 'Preparation : files to check by teacher'),
(6, 'PREP-2PRINT', 'Preparation : files to print'),
(7, 'PRINTING', 'Copies printing @Repro'),
(8, 'PICK-UP', 'Copies to pick-up @Repro'),
(9, 'PICKED-UP', 'Copies picked-up'),
(10, 'WAIT-SCAN', 'Waiting for scanning'),
(11, 'REP-CUT', 'Cutting @Repro'),
(12, '2SCAN', 'Copies to scan'),
(13, 'SCANNED', 'Copies scanned'),
(14, 'WAIT-TEACH', 'Waiting for teacher'),
(15, 'FINISHED', 'Finished');

INSERT INTO user_type (id, code, name) VALUES
(1, 'CPRO', 'CePro'),
(2, 'PostDoc', 'Post Doctorant-e'),
(3, 'CdC', 'Chargé-e de cours'),
(4, 'CollabSci', 'Collaborateur-rice scientifique'),
(5, 'AssistSci', 'Assistant-e scientifique'),
(6, 'AssistDoc', 'Assistant-e doctorant-e'),
(7, 'Prof', 'Professeur-e'),
(8, 'MER', 'Maître d''enseignement'),
(9, 'AssistAdm', 'Assistant-e administratif-ve'),
(10, 'PATT', 'Professor Assistant Tenire Track'),
(11, 'Secr', 'Secrétair-e');

INSERT INTO service_level (id, code, name) VALUES
(1, 'Gold', 'Gold'),
(2, 'Silver', 'Silver'),
(3, 'Bronze', 'Bronze');

INSERT INTO academic_year (id, code, name) VALUES
(1, '2017-2018', 'Année académique 09.2017 - 08.2018'),
(2, '2018-2019', 'Année académique 09.2018 - 08.2019'),
(3, '2019-2020', 'Année académique 09.2019 - 08.2020'),
(4, '2020-2021', 'Année académique 09.2020 - 08.2021'),
(5, '2021-2022', 'Année académique 09.2021 - 08.2022'),
(6, '2022-2023', 'Année académique 09.2022 - 08.2023'),
(7, '2023-2024', 'Année académique 09.2023 - 08.2024');

INSERT INTO section (id, code, name) VALUES
(1,'AR','Architecture'),
(2,'CGC','Chimie, Génie Chimique'),
(3,'EL','Génie électrique et électronique'),
(4,'ENAC','Faculté '),
(5,'EULER','Cours Euler'),
(6,'GC','Génie civil'),
(7,'GM','Génie mécanique'),
(8,'IC','Informatique'),
(9,'IF','Ingénierie financière'),
(10,'MA','Mathématiques'),
(11,'MAN/CMS','Mise à niveau / Cours de mathématiques spéciales'),
(12,'MT','Microtechnique'),
(13,'MTE','Management, technologie et entrepreneuriat'),
(14,'MX','Matériaux'),
(15,'Other',''),
(16,'OTHER','Other'),
(17,'PH','Physique'),
(18,'SHS','Sciences Humaines et Sociales'),
(19,'SIE','Sciences et ingénierie de l''environnement'),
(20,'SV','Ingénierie des sciences du vivant'),
(21,'UNIL','Collège de Sciences (UNIL)');

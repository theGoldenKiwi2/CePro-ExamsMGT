USE ceproexams;


INSERT INTO exam_type (id, code, name) VALUES
(1, 'EXAM', 'exam'),
(2, 'MT', 'Midterm'),
(3, 'MOCK', 'mock exam');

INSERT INTO service (id, code, description) VALUES
(1, 'SCAN_QR_PDF', 'Scan with QRCode to PDF'),
(2, 'SCAN_QR_JPG', 'Scan with QRCode to JPG'),
(3, 'ANS', 'Ans webapp plateform'),
(4, 'AMC', 'Auto-multiple-choice');

INSERT INTO exam_status (id, code, description) VALUES
(1, 'CANCELED', 'Canceled'),
(2, 'REGISTERED', 'Subscription for CePro Services registered'),
(3, 'PREP-TEACH', 'Preparation : teacher'),
(4, 'PREP-2COMPILE', 'Preparation : files to compile'),
(5, 'PREP-2CHECK', 'Preparation : files to check by teacher'),
(6, 'PREP-2PRINT', 'Preparation : files to print'),
(7, 'PRINTING', 'Copies printing @Repro'),
(8, '2PICK-UP', 'Copies to pick-up @Repro'),
(9, 'PICKED-UP', 'Copies picked-up'),
(10, 'WAIT-SCAN', 'Waiting for scanning'),
(11, 'REP-CUT', 'Cutting @Repro'),
(12, '2SCAN', 'Copies to scan'),
(13, 'SCANNED', 'Copies scanned'),
(14, 'WAIT-TEACH', 'Waiting for teacher'),
(15, 'FINISHED', 'Finished');

INSERT INTO employee_type (id, code, name) VALUES
(1, 'CPRO', 'CePro'),
(2, 'Prof', 'Professeur-e'),
(3, 'PATT', 'Professor Assistant Tenire Track'),
(4, 'CollabSci', 'Collaborateur-rice scientifique'),
(5, 'AssistDoc', 'Assistant-e doctorant-e'),
(6, 'AssistAdm', 'Assistant-e administratif-ve'),
(7, 'CdC', 'Chargé-e de cours'),
(8, 'MER', 'Maître d''enseignement'),
(9, 'Secr', '#N/A'),
(10, 'NULL', 'NULL');

INSERT INTO service_level (id, code, name) VALUES
(1, 'Gold', 'Gold'),
(2, 'Silver', 'Silver'),
(3, 'Bronze', 'Bronze');

INSERT INTO section (id, code, name) VALUES
(1, 'MAN/CMS', 'Mise à Niveau / Cours de Mathématiques Spéciales'),
(2, 'EL', 'Génie électrique et électronique'),
(3, 'EULER', 'Cours Euler'),
(4, 'GC', 'Génie Civil'),
(5, 'GM', 'Génie Mécanique'),
(6, 'IC', 'Informatique et Communication'),
(7, 'IF', 'Ingénieurie Financière'),
(8, 'AR', 'Architecture'),
(9, 'MA', 'Mathématiques'),
(10, 'MT', 'Microtechnique'),
(11, 'MTE', 'Management, Technologie et entrepreneurship'),
(12, 'MX', 'Matériaux'),
(13, 'NX', 'Neuro-X'),
(14, 'PH', 'Physique'),
(15, 'SHS', 'Sciences Humaines et Sociales'),
(16, 'SIE', 'Sciences et Ingénierie de l''environnement'),
(17, 'SV', 'Sciences de la vie'),
(18, 'UNIL', 'Collège des Sciences');

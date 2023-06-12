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
(11, 'Secr', '#N/A');

INSERT INTO service_level (id, code, name) VALUES
(1, 'Gold', 'Gold'),
(2, 'Silver', 'Silver'),
(3, 'Bronze', 'Bronze')
DROP DATABASE IF EXISTS ceproexamsmgt;
CREATE DATABASE ceproexamsmgt CHARACTER SET utf8mb4 collate utf8mb4_bin;

DROP TABLE IF EXISTS ceproexamsmgt.exam_has_section;
DROP TABLE IF EXISTS ceproexamsmgt.user_has_exam;
DROP TABLE IF EXISTS ceproexamsmgt.user;
DROP TABLE IF EXISTS ceproexamsmgt.user_type;
DROP TABLE IF EXISTS ceproexamsmgt.exam;
DROP TABLE IF EXISTS ceproexamsmgt.section;
DROP TABLE IF EXISTS ceproexamsmgt.service;
DROP TABLE IF EXISTS ceproexamsmgt.service_level;
DROP TABLE IF EXISTS ceproexamsmgt.exam_status;
DROP TABLE IF EXISTS ceproexamsmgt.exam_type;

CREATE TABLE ceproexamsmgt.user_type
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  code VARCHAR (20),
  name VARCHAR (50)
);

CREATE TABLE ceproexamsmgt.exam_type
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  code VARCHAR(20),
  name VARCHAR(50)
);

CREATE TABLE ceproexamsmgt.section
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  code VARCHAR(20),
  name VARCHAR(50)
);

CREATE TABLE ceproexamsmgt.exam_status
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  code VARCHAR(45) NULL,
  name VARCHAR(100) NULL
);

CREATE TABLE ceproexamsmgt.service_level 
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  code VARCHAR(20) NULL,
  name VARCHAR(50) NULL
);

CREATE TABLE ceproexamsmgt.service
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  code VARCHAR(45) NULL,
  description VARCHAR(100) NULL
  );

CREATE TABLE ceproexamsmgt.user
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  lastname VARCHAR(50),
  firstname VARCHAR(50) ,
  email VARCHAR(100),
  password VARCHAR(100),
  authenticated TINYINT(1),
  sciper VARCHAR(6),
  user_type_id INT,
  INDEX fk_user_type_idx (user_type_id ASC),
  CONSTRAINT fk_user_user_type_id FOREIGN KEY (user_type_id) REFERENCES user_type (id)
);

CREATE TABLE ceproexamsmgt.exam
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  code VARCHAR(20),
  name VARCHAR(50),
  service_level_id INT,
  service_id INT,
  exam_type_id INT,
  exam_status_id INT,
  exam_date DATETIME,
  exam_years VARCHAR (10),
  exam_semester VARCHAR (10),
  nb_students INT,
  nb_pages INT,
  deadline_prep DATETIME,
  deadline_repro DATETIME,
  remark VARCHAR (250),
  INDEX fk_service_level_idx (service_level_id ASC),
  INDEX fk_services_idx (service_id ASC),
  INDEX fk_exam_type_idx (exam_type_id ASC),
  INDEX fk_exam_status_idx (exam_status_id ASC),
  CONSTRAINT fk_exam_service_level FOREIGN KEY (service_level_id) REFERENCES service_level (id),
  CONSTRAINT fk_exam_service FOREIGN KEY (service_id) REFERENCES service (id),
  CONSTRAINT fk_exam_exam_type FOREIGN KEY (exam_type_id) REFERENCES exam_type (id),
  CONSTRAINT fk_exam_exam_status FOREIGN KEY (exam_status_id) REFERENCES exam_status (id)
    );
    
CREATE TABLE ceproexamsmgt.exam_has_section
(
  exam_id INT NOT NULL,
  section_id INT NOT NULL,
  PRIMARY KEY (exam_id, section_id),
  INDEX fk_section_idx (section_id ASC),
  INDEX fk_exam_idx (exam_id ASC),
  CONSTRAINT fk_exam_has_section_exam_id FOREIGN KEY (exam_id) REFERENCES exam (id),
  CONSTRAINT fk_exam_has_section_section_id FOREIGN KEY (section_id) REFERENCES section (id)
);

CREATE TABLE ceproexamsmgt.user_has_exam
(
  user_id INT NOT NULL,
  exam_id INT NOT NULL,
  PRIMARY KEY (user_id, exam_id),
  INDEX fk_exam_idx (exam_id ASC),
  INDEX fk_user (user_id ASC),
  CONSTRAINT fk_user_has_exam_user_id FOREIGN KEY (user_id) REFERENCES user (id),
  CONSTRAINT fk_user_has_exam_exam_id FOREIGN KEY (exam_id) REFERENCES exam (id)
)

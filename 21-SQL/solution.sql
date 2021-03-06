/*  create Database  */
CREATE DATABASE library;

/* Select database */
USE library;

/* CREATE TABLE 

    TABLES:
        1. author
        2. book
        3. client
        4. borrower
    
    we do not have to explicitly create an index for a primary key, it is done by default.

*/ 
CREATE TABLE IF NOT EXISTS author (
    author_id INT(10) NOT NULL AUTO_INCREMENT,
    author_first_name VARCHAR(255) NOT NULL,
    author_last_name VARCHAR(255) NOT NULL,
    author_nationality VARCHAR(255) NOT NULL,
    PRIMARY KEY (author_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS book(
    book_id INT(10) NOT NULL AUTO_INCREMENT,
    book_title VARCHAR(255) NOT NULL,
    book_author INT(10) NOT NULL, 
    genre VARCHAR(50) NOT NULL,
    PRIMARY KEY(book_id),
    FOREIGN KEY (book_author) REFERENCES author (author_id)
) ENGINE =InnoDB;

/* Client DOB Contains only year so data type for that will be year*/
CREATE TABLE IF NOT EXISTS client(
    client_id INT(10) NOT NULL AUTO_INCREMENT,
    client_first_name VARCHAR(255) NOT NULL,
    client_last_name VARCHAR(255) NOT NULL,
    client_dob YEAR(4) NOT NULL,
    occupation VARCHAR(50) NOT NULL,
    PRIMARY KEY(client_id)
)ENGINE =InnoDB;

CREATE TABLE IF NOT EXISTS borrower(
    borrow_id INT(10) NOT NULL AUTO_INCREMENT,
    client_id INT(10) NOT NULL,
    book_id INT(10) NOT NULL,
    borrow_date VARCHAR(50) NOT NULL,
    PRIMARY KEY(borrow_id),
    FOREIGN KEY(client_id) REFERENCES client (client_id),
    FOREIGN KEY(book_id) REFERENCES book (book_id)
)ENGINE=InnoDB;

/* INSERT DATA ON AUTHOR TABLE */

INSERT INTO books.author (
    author_id,
    author_first_name,
    author_last_name,
    author_nationality
)
VALUES
    (1,"Sofia", "Smith", "Canada"),
    (2,"Maria", "Brown", "Brazil"),
    (3,"Elena", "Martin", "Mexico"),
    (4,"Zoe", "Roy", "France"),
    (5,"Sebastian", "Lavoie", "Canada"),
    (6,"Dylan", "Garcia", "Spain"),
    (7,"Ian", "Cruz", "Mexico"),
    (8,"Lucas", "Smith", "USA"),
    (9,"Fabian", "Wilson", "USA"),
    (10,"Liam", "Taylor", "Canada"),
    (11,"William", "Thomas", "Great Britain"),
    (12,"Logan", "Moore", "Canada"),
    (13,"Oliver", "Martin", "France"),
    (14,"Alysha", "Thompson", "Canada"),
    (15,"Isabelle", "Lee", "Canada"),
    (16,"Emily", "Clark", "USA"),
    (17,"John", "Young", "China"),
    (18,"David", "Wright", "Canada"),
    (19,"Thomas", "Scott", "Canada"),
    (20,"Helena", "Adams", "Canada"),
    (21,"Sofia", "Carter", "USA"),
    (22,"Liam", "Parker", "Canada"),
    (23,"Emily", "Murphy", "USA");

/* INSERT DATA ON BOOK TABLE */

INSERT INTO books.book (
    book_id,
    book_title,
    book_author,
    genre
)
VALUES
    (1,"Build your database system", 1, "Science"),
    (2,"The red wall", 2, "Fiction"),
    (3,"The perfect match", 3, "Fiction"),
    (4,"Digital Logic", 4, "Science"),
    (5,"How to be a great lawyer", 5, "Law"),
    (6,"Manage successful negotiations", 6, "Society"),
    (7,"Pollution today", 7, "Science"),
    (8,"A gray park", 2, "Fiction"),
    (9,"How to be rich in one year", 8, "Humor"),
    (10,"Their bright fate", 9, "Fiction"),
    (11,"Black lines", 10, "Fiction"),
    (12,"History of theater", 11, "Literature"),
    (13,"Electrical transformers", 12, "Science"),
    (14,"Build your big data system", 1, "Science"),
    (15,"Right and left", 13, "Children"),
    (16,"Programming using Python", 1, "Science"),
    (17,"Computer networks", 14, "Science"),
    (18,"Performance evaluation", 15, "Science"),
    (19,"Daily exercise", 16, "Well being"),
    (20,"The silver uniform", 17, "Fiction"),
    (21,"Industrial revolution", 18, "History"),
    (22,"Green nature", 19, "Well being"),
    (23,"Perfect football", 20, "Well being"),
    (24,"The chocolate love", 21, "Humor"),
    (25,"Director and leader", 22, "Society"),
    (26,"Play football every week", 20, "well being"),
    (27,"Maya the bee", 13, "Children"),
    (28,"Perfect rugby", 20, "well being"),
    (29,"The end", 23, "Fiction"),
    (30,"Computer security", 1, "Science"),
    (31,"Participate", 22, "Society"),
    (32,"Positive figures", 3, "Fiction");

/* INSERT DATA ON CLIENT TABLE */
INSERT INTO books.client (
    client_id,
    client_first_name,
    client_last_name,
    client_dob,
    occupation
)
VALUES 
    (1, "Kaiden", "Hill", 2006, "Student"),
    (2, "Alina", "Morton", 2010, "Student"),
    (3, "Fania", "Brooks", 1983, "Food Scientist"),
    (4, "Courtney", "Jensen", 2006, "Student"),
    (5, "Brittany", "Hill", 1983, "Firefighter"),
    (6, "Max", "Rogers", 2005, "Student"),
    (7, "Margaret", "McCarthy", 1981, "School Psychologist"),
    (8, "Julie", "McCarthy", 1973, "Professor"),
    (9, "Ken", "McCarthy", 1974, "Securities Clerk"),
    (10, "Britany", "O'Quinn", 1984, "Violinist"),
    (11, "Conner", "Gardner", 1998, "Licensed Massage Therapist"),
    (12, "Mya", "Austin", 1960, "Parquet Floor Layer"),
    (13, "Thierry", "Rogers", 2004, "Student"),
    (14, "Eloise", "Rogers", 1984, "Computer Security Manager"),
    (15, "Gerard", "Jackson", 1979, "Oil Exploration Engineer"),
    (16, "Randy", "Day", 1986, "Aircraft Electrician"),
    (17, "Jodie", "Page", 1990, "Manufacturing Director"),
    (18, "Coral", "Rice", 1996, "Window Washer"),
    (19, "Ayman", "Austin", 2002, "Student"),
    (20, "Jaxson", "Austin", 1999, "Repair Worker"),
    (21, "Joel", "Austin", 1973, "Police Officer"),
    (22, "Alina", "Austin", 2010, "Student"),
    (23, "Elin", "Austin", 1962, "Payroll Clerk"),
    (24, "Ophelia", "Wolf", 2004, "Student"),
    (25, "Eliot", "McGuire", 1967, "Dentist"),
    (26, "Peter", "McKinney", 1968, "Professor"),
    (27, "Annabella", "Henry", 1974, "Nurse"),
    (28, "Anastasia", "Baker", 2001, "Student"),
    (29, "Tyler", "Baker", 1984, "Police Officer"),
    (30, "Lilian", "Ross", 1983, "Insurance Agent"),
    (31, "Thierry", "Arnold", 1975, "Bus Driver"),
    (32, "Angelina", "Rowe", 1979, "Firefighter"),
    (33, "Marcia", "Rowe", 1974, "Health Educator"),
    (34, "Martin", "Rowe", 1976, "Ship Engineer"),
    (35, "Adeline", "Rowe", 2005, "Student"),
    (36, "Colette", "Rowe", 1963, "Professor"),
    (37, "Diane", "Clark", 1975, "Payroll Clerk"),
    (38, "Caroline", "Clark", 1960, "Dentist"),
    (39, "Dalton", "Clayton", 1982, "Police Officer"),
    (40, "Kaiden", "Clayton", 1990, "Bus Driver"),
    (41, "Melanie", "Clayton", 1987, "Computer Engineer"),
    (42, "Alana", "Wilson", 2007, "Student"),
    (43, "Carson", "Byrne", 1995, "Food Scientist"),
    (44, "Conrad", "Byrne", 2007, "Student"),
    (45, "Ryan", "Porter", 2008, "Student"),
    (46, "Elin", "Porter", 1978, "Computer Programmer"),
    (47, "Tyler", "Harvey", 2007, "Student"),
    (48, "Arya", "Harvey", 2008, "Student"),
    (49, "Serena", "Harvey", 1978, "School Teacher"),
    (50, "Lilly", "Franklin", 1976, "Doctor"),
    (51, "Mai", "Franklin", 1994, "Dentist"),
    (52, "John", "Franklin", 1999, "Firefighter"),
    (53, "Judy", "Franklin", 1995, "Firefighter"),
    (54, "Katy", "Lloyd", 1992, "School Teacher"),
    (55, "Tamara", "Allen", 1963, "Ship Engineer"),
    (56, "Maxim", "Lyons", 1985, "Police Officer"),
    (57, "Allan", "Lyons", 1983, "Computer Engineer"),
    (58, "Marc", "Harris", 1980, "School Teacher"),
    (59, "Elin", "Young", 2009, "Student"),
    (60, "Diana", "Young", 2008, "Student"),
    (61, "Diane", "Young", 2006, "Student"),
    (62, "Alana", "Bird", 2003, "Student"),
    (63, "Anna", "Becker", 1979, "Security Agent"),
    (64, "Katie", "Grant", 1977, "Manager"),
    (65, "Joan", "Grant", 2010, "Student"),
    (66, "Bryan", "Bell", 2001, "Student"),
    (67, "Belle", "Miller", 1970, "Professor"),
    (68, "Peggy", "Stevens", 1990, "Bus Driver"),
    (69, "Steve", "Williamson", 1975, "HR Clerk"),
    (70, "Tyler", "Williamson", 1999, "Doctor"),
    (71, "Izabelle", "Williamson", 1990, "Systems Analyst"),
    (72, "Annabel", "Williamson", 1960, "Cashier"),
    (73, "Mohamed", "Waters", 1966, "Insurance Agent"),
    (74, "Marion", "Newman", 1970, "Computer Programmer"),
    (75, "Ada", "Williams", 1986, "Computer Programmer"),
    (76, "Sean", "Scott", 1983, "Bus Driver"),
    (77, "Farrah", "Scott", 1974, "Ship Engineer"),
    (78, "Christine", "Lambert", 1973, "School Teacher"),
    (79, "Alysha", "Lambert", 2007, "Student"),
    (80, "Maia", "Grant", 1984, "School Teacher");

/* INSERT DATA ON BORROWER TABLE 
    The given data format won't work in SQL. Date needs to be 
    converted into correct format. 
    used update query to convert string to date format.
*/

INSERT INTO borrower(
    borrow_id,
    client_id,
    book_id,
    borrow_date
) VALUES 
        (1,35,17,'20/07/2016'),
        (2,1,3,'19/04/2017'),
        (3,42,8,'03/10/2016'),
        (4,62,16,'05/04/2016'),
        (5,53,13,'17/01/2017'),
        (6,33,15,'26/11/2015'),
        (7,40,14,'21/01/2015'),
        (8,64,2,'10/09/2017'),
        (9,56,30,'02/08/2017'),
        (10,23,2,'28/06/2018'),
        (11,46,19,'18/11/2015'),
        (12,61,20,'24/11/2015'),
        (13,58,7,'17/06/2017'),
        (14,46,16,'12/02/2017'),
        (15,80,21,'18/03/2018'),
        (16,51,23,'01/09/2015'),
        (17,49,18,'28/07/2015'),
        (18,43,18,'04/11/2015'),
        (19,30,2,'10/08/2018'),
        (20,48,24,'13/05/2015'),
        (21,71,5,'05/09/2016'),
        (22,35,3,'03/07/2016'),
        (23,57,1,'17/03/2015'),
        (24,23,25,'16/08/2017'),
        (25,20,12,'24/07/2018'),
        (26,25,7,'31/01/2015'),
        (27,72,29,'10/04/2016'),
        (28,74,20,'31/07/2017'),
        (29,53,14,'20/02/2016'),
        (30,32,10,'24/07/2017'),
        (31,12,15,'25/04/2018'),
        (32,77,13,'09/06/2017'),
        (33,30,4,'24/10/2017'),
        (34,37,24,'14/01/2016'),
        (35,27,26,'05/06/2017'),
        (36,1,16,'06/05/2018'),
        (37,21,9,'19/03/2016'),
        (38,69,28,'29/03/2017'),
        (39,17,19,'14/03/2017'),
        (40,8,9,'22/04/2016'),
        (41,63,18,'25/01/2015'),
        (42,65,20,'10/10/2016'),
        (43,51,19,'28/07/2015'),
        (44,23,12,'25/01/2017'),
        (45,17,4,'18/04/2017'),
        (46,68,5,'06/09/2016'),
        (47,46,13,'30/09/2017'),
        (48,15,13,'05/07/2017'),
        (49,11,19,'14/12/2017'),
        (50,78,15,'26/01/2017'),
        (51,47,9,'03/03/2015'),
        (52,68,7,'26/05/2016'),
        (53,37,26,'06/02/2017'),
        (54,48,27,'30/12/2015'),
        (55,9,21,'21/10/2017'),
        (56,29,8,'01/04/2018'),
        (57,64,18,'29/08/2017'),
        (58,61,26,'21/02/2018'),
        (59,39,28,'26/07/2016'),
        (60,73,18,'22/08/2018'),
        (61,11,13,'17/01/2018'),
        (62,45,6,'20/07/2016'),
        (63,33,13,'18/03/2018'),
        (64,10,17,'06/06/2016'),
        (65,28,18,'17/02/2017'),
        (66,51,3,'09/12/2016'),
        (67,29,2,'18/09/2015'),
        (68,28,30,'14/09/2017'),
        (69,74,20,'12/12/2015'),
        (70,15,22,'14/01/2015'),
        (71,57,8,'20/08/2017'),
        (72,2,5,'18/01/2015'),
        (73,74,12,'14/04/2018'),
        (74,51,10,'25/02/2016'),
        (75,25,17,'24/02/2015'),
        (76,45,21,'10/02/2017'),
        (77,27,25,'03/08/2016'),
        (78,32,28,'15/06/2016'),
        (79,71,21,'21/05/2017'),
        (80,75,26,'03/05/2016'),
        (81,56,32,'23/12/2015'),
        (82,26,32,'16/05/2015'),
        (83,66,32,'30/05/2015'),
        (84,57,18,'15/09/2017'),
        (85,40,15,'02/09/2016'),
        (86,65,4,'17/08/2017'),
        (87,54,7,'19/12/2015'),
        (88,29,4,'22/07/2017'),
        (89,44,9,'31/12/2017'),
        (90,56,31,'13/06/2015'),
        (91,17,4,'01/04/2015'),
        (92,35,16,'19/07/2018'),
        (93,22,18,'22/06/2017'),
        (94,39,24,'29/05/2015'),
        (95,63,14,'20/01/2018'),
        (96,53,21,'31/07/2016'),
        (97,40,9,'10/07/2016'),
        (98,52,4,'05/04/2017'),
        (99,27,20,'04/09/2016'),
        (100,72,29,'06/12/2015'),
        (101,49,16,'19/12/2017'),
        (102,6,12,'04/12/2016'),
        (103,74,31,'27/07/2016'),
        (104,48,32,'29/06/2016'),
        (105,69,2,'27/12/2016'),
        (106,60,32,'29/10/2017'),
        (107,45,22,'12/06/2017'),
        (108,42,15,'14/05/2017'),
        (109,79,8,'13/10/2016'),
        (110,70,18,'04/12/2016'),
        (111,34,8,'06/03/2016'),
        (112,43,8,'19/12/2015'),
        (113,42,32,'20/04/2016'),
        (114,67,5,'06/03/2017'),
        (115,80,25,'23/06/2015'),
        (116,54,11,'03/05/2017'),
        (117,34,28,'30/08/2017'),
        (118,65,20,'26/08/2017'),
        (119,61,19,'05/01/2018'),
        (120,38,12,'17/01/2018'),
        (121,51,4,'13/05/2016'),
        (122,7,16,'17/03/2016'),
        (123,46,16,'25/11/2016'),
        (124,75,30,'12/08/2018'),
        (125,72,32,'12/03/2015'),
        (126,44,17,'15/06/2015'),
        (127,68,15,'21/02/2016'),
        (128,21,1,'19/06/2016'),
        (129,14,25,'10/10/2016'),
        (130,68,21,'27/05/2016'),
        (131,35,20,'19/03/2015'),
        (132,16,27,'08/08/2016'),
        (133,79,31,'07/03/2018'),
        (134,14,17,'28/04/2018'),
        (135,29,28,'11/03/2018'),
        (136,41,4,'08/08/2018'),
        (137,42,3,'23/02/2016'),
        (138,45,3,'10/07/2017'),
        (139,36,16,'19/07/2018'),
        (140,36,30,'07/08/2015'),
        (141,54,32,'14/03/2018'),
        (142,61,15,'28/03/2017'),
        (143,1,13,'17/05/2018'),
        (144,43,1,'14/05/2015'),
        (145,37,14,'30/07/2015'),
        (146,62,17,'19/09/2015'),
        (147,50,22,'02/12/2016'),
        (148,45,1,'24/07/2016'),
        (149,32,17,'10/03/2018'),
        (150,13,28,'14/02/2016'),
        (151,15,9,'11/08/2018'),
        (152,10,19,'29/08/2018'),
        (153,66,3,'27/11/2016'),
        (154,68,29,'12/07/2017'),
        (155,21,14,'27/06/2018'),
        (156,35,9,'22/01/2016'),
        (157,17,24,'25/08/2016'),
        (158,40,21,'09/07/2015'),
        (159,1,24,'28/03/2016'),
        (160,70,27,'10/07/2015'),
        (161,80,26,'24/04/2016'),
        (162,29,5,'18/10/2015'),
        (163,76,12,'25/04/2018'),
        (164,22,4,'24/12/2016'),
        (165,2,2,'26/10/2017'),
        (166,35,13,'28/02/2016'),
        (167,40,8,'02/10/2017'),
        (168,68,9,'03/01/2016'),
        (169,32,5,'13/11/2016'),
        (170,34,17,'15/09/2016'),
        (171,34,16,'13/04/2018'),
        (172,80,30,'13/10/2016'),
        (173,20,32,'17/11/2015'),
        (174,36,10,'01/09/2017'),
        (175,78,12,'27/06/2018'),
        (176,57,8,'22/03/2016'),
        (177,75,11,'27/06/2017'),
        (178,71,10,'01/08/2015'),
        (179,48,22,'29/09/2015'),
        (180,19,16,'21/02/2016'),
        (181,79,30,'20/08/2018'),
        (182,70,13,'16/09/2016'),
        (183,30,6,'10/2/2017'),
        (184,45,12,'12/10/2017'),
        (185,30,27,'23/11/2016'),
        (186,26,3,'13/08/2016'),
        (187,66,6,'14/01/2017'),
        (188,47,15,'10/02/2016'),
        (189,53,30,'08/08/2018'),
        (190,80,16,'31/03/2016'),
        (191,70,13,'03/02/2018'),
        (192,14,25,'27/03/2016'),
        (193,46,22,'13/01/2016'),
        (194,30,32,'06/08/2015'),
        (195,60,14,'27/11/2016'),
        (196,14,13,'23/05/2018'),
        (197,71,15,'22/06/2016'),
        (198,38,21,'27/12/2015'),
        (199,69,30,'29/04/2017'),
        (200,49,31,'03/06/2018'),
        (201,28,28,'29/05/2015'),
        (202,49,3,'30/08/2016'),
        (203,75,1,'29/10/2015'),
        (204,78,3,'12/05/2017'),
        (205,43,18,'25/03/2015'),
        (206,27,21,'22/02/2016'),
        (207,64,22,'03/04/2015'),
        (208,21,11,'09/12/2017'),
        (209,66,29,'20/12/2016'),
        (210,45,13,'15/04/2017'),
        (211,48,30,'31/01/2015'),
        (212,20,25,'20/12/2017'),
        (213,41,20,'29/01/2018'),
        (214,51,12,'05/07/2015'),
        (215,5,1,'12/04/2015'),
        (216,40,3,'24/02/2018'),
        (217,79,4,'27/06/2018'),
        (218,15,10,'01/11/2016'),
        (219,42,22,'28/12/2016'),
        (220,17,9,'29/01/2018'),
        (221,38,13,'09/05/2016'),
        (222,79,2,'06/12/2017'),
        (223,74,3,'07/12/2015'),
        (224,46,8,'05/06/2016'),
        (225,78,22,'11/08/2018'),
        (226,45,2,'20/04/2015'),
        (227,72,31,'11/11/2015'),
        (228,18,17,'21/03/2015'),
        (229,29,3,'13/08/2017'),
        (230,66,11,'05/06/2018'),
        (231,36,16,'28/04/2016'),
        (232,26,2,'23/10/2016'),
        (233,32,1,'31/10/2017'),
        (234,62,14,'25/07/2017'),
        (235,12,4,'08/07/2015'),
        (236,38,32,'24/02/2015'),
        (237,29,16,'28/07/2016'),
        (238,36,25,'07/05/2017'),
        (239,76,7,'13/06/2015'),
        (240,28,16,'15/08/2016'),
        (241,60,13,'26/08/2016'),
        (242,8,3,'28/07/2017'),
        (243,25,1,'30/07/2016'),
        (244,62,29,'24/08/2018'),
        (245,51,8,'01/09/2016'),
        (246,27,23,'08/02/2015'),
        (247,69,12,'25/06/2018'),
        (248,51,12,'04/07/2015'),
        (249,7,4,'01/05/2015'),
        (250,31,15,'29/10/2017'),
        (251,14,23,'15/01/2015'),
        (252,14,1,'21/05/2018'),
        (253,39,25,'26/12/2015'),
        (254,79,24,'31/05/2016'),
        (255,40,15,'18/03/2016'),
        (256,51,13,'13/04/2018'),
        (257,61,1,'11/02/2015'),
        (258,15,24,'02/03/2018'),
        (259,10,22,'21/01/2018'),
        (260,67,10,'8/7/2017'),
        (261,79,11,'11/12/2016'),
        (262,19,32,'04/05/2016'),
        (263,35,11,'01/08/2017'),
        (264,27,13,'15/12/2017'),
        (265,30,22,'22/12/2015'),
        (266,8,7,'26/06/2015'),
        (267,70,9,'20/03/2016'),
        (268,56,18,'29/01/2016'),
        (269,13,19,'06/03/2015'),
        (270,61,2,'18/06/2016'),
        (271,47,13,'18/09/2017'),
        (272,30,22,'19/02/2016'),
        (273,18,22,'31/12/2016'),
        (274,34,29,'27/10/2017'),
        (275,32,21,'03/06/2015'),
        (276,9,28,'30/03/2016'),
        (277,62,24,'23/03/2015'),
        (278,44,22,'29/04/2017'),
        (279,27,5,'25/03/2015'),
        (280,61,28,'14/07/2017'),
        (281,5,13,'04/12/2016'),
        (282,43,19,'15/03/2018'),
        (283,34,19,'05/06/2016'),
        (284,35,5,'19/02/2018'),
        (285,13,12,'23/09/2016'),
        (286,74,18,'26/12/2016'),
        (287,70,31,'15/08/2017'),
        (288,42,17,'15/06/2016'),
        (289,51,24,'30/07/2018'),
        (290,45,30,'15/01/2015'),
        (291,70,17,'07/10/2017'),
        (292,77,7,'06/01/2017'),
        (293,74,25,'25/09/2015'),
        (294,47,14,'01/02/2018'),
        (295,10,2,'18/04/2017'),
        (296,16,21,'03/10/2016'),
        (297,48,5,'17/09/2016'),
        (298,72,3,'10/02/2017'),
        (299,26,23,'01/03/2016'),
        (300,49,23,'25/10/2016');
/* CONVERT STRING COLUMN INTO DATE COLUMN */
UPDATE borrower set borrow_date=str_to_date(borrow_date,'%d/%m/%Y');


/* Q1 - Display all contents of the Clients table 

    This simple query retrive all the data from the table.
*/

SELECT * FROM client;

/* Q2 - First names, last names, ages and occupations of all clients 

    For easy readability used AS keyword to change the result column name.
    There is no age column in the database, so used current year and dob year to
    calculate age.
*/

SELECT client_first_name as first_name,
	   client_last_name as last_name,
       (YEAR(CURDATE()) - client_dob) as age,
       occupation from client;

/* Q3 - First and last names of clients that borrowed books in March 2018 

    Retrived first name, last name from client name. we need to join two table, 
    using table alise to get specfic data from the database.
    used where clause to filter the data
    used month() and year() to specify the condition.

*/

SELECT c.client_first_name as first_name, 
       c.client_last_name as last_name
	   FROM client AS c, borrower as b 
       WHERE YEAR(DATE(b.borrow_date))=2018 AND 
             MONTH(DATE(b.borrow_date)) = 03 AND 
             c.client_id = b.client_id;

/* Q4 - First and last names of the top 5 authors clients borrowed in 2017 

    Since data spread over different database, we need to use join multiple database
    First retrived first name and lastname and gave alise to result column.
    Make sure both author table id and books table id matching, this is essential without that we can't
    retrive author name. 
    Matching book id from books table with borrower id book table, because author id not present in 
    brower table so we need to match with book table to get author id. 
    using Year() to restrict data only on the year 2017.
    Grouping based on bookid on borrower tabele.
    Using order by to check top 5 author and using limit keyword to restrict to 5 result.
*/

SELECT a.author_first_name AS first_name, 
	   a.author_last_name AS last_name
       FROM borrower as bo, book as b, author as a
       WHERE b.book_id = bo.book_id AND b.book_author = a.author_id
       AND YEAR(DATE(bo.borrow_date))=2017
       GROUP BY bo.book_id 
       ORDER BY count(bo.book_id) DESC LIMIT 5;

/* Q5 - Least 5 author nationalities clients borrowed during the years 2015-2017

    Like previous query data spread over different database, we need to use join 3 database to get data.
    First retrived nationality from author table and gave alise to result column.
    Connecting borower table books id with books table id to get all the authors. 
    then connecting with author table to retrive author data
    using Year() and between keywords to restrict data only between years 2015 and 2018
    Grouping based on author_nationality.
    Using order by on book_id to check least 5 author and using limit keyword to restrict to 5 result.
 */

SELECT a.author_nationality AS nationality
       FROM borrower as bo, book as b, author as a
       WHERE b.book_id = bo.book_id AND b.book_author = a.author_id
       AND YEAR(DATE(bo.borrow_date)) BETWEEN 2015 AND 2018
       GROUP BY a.author_nationality 
       ORDER BY count(bo.book_id) ASC LIMIT 5;

/* Q6 - The book that was most borrowed during the years 2015-2017 
    
    Books title has been retrived from books table,
    Connection borrower table book id with books table book id.
    usig year() and between keywords to retrive specific year value.

*/

SELECT b.book_title
       FROM borrower as bo, book as b
       WHERE b.book_id = bo.book_id
       AND YEAR(DATE(bo.borrow_date)) BETWEEN 2015 AND 2017
       GROUP BY bo.book_id
       ORDER BY count(bo.book_id) DESC LIMIT 1;

/* Q7 - Top borrowed genres for client born in years 1970-1980 

    Genere retrived from books table and matching book id on the book
    table with borrower table book id. We need to capture client id which available 
    only on borrower and cliend id. after matching client id checking conditon to 
    retrive data only between 1970 and 1980. 
    Group by genere and order by get count of genre and identify top borrowd books.

*/

SELECT b.genre
       FROM borrower AS bo, book AS b, client as c
       WHERE b.book_id = bo.book_id AND bo.client_id = c.client_id
       AND c.client_dob BETWEEN 1970 and 1980
       GROUP BY b.genre 
       ORDER BY count(b.genre) DESC;

/* Q8 - Top 5 occupations that borrowed the most in 2016 

    ocuupation details available only on client table. 
    Link between borrower table and client table is client id
    using that retrive all the occupation information.
    Using conditional opearator we can restrict data only on year 2016.
    Group details based on occupation order desc to get top 5 occupation list.

*/

SELECT c.occupation
       FROM borrower AS bo, client AS c
       WHERE bo.client_id = c.client_id
       AND YEAR(bo.borrow_date) = 2016
       GROUP BY c.occupation 
       ORDER BY count(bo.client_id) DESC LIMIT 5;

/* Q9 - Average number of borrowed books by job title */

SELECT c.occupation, ROUND(COUNT(c.occupation) / COUNT(DISTINCT bo.client_id)) as avg_borrowd
        FROM borrower AS bo, client AS C
        WHERE bo.client_id = c.client_id
        GROUP BY c.occupation;

/* Q10 - Create a VIEW and display the titles that were borrowed by at least 20% of clients */

CREATE VIEW `Books Borrowed by atleast 20% of clients` AS 
    SELECT b.book_title FROM book as b, borrower as bo
    WHERE bo.book_id = b.book_id
    GROUP BY b.book_title
    HAVING COUNT(bo.client_id) >= (COUNT(bo.client_id)*0.2);

-- confirming the view created
SELECT * FROM `Books Borrowed by atleast 20% of clients`;

/* Q11 - The top month of borrows in 2017 */

SELECT MONTH(borrow_date) AS top_month, 
        COUNT(MONTH(borrow_date)) AS total_book_borrowed
        FROM borrower
        WHERE YEAR(borrow_date) = 2017
        GROUP BY MONTH(borrow_date)
        ORDER BY total_book_borrowed DESC LIMIT 3;

/* Q12 - Average number of borrows by age */

SELECT DISTINCT (YEAR(NOW()) - c.client_dob) AS age,
       ROUND(COUNT(c.client_id)/ COUNT(DISTINCT bo.client_id))AS average_borrowed
        FROM client as c, borrower as bo
        WHERE bo.client_id = c.client_id
        GROUP BY age;


/* Q13 - The oldest and the youngest clients of the library */

SELECT * FROM client where 
		client_dob in (SELECT MIN(client_dob) FROM client) OR
        client_dob in (SELECT MAX(client_dob) FROM client);


SELECT MAX(YEAR(NOW()) - c.client_dob) AS Oldest,
       MIN(YEAR(NOW())- c.client_dob)AS Youngest
        FROM client as c, borrower as bo
        WHERE bo.client_id = c.client_id;

/* Q14 - First and last names of authors that wrote books in more than one genre */

SELECT  a.author_first_name AS first_name,
        a.author_last_name AS last_name
        FROM author as a, book as b
        WHERE a.author_id = b.book_author
        GROUP BY a.author_id 
        HAVING (COUNT(b.genre) > 1);

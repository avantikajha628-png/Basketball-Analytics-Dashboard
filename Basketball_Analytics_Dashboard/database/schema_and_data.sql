BEGIN TRANSACTION;
CREATE TABLE games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            home_score INTEGER NOT NULL,
            away_score INTEGER NOT NULL,
            game_date TEXT NOT NULL
        );
INSERT INTO "games" VALUES(1,'Lakers','Warriors',118,112,'2026-01-05');
INSERT INTO "games" VALUES(2,'Bucks','Celtics',109,115,'2026-01-06');
INSERT INTO "games" VALUES(3,'Nuggets','Suns',121,118,'2026-01-07');
INSERT INTO "games" VALUES(4,'76ers','Knicks',102,108,'2026-01-08');
INSERT INTO "games" VALUES(5,'Mavericks','Clippers',130,124,'2026-01-09');
INSERT INTO "games" VALUES(6,'Heat','Cavaliers',99,105,'2026-01-10');
INSERT INTO "games" VALUES(7,'Timberwolves','Kings',112,110,'2026-01-11');
INSERT INTO "games" VALUES(8,'Thunder','Rockets',128,119,'2026-01-12');
INSERT INTO "games" VALUES(9,'Grizzlies','Pelicans',104,101,'2026-01-13');
INSERT INTO "games" VALUES(10,'Hawks','Pacers',116,120,'2026-01-14');
INSERT INTO "games" VALUES(11,'Spurs','Raptors',98,94,'2026-01-15');
INSERT INTO "games" VALUES(12,'Warriors','Suns',111,117,'2026-01-16');
INSERT INTO "games" VALUES(13,'Celtics','Knicks',122,113,'2026-01-17');
INSERT INTO "games" VALUES(14,'Lakers','Nuggets',108,114,'2026-01-18');
INSERT INTO "games" VALUES(15,'Bucks','76ers',119,110,'2026-01-19');
INSERT INTO "games" VALUES(16,'Cavaliers','Pacers',105,100,'2026-01-20');
INSERT INTO "games" VALUES(17,'Kings','Clippers',112,109,'2026-01-21');
INSERT INTO "games" VALUES(18,'Rockets','Mavericks',101,106,'2026-01-22');
INSERT INTO "games" VALUES(19,'Thunder','Timberwolves',124,118,'2026-01-23');
INSERT INTO "games" VALUES(20,'Heat','Hawks',96,92,'2026-01-24');
CREATE TABLE players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            team TEXT NOT NULL,
            position TEXT NOT NULL,
            games INTEGER NOT NULL,
            points INTEGER NOT NULL,
            assists INTEGER NOT NULL,
            rebounds INTEGER NOT NULL,
            field_goal REAL NOT NULL
        );
INSERT INTO "players" VALUES(1,'LeBron James','Lakers','Forward',55,1512,429,385,52.4);
INSERT INTO "players" VALUES(2,'Stephen Curry','Warriors','Guard',56,1428,336,246,45.2);
INSERT INTO "players" VALUES(3,'Kevin Durant','Suns','Forward',54,1458,216,351,52.1);
INSERT INTO "players" VALUES(4,'Giannis Antetokounmpo','Bucks','Forward',58,1734,348,638,61.0);
INSERT INTO "players" VALUES(5,'Nikola Jokic','Nuggets','Center',57,1596,570,690,58.3);
INSERT INTO "players" VALUES(6,'Joel Embiid','76ers','Center',50,1550,200,550,53.6);
INSERT INTO "players" VALUES(7,'Luka Doncic','Mavericks','Guard',56,1736,476,476,48.7);
INSERT INTO "players" VALUES(8,'Jayson Tatum','Celtics','Forward',58,1624,261,464,46.5);
INSERT INTO "players" VALUES(9,'Damian Lillard','Bucks','Guard',55,1540,385,220,43.8);
INSERT INTO "players" VALUES(10,'Devin Booker','Suns','Guard',53,1378,371,265,47.9);
INSERT INTO "players" VALUES(11,'Anthony Edwards','Timberwolves','Guard',57,1482,285,313,45.6);
INSERT INTO "players" VALUES(12,'Ja Morant','Grizzlies','Guard',45,1150,337,234,46.8);
INSERT INTO "players" VALUES(13,'Trae Young','Hawks','Guard',54,1350,594,205,43.1);
INSERT INTO "players" VALUES(14,'Jimmy Butler','Heat','Forward',52,1144,260,260,49.5);
INSERT INTO "players" VALUES(15,'Kawhi Leonard','Clippers','Forward',48,1152,187,230,51.2);
INSERT INTO "players" VALUES(16,'Paul George','76ers','Forward',50,1150,200,220,44.7);
INSERT INTO "players" VALUES(17,'Donovan Mitchell','Cavaliers','Guard',55,1512,275,220,46.3);
INSERT INTO "players" VALUES(18,'Bam Adebayo','Heat','Center',56,1120,224,616,52.8);
INSERT INTO "players" VALUES(19,'Domantas Sabonis','Kings','Center',58,1102,464,754,60.1);
INSERT INTO "players" VALUES(20,'Karl-Anthony Towns','Knicks','Center',54,1188,216,594,50.9);
INSERT INTO "players" VALUES(21,'De''Aaron Fox','Kings','Guard',56,1400,336,224,47.6);
INSERT INTO "players" VALUES(22,'Zion Williamson','Pelicans','Forward',40,960,200,240,57.3);
INSERT INTO "players" VALUES(23,'Shai Gilgeous-Alexander','Thunder','Guard',57,1710,342,285,51.4);
INSERT INTO "players" VALUES(24,'Anthony Davis','Lakers','Forward',53,1272,159,583,55.9);
INSERT INTO "players" VALUES(25,'Jaylen Brown','Celtics','Guard',55,1375,220,330,48.9);
INSERT INTO "players" VALUES(26,'Pascal Siakam','Pacers','Forward',54,1188,216,378,49.1);
INSERT INTO "players" VALUES(27,'Tyrese Haliburton','Pacers','Guard',56,1064,616,224,47.8);
INSERT INTO "players" VALUES(28,'Brandon Ingram','Pelicans','Forward',44,968,220,220,46.9);
INSERT INTO "players" VALUES(29,'Rudy Gobert','Timberwolves','Center',58,754,116,754,65.2);
INSERT INTO "players" VALUES(30,'Victor Wembanyama','Spurs','Center',55,1210,220,605,46.5);
INSERT INTO "players" VALUES(31,'Kyrie Irving','Mavericks','Guard',52,1300,260,208,47.3);
INSERT INTO "players" VALUES(32,'Klay Thompson','Mavericks','Guard',54,972,108,162,44.8);
INSERT INTO "players" VALUES(33,'Draymond Green','Warriors','Forward',55,550,385,385,50.6);
INSERT INTO "players" VALUES(34,'Chris Paul','Spurs','Guard',53,636,477,212,46.1);
INSERT INTO "players" VALUES(35,'Zach LaVine','Kings','Guard',50,1150,200,200,45.0);
INSERT INTO "players" VALUES(36,'Fred VanVleet','Rockets','Guard',56,952,392,168,41.3);
INSERT INTO "players" VALUES(37,'Jalen Brunson','Knicks','Guard',57,1596,399,171,47.6);
INSERT INTO "players" VALUES(38,'Alperen Sengun','Rockets','Center',56,1176,336,560,53.4);
INSERT INTO "players" VALUES(39,'Scottie Barnes','Raptors','Forward',56,1064,336,448,47.9);
INSERT INTO "players" VALUES(40,'Evan Mobley','Cavaliers','Center',55,990,165,550,55.1);
CREATE TABLE teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_name TEXT NOT NULL,
            conference TEXT NOT NULL,
            wins INTEGER NOT NULL,
            losses INTEGER NOT NULL
        );
INSERT INTO "teams" VALUES(1,'Lakers','Western',47,35);
INSERT INTO "teams" VALUES(2,'Warriors','Western',44,38);
INSERT INTO "teams" VALUES(3,'Suns','Western',49,33);
INSERT INTO "teams" VALUES(4,'Bucks','Eastern',51,31);
INSERT INTO "teams" VALUES(5,'Nuggets','Western',53,29);
INSERT INTO "teams" VALUES(6,'76ers','Eastern',46,36);
INSERT INTO "teams" VALUES(7,'Mavericks','Western',50,32);
INSERT INTO "teams" VALUES(8,'Celtics','Eastern',57,25);
INSERT INTO "teams" VALUES(9,'Timberwolves','Western',52,30);
INSERT INTO "teams" VALUES(10,'Grizzlies','Western',41,41);
INSERT INTO "teams" VALUES(11,'Hawks','Eastern',38,44);
INSERT INTO "teams" VALUES(12,'Heat','Eastern',45,37);
INSERT INTO "teams" VALUES(13,'Clippers','Western',48,34);
INSERT INTO "teams" VALUES(14,'Cavaliers','Eastern',54,28);
INSERT INTO "teams" VALUES(15,'Kings','Western',46,36);
INSERT INTO "teams" VALUES(16,'Knicks','Eastern',50,32);
INSERT INTO "teams" VALUES(17,'Pelicans','Western',42,40);
INSERT INTO "teams" VALUES(18,'Thunder','Western',56,26);
INSERT INTO "teams" VALUES(19,'Pacers','Eastern',45,37);
INSERT INTO "teams" VALUES(20,'Spurs','Western',39,43);
INSERT INTO "teams" VALUES(21,'Rockets','Western',43,39);
INSERT INTO "teams" VALUES(22,'Raptors','Eastern',33,49);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('players',40);
INSERT INTO "sqlite_sequence" VALUES('teams',22);
INSERT INTO "sqlite_sequence" VALUES('games',20);
COMMIT;

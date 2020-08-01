create table Ages(
name varchar(128),
age integer
)
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Kesia', 13);
INSERT INTO Ages (name, age) VALUES ('Analucia', 39);
INSERT INTO Ages (name, age) VALUES ('Alesha', 25);
INSERT INTO Ages (name, age) VALUES ('Graham', 15);
INSERT INTO Ages (name, age) VALUES ('Caitlyn', 13);
INSERT INTO Ages (name, age) VALUES ('Aaren', 27);
SELECT hex(name || age) AS X FROM Ages ORDER BY X

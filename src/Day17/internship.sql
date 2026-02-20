CREATE TABLE interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
);

INSERT INTO interns VALUES (1,'Asha','Data Science',15000);
INSERT INTO interns VALUES (2,'Rahul','Web Dev',12000);
INSERT INTO interns VALUES (3,'Meena','Data Science',16000);
INSERT INTO interns VALUES (4,'Kiran','UI/UX',10000);
INSERT INTO interns VALUES (5,'Vikram','Web Dev',14000);

SELECT name, track FROM interns;
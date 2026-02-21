sqlite3 sample.db

CREATE TABLE interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
);

INSERT INTO interns VALUES (1, 'Asha', 'Data Science', 15000);
INSERT INTO interns VALUES (2, 'Ravi', 'Web Development', 12000);
INSERT INTO interns VALUES (3, 'Maya', 'AI & ML', 18000);
INSERT INTO interns VALUES (4, 'Kiran', 'Data Science', 8000);
INSERT INTO interns VALUES (5, 'Neha', 'Web Development', 7000);

SELECT * 
FROM interns
WHERE track = 'Data Science' AND stipend > 5000;

SELECT track, AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track;

SELECT track, COUNT(*) AS intern_count
FROM interns
GROUP BY track;
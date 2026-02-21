sqlite3 sample.db

CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
);

INSERT INTO mentors VALUES (1, 'Dr. Smith', 'Data Science');
INSERT INTO mentors VALUES (2, 'Ms. Riya', 'Web Development');
INSERT INTO mentors VALUES (3, 'Mr. John', 'AI & ML');

SELECT interns.name AS Intern, interns.track AS Track, mentors.mentor_name AS Mentor
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
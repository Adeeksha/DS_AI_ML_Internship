# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 22:06:10 2026

@author: ADEEKSHA
"""

import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("D:\\DS_AI_Internship\\src\\Day18\\sample.db")

# INNER JOIN query
query = """
SELECT interns.name AS Intern, interns.track AS Track, mentors.mentor_name AS Mentor
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

# Load result into Pandas
df = pd.read_sql_query(query, conn)
print(df)

# Close connection
conn.close()
# training_data.py

ddl_applicants = """
CREATE TABLE applicants (
    applicantid INT,
    position INT,
    application_date DATE,
    stage VARCHAR(50),
    status VARCHAR(50),
    recruiter VARCHAR(50),
    country VARCHAR(50),
    applicant_name VARCHAR(100),
    salary INT
);
"""

ddl_ipl = """
CREATE TABLE ipl (
    "ID" serial PRIMARY KEY,
    "Wk" integer NOT NULL,
    "Date" date NOT NULL,
    "Home" varchar(50) NOT NULL,
    "HomeGoals" integer NOT NULL,
    "AwayGoals" integer NOT NULL,
    "Away" varchar(50) NOT NULL,
    "FTR" varchar(1) NOT NULL
);
"""

queries = [
    ("Select teams which have AwayGoals as 1", """
    SELECT "Home", "Away", "AwayGoals"
    FROM ipl
    WHERE "AwayGoals" = 1;
    """),
    ("Count the number of matches where FTR (Full Time Result) is 'H' (Home win)", """
    SELECT COUNT(*)
    FROM ipl
    WHERE "FTR" = 'H';
    """),
    ("Find the match with the highest number of total goals", """
    SELECT "Home", "Away", "HomeGoals", "AwayGoals"
    FROM ipl
    ORDER BY ("HomeGoals" + "AwayGoals") DESC
    LIMIT 1;
    """),
    
    ("List matches where both teams scored at least 2 goals ", """
    SELECT "Home", "Away", "HomeGoals", "AwayGoals"
            FROM ipl
            WHERE "HomeGoals" >= 2 AND "AwayGoals" >= 2;
    """),

    ("Calculate the average number of goals scored per match", """
     SELECT AVG("HomeGoals" + "AwayGoals") AS avg_goals_per_match
        FROM ipl;
     """),

    ("Find matches where the result was a draw (FTR is 'D') ", """
     SELECT "Home", "Away", "HomeGoals", "AwayGoals"
        FROM ipl
        WHERE "FTR" = 'D';
        """),
    (" List matches where the home team won by at least 2 goals", """
     SELECT "Home", "Away", "HomeGoals", "AwayGoals"
        FROM ipl
        WHERE "FTR" = 'H' AND ("HomeGoals" - "AwayGoals") >= 2;
        """),
    ("Identify matches where both teams had the same number of goals ", """
     SELECT "Home", "Away", "HomeGoals", "AwayGoals"
        FROM ipl
        WHERE "HomeGoals" = "AwayGoals";
        """),
    ("Retrieve the most recent matches played", """
     SELECT "Home", "Away", "Date"
        FROM ipl
        ORDER BY "Date" DESC
        LIMIT 10;
        """),
    ("Calculate the total number of matches played", """
     SELECT COUNT(*)
        FROM ipl;
     """),


    
]

documentation1 = """
The ipl table stores information about football matches including details about the date, teams involved, goals scored, and the result of the match. Below is the detailed documentation for each column in the table.
"""

queries_applicants = [
    ("Select applicants from a specific country (e.g., USA)", """
    SELECT "applicantid", "applicant_name", "position", "country"
    FROM applicants
    WHERE "country" = 'USA';
    """),
    ("Count the number of applicants with a status of 'pending'", """
    SELECT COUNT(*)
    FROM applicants
    WHERE "status" = 'pending';
    """),
    ("Find the applicant with the highest salary expectation", """
    SELECT "applicantid", "applicant_name", "salary"
    FROM applicants
    ORDER BY "salary" DESC
    LIMIT 1;
    """),

    ("List all applicants who applied in October 2018 ","""
     SELECT "applicantid", "applicant_name", "application_date"
FROM applicants
WHERE "application_date" BETWEEN '2018-10-01' AND '2018-10-31';
     """),

    (" Calculate the average expected salary of applicants","""
     SELECT AVG("salary") AS avg_salary
FROM applicants;"""),

    ("Find all applicants recruited by a specific recruiter (e.g., Sheldon Cooper)","""
     SELECT "applicantid", "applicant_name", "recruiter"
FROM applicants
WHERE "recruiter" = 'Sheldon Cooper';"""),

    ("List applicants currently in the 'interview' stage ","""
     SELECT "applicantid", "applicant_name", "stage"
FROM applicants
WHERE "stage" = 'interview';"""),

    (" Identify applicants who applied for a specific position (e.g., 1001)","""
     SELECT "applicantid", "applicant_name", "position"
FROM applicants
WHERE "position" = '1001';"""),

    (" Retrieve the most recent applications","""
     SELECT "applicantid", "applicant_name", "application_date"
FROM applicants
ORDER BY "application_date" DESC
LIMIT 10;"""),

    (" Calculate the total number of applicants","""
     SELECT COUNT(*)
FROM applicants;"""),

   
    # Add other queries here...
]

documentation2 = """
The applicants table stores information about job applicants including details about the position applied for, application date, current stage of the application process, status, recruiter, country, applicant name, and salary expectation. Below is the detailed documentation for each column in the table.
"""

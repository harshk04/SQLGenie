# # training_data.py

# training_data.py

ddl_departments= """
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL
);
"""

ddl_students = """
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    department_id INT REFERENCES departments(department_id)
);
"""

ddl_professors="""
CREATE TABLE professors (
    professor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    department_id INT REFERENCES departments(department_id)
);
"""
ddl_courses="""
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    department_id INT REFERENCES departments(department_id),
    professor_id INT REFERENCES professors(professor_id)
);"""

ddl_enrollments="""
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    enrollment_date DATE NOT NULL
);
"""

# documentation = [("""
# The applicants table stores information about job applicants including details about the position applied for, application date, current stage of the application process, status, recruiter, country, applicant name, and salary expectation. Below is the detailed documentation for each column in the table.
# """)
# ]

queries = [
    ("Find all courses a student is enrolled in", """
    SELECT s.first_name, s.last_name, c.course_name
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    WHERE s.student_id = 1;

    """),
    ("List all students in a particular course", """
    SELECT c.course_name, s.first_name, s.last_name
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    JOIN students s ON e.student_id = s.student_id
    WHERE c.course_id = 1;

    """),
    ("Get the department and professor for a specific course:", """
    SELECT c.course_name, d.department_name, p.first_name, p.last_name
    FROM courses c
    JOIN departments d ON c.department_id = d.department_id
    JOIN professors p ON c.professor_id = p.professor_id
    WHERE c.course_id = 1;

    """),
    
    ("List all courses offered by a specific department: ", """
   SELECT d.department_name, c.course_name
    FROM departments d
    JOIN courses c ON d.department_id = c.department_id
    WHERE d.department_id = 1;

    """),

    ("Find all professors in a specific department:", """
    SELECT d.department_name, p.first_name, p.last_name
    FROM departments d
    JOIN professors p ON d.department_id = p.department_id
    WHERE d.department_id = 1;

     """),

    ("Find the email addresses of all students enrolled in a particular course:", """
     SELECT s.email
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    WHERE c.course_name = 'Algorithms';

        """),
    ("List all courses taught by a particular professor:", """
     SELECT p.first_name, p.last_name, c.course_name
    FROM professors p
    JOIN courses c ON p.professor_id = c.professor_id
    WHERE p.first_name = 'Alan' AND p.last_name = 'Turing';

        """),
    ("Find all students and their respective departments:", """
     SELECT s.first_name, s.last_name, d.department_name
    FROM students s
    JOIN departments d ON s.department_id = d.department_id;

        """),
    ("List all students along with the courses they are enrolled in and the professors teaching those courses:", """
     SELECT s.first_name AS student_first_name, s.last_name AS student_last_name, 
       c.course_name, p.first_name AS professor_first_name, p.last_name AS professor_last_name
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    JOIN professors p ON c.professor_id = p.professor_id;

        """),
    ("Get the number of students enrolled in each course:", """
    SELECT c.course_name, COUNT(e.student_id) AS number_of_students
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    GROUP BY c.course_name;

     """),

        ("Find courses that are offered by a specific department and taught by a specific professor", """
    SELECT c.course_name
FROM courses c
JOIN departments d ON c.department_id = d.department_id
JOIN professors p ON c.professor_id = p.professor_id
WHERE d.department_name = 'Computer Science' AND p.first_name = 'Alan' AND p.last_name = 'Turing';


     """),
         ("List all departments and the number of professors in each:", """
    SELECT d.department_name, COUNT(p.professor_id) AS number_of_professors
FROM departments d
JOIN professors p ON d.department_id = p.department_id
GROUP BY d.department_name;


     """),
         ("Get the number of students enrolled in each course:", """
    SELECT c.course_name, COUNT(e.student_id) AS number_of_students
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    GROUP BY c.course_name;

     """),
         ("Get the number of students enrolled in each course:", """
    SELECT c.course_name, COUNT(e.student_id) AS number_of_students
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    GROUP BY c.course_name;

     """),
         ("Get the number of students enrolled in each course:", """
    SELECT c.course_name, COUNT(e.student_id) AS number_of_students
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    GROUP BY c.course_name;

     """),

    
]

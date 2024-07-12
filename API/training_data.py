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

     ("Find the total number of students in each department:", """
    SELECT d.department_name, COUNT(s.student_id) AS total_students
    FROM departments d
    JOIN students s ON d.department_id = s.department_id
    GROUP BY d.department_name;
    """),

    ("List all professors and the courses they teach, along with the department they belong to:", """
    SELECT p.first_name AS professor_first_name, p.last_name AS professor_last_name, 
           c.course_name, d.department_name
    FROM professors p
    JOIN courses c ON p.professor_id = c.professor_id
    JOIN departments d ON p.department_id = d.department_id;
    """),

    ("Get the average number of students enrolled per course in each department:", """
    SELECT d.department_name, AVG(course_enrollment) AS avg_students_per_course
    FROM (
        SELECT c.department_id, COUNT(e.student_id) AS course_enrollment
        FROM courses c
        LEFT JOIN enrollments e ON c.course_id = e.course_id
        GROUP BY c.course_id
    ) AS dept_courses
    JOIN departments d ON dept_courses.department_id = d.department_id
    GROUP BY d.department_name;
    """),

    ("Find students who are enrolled in more than 2 courses:", """
    SELECT s.first_name, s.last_name, COUNT(e.course_id) AS course_count
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    GROUP BY s.student_id
    HAVING COUNT(e.course_id) > 2;
    """),

    ("Get the details of students who are not enrolled in any course:", """
    SELECT s.first_name, s.last_name, s.email
    FROM students s
    LEFT JOIN enrollments e ON s.student_id = e.student_id
    WHERE e.course_id IS NULL;
    """),

    ("Find courses taught by professors from other departments:", """
    SELECT c.course_name, p.first_name, p.last_name, d1.department_name AS course_department, d2.department_name AS professor_department
    FROM courses c
    JOIN professors p ON c.professor_id = p.professor_id
    JOIN departments d1 ON c.department_id = d1.department_id
    JOIN departments d2 ON p.department_id = d2.department_id
    WHERE c.department_id <> p.department_id;
    """),

    ("List all students who share the same last name as any professor:", """
    SELECT DISTINCT s.first_name, s.last_name
    FROM students s
    JOIN professors p ON s.last_name = p.last_name;
    """),

    ("Get the total number of courses each professor teaches:", """
    SELECT p.first_name, p.last_name, COUNT(c.course_id) AS total_courses
    FROM professors p
    JOIN courses c ON p.professor_id = c.professor_id
    GROUP BY p.professor_id;
    """),

    ("Find professors who teach more than one course in the same department:", """
    SELECT p.first_name, p.last_name, d.department_name, COUNT(c.course_id) AS course_count
    FROM professors p
    JOIN courses c ON p.professor_id = c.professor_id
    JOIN departments d ON c.department_id = d.department_id
    WHERE p.department_id = d.department_id
    GROUP BY p.professor_id, d.department_name
    HAVING COUNT(c.course_id) > 1;
    """),

    ("List students who are enrolled in courses from different departments:", """
    SELECT s.first_name, s.last_name, COUNT(DISTINCT c.department_id) AS dept_count
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    GROUP BY s.student_id
    HAVING COUNT(DISTINCT c.department_id) > 1;
    """),

    ("Find the department with the highest number of enrolled students:", """
    SELECT d.department_name
    FROM departments d
    JOIN students s ON d.department_id = s.department_id
    GROUP BY d.department_name
    ORDER BY COUNT(s.student_id) DESC
    LIMIT 1;
    """),

    ("Get the names of students who are enrolled in all courses taught by a specific professor:", """
    SELECT s.first_name, s.last_name
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    JOIN professors p ON c.professor_id = p.professor_id
    WHERE p.first_name = 'Alan' AND p.last_name = 'Turing'
    GROUP BY s.student_id
    HAVING COUNT(e.course_id) = (SELECT COUNT(course_id) FROM courses WHERE professor_id = p.professor_id);
    """),

    ("Find the course with the highest average enrollment duration:", """
    SELECT c.course_name, AVG(CURRENT_DATE - e.enrollment_date) AS avg_duration
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    GROUP BY c.course_name
    ORDER BY avg_duration DESC
    LIMIT 1;
    """),

    ("List students who have the same first and last names as any professor:", """
    SELECT DISTINCT s.first_name, s.last_name
    FROM students s
    JOIN professors p ON s.first_name = p.first_name AND s.last_name = p.last_name;
    """),

    ("Get the average number of courses per student in each department:", """
    SELECT d.department_name, AVG(course_count) AS avg_courses_per_student
    FROM (
        SELECT s.department_id, COUNT(e.course_id) AS course_count
        FROM students s
        LEFT JOIN enrollments e ON s.student_id = e.student_id
        GROUP BY s.student_id
    ) AS student_courses
    JOIN departments d ON student_courses.department_id = d.department_id
    GROUP BY d.department_name;
    """),

    ("Find students who have never enrolled in courses taught by professors from their own department:", """
    SELECT s.first_name, s.last_name
    FROM students s
    WHERE NOT EXISTS (
        SELECT 1
        FROM enrollments e
        JOIN courses c ON e.course_id = c.course_id
        JOIN professors p ON c.professor_id = p.professor_id
        WHERE e.student_id = s.student_id AND p.department_id = s.department_id
    );
    """),

    ("List courses with the same name but different professors:", """
    SELECT c.course_name, p1.first_name AS professor1_first_name, p1.last_name AS professor1_last_name,
           p2.first_name AS professor2_first_name, p2.last_name AS professor2_last_name
    FROM courses c
    JOIN professors p1 ON c.professor_id = p1.professor_id
    JOIN professors p2 ON c.professor_id = p2.professor_id AND p1.professor_id <> p2.professor_id
    WHERE c.course_name IN (
        SELECT course_name
        FROM courses
        GROUP BY course_name
        HAVING COUNT(DISTINCT professor_id) > 1
    )
    ORDER BY c.course_name;
    """),

    ("Get the number of unique courses each student is enrolled in:", """
    SELECT s.first_name, s.last_name, COUNT(DISTINCT e.course_id) AS unique_courses
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    GROUP BY s.student_id;
    """),

    ("Find departments with more professors than students:", """
    SELECT d.department_name, COUNT(p.professor_id) AS professor_count, COUNT(s.student_id) AS student_count
    FROM departments d
    LEFT JOIN professors p ON d.department_id = p.department_id
    LEFT JOIN students s ON d.department_id = s.department_id
    GROUP BY d.department_name
    HAVING COUNT(p.professor_id) > COUNT(s.student_id);
    """),

    ("List all students who have enrolled in at least one course and their enrollment dates:", """
    SELECT s.first_name, s.last_name, e.enrollment_date
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    ORDER BY s.last_name, s.first_name, e.enrollment_date;
    """)


]

documentation = [
    ("""
    The departments table stores information about the different departments within the institution. Below is the detailed documentation for each column in the table:
    - department_id: An auto-incremented integer serving as the primary key for the table.
    - department_name: A string representing the name of the department. This field cannot be null.
    """),

    ("""
    The students table stores information about the students enrolled in the institution. Below is the detailed documentation for each column in the table:
    - student_id: An auto-incremented integer serving as the primary key for the table.
    - first_name: A string representing the first name of the student. This field cannot be null.
    - last_name: A string representing the last name of the student. This field cannot be null.
    - email: A unique string representing the email address of the student. This field cannot be null.
    - department_id: An integer referencing the department_id in the departments table, indicating the department the student belongs to.
    """),

    ("""
    The professors table stores information about the professors in the institution. Below is the detailed documentation for each column in the table:
    - professor_id: An auto-incremented integer serving as the primary key for the table.
    - first_name: A string representing the first name of the professor. This field cannot be null.
    - last_name: A string representing the last name of the professor. This field cannot be null.
    - email: A unique string representing the email address of the professor. This field cannot be null.
    - department_id: An integer referencing the department_id in the departments table, indicating the department the professor belongs to.
    """),

    ("""
    The courses table stores information about the courses offered by the institution. Below is the detailed documentation for each column in the table:
    - course_id: An auto-incremented integer serving as the primary key for the table.
    - course_name: A string representing the name of the course. This field cannot be null.
    - department_id: An integer referencing the department_id in the departments table, indicating the department offering the course.
    - professor_id: An integer referencing the professor_id in the professors table, indicating the professor teaching the course.
    """),

    ("""
    The enrollments table stores information about the students' enrollment in courses. Below is the detailed documentation for each column in the table:
    - enrollment_id: An auto-incremented integer serving as the primary key for the table.
    - student_id: An integer referencing the student_id in the students table, indicating the student enrolled in the course.
    - course_id: An integer referencing the course_id in the courses table, indicating the course the student is enrolled in.
    - enrollment_date: A date indicating when the student was enrolled in the course. This field cannot be null.
    """)
]

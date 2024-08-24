-- Create table for Grades
CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY,
    grade_level INT NOT NULL CHECK (grade_level BETWEEN 1 AND 6)
);

-- Create table for Classes
CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY,
    grade_id INT NOT NULL,
    class_name VARCHAR(10) NOT NULL,
    homeroom_teacher_id INT,
    FOREIGN KEY (grade_id) REFERENCES Grades (grade_id),
    FOREIGN KEY (homeroom_teacher_id) REFERENCES Teachers (teacher_id)
);

-- Create table for Students
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    class_id INT NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (class_id) REFERENCES Classes (class_id)
);

-- Create table for Teachers
CREATE TABLE Teachers (
    teacher_id SERIAL PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL
);

-- Create table for Subjects
CREATE TABLE Subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL
);

-- Create table for Teacher_Subjects (many-to-many relationship)
CREATE TABLE Teacher_Subjects (
    teacher_id INT NOT NULL,
    subject_id INT NOT NULL,
    PRIMARY KEY (teacher_id, subject_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers (teacher_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects (subject_id)
);

-- Insert predefined subjects
INSERT INTO Subjects (subject_name) VALUES
('수학'), ('국어'), ('영어'), ('체육'), ('음악'), ('과학'), ('사회'), ('도덕');
import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.create_tables()

    def create_connection(self):
        """Create a database connection to the SQLite database"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print("Connection Error:", e)
        return conn

    def create_tables(self):
        """Create tables for the SIS"""
        conn = self.create_connection()
        try:
            if conn:
                cursor = conn.cursor()

                cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                    student_id INTEGER PRIMARY KEY,
                                    first_name TEXT,
                                    last_name TEXT,
                                    date_of_birth TEXT,
                                    email TEXT,
                                    phone_number TEXT)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                                    course_id INTEGER PRIMARY KEY,
                                    course_name TEXT,
                                    course_code TEXT,
                                    instructor_name TEXT)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS enrollments (
                                    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    student_id INTEGER,
                                    course_id INTEGER,
                                    enrollment_date TEXT,
                                    FOREIGN KEY (student_id) REFERENCES students (student_id),
                                    FOREIGN KEY (course_id) REFERENCES courses (course_id))''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                                    teacher_id INTEGER PRIMARY KEY,
                                    first_name TEXT,
                                    last_name TEXT,
                                    email TEXT,
                                    expertise TEXT)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                                    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    student_id INTEGER,
                                    amount REAL,
                                    payment_date TEXT,
                                    FOREIGN KEY (student_id) REFERENCES students (student_id))''')

                conn.commit()
        except Error as e:
            print("Table Creation Error:", e)
        finally:
            if conn:
                conn.close()

    def insert_student(self, student):
        conn = self.create_connection()
        try:
            if conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO students (student_id, first_name, last_name, date_of_birth, email, phone_number)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                               (student.student_id, student.first_name, student.last_name, student.date_of_birth, student.email, student.phone_number))
                conn.commit()
        except Error as e:
            print("Error inserting student:", e)
        finally:
            if conn:
                conn.close()

    def insert_course(self, course):
        conn = self.create_connection()
        try:
            if conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO courses (course_id, course_name, course_code, instructor_name)
                                  VALUES (?, ?, ?, ?)''',
                               (course.course_id, course.course_name, course.course_code, course.instructor_name))
                conn.commit()
        except Error as e:
            print("Error inserting course:", e)
        finally:
            if conn:
                conn.close()

    def insert_teacher(self, teacher):
        conn = self.create_connection()
        try:
            if conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO teachers (teacher_id, first_name, last_name, email, expertise)
                                  VALUES (?, ?, ?, ?, ?)''',
                               (teacher.teacher_id, teacher.first_name, teacher.last_name, teacher.email, teacher.expertise))
                conn.commit()
        except Error as e:
            print("Error inserting teacher:", e)
        finally:
            if conn:
                conn.close()

    def insert_enrollment(self, student_id, course_id, enrollment_date):
        conn = self.create_connection()
        try:
            if conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO enrollments (student_id, course_id, enrollment_date)
                    VALUES (?, ?, ?)
                ''', (student_id, course_id, enrollment_date))
                conn.commit()
        except Error as e:
            print("Error inserting enrollment:", e)
        finally:
            if conn:
                conn.close()

    def insert_payments(self, student_id, amount, payment_date):
        conn = self.create_connection()
        try:
            if conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO payments (student_id, amount, payment_date)
                    VALUES (?, ?, ?)
                ''', (student_id, amount, payment_date))
                conn.commit()
                print("Payment recorded successfully.")
        except Error as e:
            print("Error inserting payment:", e)
        finally:
            if conn:
                conn.close()



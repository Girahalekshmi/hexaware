from dao.DatabaseManager import DatabaseManager
from entity.student import Student
from entity.Course import Course
from entity.Teacher import Teacher
from entity.Enrollment import Enrollment
from entity.Payment import Payment

class SIS:
    def __init__(self, db_file):
        self.db_file = db_file
        self.db_manager = DatabaseManager(db_file)
        self.db_manager.create_tables()

        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []

    def enroll_student_in_course(self, student, course):
        student.enroll_in_course(course)
        course.get_enrollments().append(student)
        self.enrollments.append((student, course))

    def assign_teacher_to_course(self, teacher, course):
        course.assign_teacher(teacher)
        teacher.get_assigned_courses().append(course)

    def record_payment(self, student, amount, payment_date):
        student.make_payment(amount, payment_date)
        self.payments.append((student, amount, payment_date))

    def generate_enrollment_report(self, course):
        print(f"Enrollment Report for Course: {course._course_name}")
        for student in course.get_enrollments():
            print(f"- {student.get_full_name()} ({student._student_id})")

    def generate_payment_report(self, student):
        print(f"Payment Report for Student: {student.get_full_name()}")
        for amount, date in student.get_payment_history():
            print(f"- Amount: ₹{amount}, Date: {date}")

    def calculate_course_statistics(self, course):
        enrolled_students = course.get_enrollments()
        total_enrollments = len(enrolled_students)
        total_payments = 0
        for student in enrolled_students:
            for amount, _ in student.get_payment_history():
                total_payments += amount
        print(f"Statistics for {course._course_name}")
        print(f"- Total Enrollments: {total_enrollments}")
        print(f"- Total Payments: ₹{total_payments}")

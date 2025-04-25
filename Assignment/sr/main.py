from service.SIS import SIS
from entity.student import Student
from entity.Course import Course
from entity.Teacher import Teacher
from datetime import date
from datetime import datetime

def main():
    # Initialize SIS system with database file
    sis_system = SIS('student.db')

    # Create student, course, and teacher instances
    student = Student(4, "neelakendan", "A", "2003-05-21", "giraha@example.com", "0987654432")
    course = Course(104, "project management", "CS201", "Dr. kala")
    teacher = Teacher(4, "Dr. kala", "N", "dr.kala@example.com", "project management")

    # Ensure the database and tables are created
    sis_system.db_manager.create_tables()

    # Insert student, course, and teacher into the database
    sis_system.db_manager.insert_student(student)
    sis_system.db_manager.insert_course(course)
    sis_system.db_manager.insert_teacher(teacher)
    amount = 500.00
    payment_date = datetime.now().strftime("%Y-%m-%d")
    # Enroll student in course (in memory)
    sis_system.enroll_student_in_course(student, course)

    # Save enrollment to the database
    enrollment_date = date.today().isoformat()
    sis_system.db_manager.insert_enrollment(student.student_id, course.course_id, enrollment_date)
    sis_system.db_manager.insert_payments(student.student_id, amount, payment_date)

    # Assign teacher to course (in memory)
    sis_system.assign_teacher_to_course(teacher, course)

    # Print confirmation
    print("Student created:", student.first_name, student.last_name)
    print("Course created:", course.course_name)
    print("Teacher created:", teacher.first_name, teacher.last_name)

    print("Students enrolled in", course.course_name)
    for student in course.get_enrollments():
        print(f"- {student.first_name} {student.last_name} (Student ID: {student.student_id})")


if __name__ == "__main__":
    main()

#this is a sample code



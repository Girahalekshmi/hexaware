class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student is already enrolled in the course."):
        super().__init__(message)


class CourseNotFoundException(Exception):
    def __init__(self, message="Course not found."):
        super().__init__(message)


class StudentNotFoundException(Exception):
    def __init__(self, message="Student not found."):
        super().__init__(message)


class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher not found."):
        super().__init__(message)


class PaymentValidationException(Exception):
    def __init__(self, message="Invalid payment details."):
        super().__init__(message)


class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid data for student."):
        super().__init__(message)


class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid data for course."):
        super().__init__(message)


class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid data for enrollment."):
        super().__init__(message)


class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid data for teacher."):
        super().__init__(message)


class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for course enrollment."):
        super().__init__(message)



class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []  # List of Enrollment objects
        self.payments = []     # List of Payment objects

    def enroll_in_course(self, course):
        self.enrollments.append(course)

    def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def make_payment(self, amount, payment_date):
        self.payments.append(Payment(None, self, amount, payment_date))

    def display_student_info(self):
        print(f"ID: {self.student_id}, Name: {self.first_name} {self.last_name}, DOB: {self.date_of_birth}, Email: {self.email}, Phone: {self.phone_number}")

    def get_enrolled_courses(self):
        return self.enrollments

    def get_payment_history(self):
        return self.payments


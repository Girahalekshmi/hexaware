class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []
        self.teacher = None

    def assign_teacher(self, teacher):
        self.teacher = teacher
        teacher.assigned_courses.append(self)

    def update_course_info(self, course_code, course_name, instructor_name):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor_name

    def display_course_info(self):
        print(f"Course ID: {self.course_id}, Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor_name}")

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.teacher

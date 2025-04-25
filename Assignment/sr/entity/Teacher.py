class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email, expertise):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.expertise = expertise
        self.assigned_courses = []  # List of Course objects

    def update_teacher_info(self, name, email, expertise):
        name_parts = name.split(" ", 1)
        self.first_name = name_parts[0]
        self.last_name = name_parts[1] if len(name_parts) > 1 else ""
        self.email = email
        self.expertise = expertise

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Expertise: {self.expertise}")

    def get_assigned_courses(self):
        return self.assigned_courses

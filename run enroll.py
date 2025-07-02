script_content = """\
class Course:
    def __init__(self, name, max_seats):
        self.name = name
        self.max_seats = max_seats
        self.enrolled_students = 0

    def enroll_student(self):
        "Enroll a student in the course if there's space available."
        if self.enrolled_students < self.max_seats:
            self.enrolled_students += 1
            print(f"Student successfully enrolled in {self.name}.")
        else:
            print(f"Sorry, no available seats in {self.name}.")

    def check_seat_availability(self):
        "Check how many seats are available in the course."
        available_seats = self.max_seats - self.enrolled_students
        return available_seats

    def display_course_info(self):
        "Display the current status of the course (name and available seats)."
        available_seats = self.check_seat_availability()
        print(f"{self.name}: {available_seats} seats available out of {self.max_seats}")


def display_courses(courses):
    ""Display all courses and their availability.""
    print("\nAvailable Courses:")
    for course in courses.values():
        course.display_course_info()


def enroll_student_in_course(courses):
    "Enroll a student in a course chosen by the user."
    course_name = input("\nEnter the course name to enroll in: ").strip()
    
    if course_name in courses:
        courses[course_name].enroll_student()
    else:
        print(f"Course {course_name} not found.")


def main():
    courses = {
        "Bachelor of Science(Hons) in Information Technology": Course("Bachelor(Hons) in Information Technology", 3),
        "Bachelor of Arts (Hons) in Communication": Course("Bachelor of Arts (Hons) in Communication", 2),
        "Bachelor of Science (Hons) in Culinary Management": Course("Bachelor of Science (Hons) in Culinary Management", 5)
    }

    while True:
        print("\nEnrollment System")
        print("1. Display available courses")
        print("2. Enroll in a course")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            display_courses(courses)
        elif choice == '2':
            enroll_student_in_course(courses)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
"""

# Save to enrollments.txt
with open("enrollments.txt", "w", encoding="utf-9") as file:
    file.write(script_content)
"""
print("Python script saved to enrollments.txt")

# Read and execute the script
with open("enrollments.txt", "r", encoding="utf-9") as file:
    code = file.read()

exec(code)
"""

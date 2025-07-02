def add_student():
    print('Student Registration')
    
    # Validate Student Name
    name = input('Enter Student Name: ').strip().upper()
    while not name:
        print('ERROR! Please repeat again.')
        name = input('Enter Student Name: ').strip().upper()
        
    # Validate Student ID (kept as a string to allow alphanumeric IDs)
    student_id = input('Enter Student ID: ').strip().upper()
    
    while not student_id:
        print('ERROR! Please repeat again.')
        student_id = input('Enter Student ID: ').strip().upper()
        
        # Check if student ID already exists
    try:
         with open('students.txt', 'r') as file:
            students = file.readlines()
            
            student_exists = False
            for student in students:
                # Use comma split (no spaces)
                student_details = student.strip().split(',')

                # Ensure the ID exists in the line
                if len(student_details) >= 1:
                    existing_student_id = student_details[0].strip()
                    
                    if student_id == existing_student_id:
                        print("ERROR! This Student ID already exists. Please enter a unique ID.")
                        student_exists = True
                        # No need to check further
                        break 

            if student_exists:
                return  # Ask for input again
            
    except FileNotFoundError:
        pass  # No file means no students exist yet

        
    # Validate Contact Number (kept as a string to support country codes)
    contact_number = input('Enter Contact Number: ').strip()
    while not contact_number.isdigit():
        print('ERROR! Please repeat again.')
        contact_number = input('Enter Contact Number: ').strip()
        
    # Save Data to File
    try:
        with open('students.txt', 'a') as file: 
            file.write(f'{student_id},{name},{contact_number}\n')
        print('Student registered successfully!')
    except Exception as e:
        print(f'Error saving student details: {e}')
        
#add new course
def add_course():
    import re
    while True:
        new_course = input("Enter New Course: ").strip().upper()
        if not new_course:
            print("There is an error in New Course, please try again.")
        else:
            break
#add couse id
    while True:
        course_id = input("Enter Course ID: ").strip().upper()
        if not course_id:
            print("There is an error in Course ID, please try again.")
        else:
            break
# add maximum seat        
    while True:
        try:
            max_seat = int(input("Enter Maximum Seat for this course: "))
            if max_seat <= 0:
                print("Maximum seat must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input for maximum seats. Please enter a valid integer.")

#Check if the courses file exists, and read its contents if it does      
    try:
        with open('courses.txt', 'r') as file:
            courses = file.readlines()
        
        for course in courses:
             # Use comma-space split
            course_details = course.strip().split(', ')  

            # make sure at least course name and ID exist 
            if len(course_details) >= 2:  
                existing_course_name = course_details[0].strip()
                existing_course_id = course_details[1].strip()
                
                if new_course == existing_course_name or course_id == existing_course_id:
                    print("The course name or course ID already exists.")
                    return

    except FileNotFoundError:
        print("No existing courses file found. You can add a new course.")

#save data to file
    try:
        with open('courses.txt', 'a') as file:
            file.write(f'{new_course}, {course_id}, {max_seat}\n')
            print('Course added successfully!')
    except IOError as e:
        print(f'Error saving course details: {e}')

        
#Function to enroll a student in a course
def enrol_course():
    print("Enrol course")
    student_id = input("Enter Student ID: ").strip()
    student_data = {}
    
    try:
        #check if the student file exists, and read its contents if it does      
        with open("students.txt","r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts)>=3:
                    sid, name, contact = parts[0], parts[1], parts[2]
                    enrolled_courses = parts[3:] if len(parts) > 3 else []
                    student_data[sid] = (name, contact, enrolled_courses)

        #Validate if student exists
        if student_id not in student_data:
            print("Sorry. Student ID does not exist.")
            return
        
        print("Available courses: ")
        print(" Course Name | Course ID | Max Seats  | Remaining Seats ")
        print("-------------------------------------------------------")

        #Read available courses from the courses.txt file
        courses_data = []
        with open("courses.txt","r")as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >=3:
                    course_name, course_id, max_seats = parts[:3]
                    remaining_seats = int(parts[3]) if len(parts) > 3 and parts[3].strip().isdigit() else int(max_seats)
                    courses_data.append((course_name.strip(), course_id.strip(), int(max_seats), remaining_seats))

            #Display available courses
            for course_name, course_id, max_seats, remaining_seats in courses_data:
                print(f"{course_name:<12} | {course_id:<9} | {max_seats:<10} | {remaining_seats:<15}")

            #Prompt user to enter the Course ID to enroll in
            course_id = input("Please enter the Course ID to be enroled: ").strip().upper()
            found = False
            updated_lines = []
            enrolled_students = 0

            #Read courses.txt and updater the remaining seats
            with open("courses.txt","r")as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        course_names = parts[0].strip()
                        course_ids = parts[1].strip()
                        max_seats = int(parts[2].strip())
                        remaining_seat = int(parts[3]) if len(parts) > 3 and parts[3].strip().isdigit() else int(max_seats)

                        #If course ID matches, check seat availability
                        if course_ids.strip() == course_id.strip():
                            found = True
                            if remaining_seat > 0:
                                remaining_seat -=1
                                enrolled_students = max_seats - remaining_seat
                                print(f"Student successfully enrolled in {course_id}.")
                            else:
                                print(f"Sorry, no available seats in {course_id}.")
                        updated_line = f"{course_names},{course_ids},{max_seats},{remaining_seat}"
                    else:
                        updated_line = line.strip()

                    updated_lines.append(updated_line)

            #Write updated course data back to courses.txt
            with open("courses.txt","w") as file:
                file.write("\n".join(updated_lines)+"\n")
                
            if not found:
                print("Sorry. Course ID does not exist.")
                return
            
            #Update student record to include enrolled course
            updated_student_lines = []
            with open("students.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) < 3:
                        continue
                    sid, name, contact = parts[0], parts[1], parts[2]
                    enrolled_courses = parts[3:] if len(parts) > 3 else []
                    
                    if sid == student_id:
                        if course_id not in enrolled_courses:
                            enrolled_courses.append(course_id)
                    updated_line = f"{sid},{name},{contact},{','.join(enrolled_courses)}"
                    updated_student_lines.append(updated_line)

            #Write updated student data back to students.txt
            with open("students.txt", "w") as file:
                file.write("\n".join(updated_student_lines) + "\n")

        # Save enrollment details to enrollments.txt
        try:
            with open('enrollments.txt', 'a') as file:
                file.write(f'{student_id},{course_id},{course_name},{enrolled_students}/{max_seats},{remaining_seats}\n')
            print("Student enrollment successfully updated!")
        except Exception as e:
            print(f"Error saving student enrollment details:{e}")
    except FileNotFoundError:
        print("ERROR! File not found. Please check the file path!")

    return

#Function to drop a student in a course
def drop_course():
    print("Drop course")
    student_id = input("Enter Student ID: ").strip()
    try:
        #open enrollments.txt and read all lines
        with open("enrollments.txt","r") as file:
            enrollments = file.readlines()

        #Filter courses for the student ID
        student_enrollments = [e.strip() for e in enrollments if student_id == e.split(",")[0].strip()]

        #If the student is not enrolled in any courses, return
        if not student_enrollments:
            print("Sorry. Student ID is not enrolled in any course.")
            return

        #Display all enrolled courses for the student
        print("\nEnrolled Courses： ")
        for enrollment in student_enrollments:
            enrollment_details = enrollment.strip().split(",")
            if len(enrollment_details) >= 3:
                s_id = enrollment_details[0].strip()
                c_id = enrollment_details[1].strip()
                c_name = enrollment_details[2].strip()
                print(f"Student ID: {s_id} | Course Name: {c_name} | Course ID: {c_id}")

        #Ask the user for the course ID to drop
        course_id = input("Please enter the Course ID to be dropped: ").strip()

        #Remove the dropped course from enrollments.txt
        updated_enrollments = [e for e in enrollments if not (student_id in e and course_id in e)]
        with open("enrollments.txt","w") as file:
                    file.writelines(updated_enrollments)

        #Update courses.txt by increasing remaining seats for the dropped course
        courses_data = []
        with open("courses.txt","r")as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 4 and parts[1].strip() == course_id:
                    course_name, course_code, max_seats, remaining_seats = parts[0], parts[1], int(parts[2]), int(parts[3])
                    remaining_seats = int(parts[3])+1
                    courses_data.append(f"{course_name},{course_code},{max_seats},{remaining_seats}\n")
                else:
                    courses_data.append(line)
                    
        #Save the updated course information back to courses.txt
        with open("courses.txt","w") as file:
            file.writelines(courses_data)

        #Update students.txt to remove the dropped course from the student's enrolled list
        updated_students = []           
        with open("students.txt","r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    sid, name, contact = parts[0], parts[1], parts[2]
                    enrolled_courses = parts[3:] if len(parts) > 3 else []
                    
                    if sid.strip() == student_id:
                        #Remove the dropped course from the student's list
                        enrolled_courses = [c for c in enrolled_courses if c != course_id]
                        if enrolled_courses:
                            new_line = f"{sid},{name},{contact},{','.join(enrolled_courses)}"
                        else:
                            new_line = f"{sid},{name},{contact}"

                    else:
                        new_line = line.strip()

                    updated_students.append(new_line)

        #Save the updated student records back to students.txt
        with open("students.txt", "w") as file:
            file.write("\n".join(updated_students)+"\n")

        print("Course dropped successfully!")
        
    except FileNotFoundError:
        print("ERROR! File not found. Please check the file path！")


#Function to view available courses
def view_course():
    try:
        #Open the courses file in read mode
        with open("courses.txt","r") as file:
            courses = file.readlines()
            
        #Check if the file is empty
        if not courses:
            print("NO courses available yet!")
            return
        
        print("Available Courses:")
        for course in courses:
            #Strip whitespace and split course details
            course_details = course.strip().split(",")

            #Ensure there are at least 3 elements (name,ID, max seats)
            if len(course_details)>=3:
                course_name = course_details[0].strip()
                course_id = course_details[1].strip()
                max_seats = course_details[2].strip()

                #Handle optional remaining seats, defaulting to max seats
                remaining_seats = course_details[3].strip() if len(course_details) > 3 else "max_seats"

                #Display formatted course information
                print(f"Course Name: {course_name}|Course ID: {course_id}|Max_seats: {max_seats}|Remaining Seats: {remaining_seats}")

    except FileNotFoundError:
        print("Courses file not found.")#Handle case where file does not exist
        
#Function to view student information
def view_student_info():
    try:
        #Open student file in read mode
        with open("students.txt","r") as file:
            students = file.readlines()
        #Check if the file is empty
        if not students:
            print("No students available yet!")
            return
        
        print("Student Information: ")
        for student in students:
            #Strip whitespace and split student details
            student_details = student.strip().split(",")

            #Ensure there are at least 3 elements (ID,name,contact)
            if len(student_details)>=3:
                student_id = student_details[0].strip()
                student_name = student_details[1].strip()
                contact = student_details[2].strip()

                #Handle optional course field, defaulting to "No Course"
                course = student_details[3].strip()if len(student_details) > 3 else "No Course"

                #Display formatted student information
                print(f"ID: {student_id} | Name:{student_name} | Contact:{contact} | Course ID:{course}")

    except FileNotFoundError:
        print("Student file not found")#Handle case where file does not exist
        
#Function to display main menu
def main_program():
    while True:
        #Display menu option
        print("MENU:\n[1] Add a new student\n[2]Add a new course\n[3]Enrol in a course \n[4]Drop a course\n[5]View available courses\n[6]View student information\n[7]Exit")

        #Get user choice
        choice = input("Enter a number: ")

        #Perform actions based on user input
        if choice == "1":
            add_student() #Call function to add student
        elif choice == "2":
            add_course() #Call function to add course
        elif choice == "3":
            enrol_course() #Call function to enroll a course
        elif choice == "4":
            drop_course() #Call function to drop a course
        elif choice == "5":
            view_course() #Call function to view course
        elif choice == "6":
            view_student_info() #Call function to view student info
        elif choice == "7":
            print("Exiting program.")
            break #Exit Loop
        
        else:
            print("ERROR! Please enter a valid number.") #Handle invalid input

#Run to main program
main_program()

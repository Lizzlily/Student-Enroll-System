print('Student Registration')

# Validate Student Name
name = input('Enter Student Name: ').strip()
while not name:
    print('Student name cannot be empty.')
    name = input('Enter Student Name: ').strip()

# Validate Student ID (kept as a string to allow alphanumeric IDs)
student_id = input('Enter Student ID: ').strip()
while not student_id:
    print('Student ID cannot be empty.')
    student_id = input('Enter Student ID: ').strip()

# Validate Contact Number (kept as a string to support country codes)
contact_number = input('Enter Contact Number: ').strip()
while not contact_number.isdigit():
    print('Contact number must be numeric and cannot be empty.')
    contact_number = input('Enter Contact Number: ').strip()

# Save Data to File
try:
    with open('students.txt', 'a') as file:  # Ensure file name is consistent
        file.write(f'{student_id},{name},{contact_number}\n')
    print(f'{student_id},{name},{contact_number}\n')
    print('Student registered successfully!')
except Exception as e:
    print(f'Error saving student details: {e}')

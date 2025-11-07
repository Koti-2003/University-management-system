#Univesity Management System
from abc import ABC, abstractmethod
class Candidates:
    def __init__(self,name,ID,role):
        self.name = name
        self.ID = ID
        self.role = role

    @abstractmethod
    def get_details(self):
        pass
class Students(Candidates):
    def __init__(self,name,ID,role,course):
        super().__init__(name,ID,role)
        self.course = course

    def get_details(self):
        print(f'Student Details: ')
        print(f'Name: {self.name}')
        print(f'ID: {self.ID}')
        print(f'Role: {self.role}')
        print(f'Course: {self.course}')
        
class Staff(Candidates):
    def __init__(self,name,ID,role,dept):
        super().__init__(name,ID,role)
        self.dept = dept

    def get_details(self):
        print(f'Student Details: ')
        print(f'Name: {self.name}')
        print(f'ID: {self.ID}')
        print(f'Role: {self.role}')
        print(f'DEpartment: {self.dept}')

class University:
    university_name = 'Codegnan'
    location = 'Hyderabad'

    def __init__(self):
        self.student = []
        self.staff = []

    def add_student(self,student):
        self.student.append(student)
        print('Details updated successfully')
        print()

    def add_staff(self, staff):
        self.staff.append(staff)
        print('Details updated successfully')
        print()

    def remove_students(self, student):
        self.student.append(student)
        print('Details updated successfully')
        print()
    def remove_staff(self, staff):
        self.staff.remove(staff)
        print('Details updated')
        print()

    @classmethod
    def university_details(cls):
        print(f'University Name: {cls.university_name}')
        print(f'Location: {cls.location}')

    @staticmethod
    def greet():
        print('Welcome to University Management System')

u = University()
print('-'*40)
u.greet()
print('-'*40)

while True:
    print('Choose your option\n')
    print('1. UNIVERSITY DETAILS')
    print('2. ADD STUDENT')
    print('3. ADD STAFF')
    print('4. REMOVE STUDENT')
    print('5. REMOVE STAFF')
    print('6. CANDIDATES INFO')
    print('7. SEARCH STUDENT BY ID')
    print('8. EXIT')

    ch = int(input('Enter your choice: '))

    if ch == 1:
        u.university_details()
    elif ch == 2:
        name = input('Enter student name: ')
        ID = input('Enter student ID: ')
        role = 'Student'
        course = input('Enter the course: ')
        s = Students(name,ID,role,course)
        u.add_student(s)
    elif ch==3:
        name = input('Enter staff name: ')
        ID = input('Enter staff ID: ')
        role = input('Enter job title: ')
        dept = input('Enter the department: ')
        s = Staff(name, ID, role,dept)
        u.add_staff(s)
    elif ch==4:
        id_num = input('Enter ID to be removed: ')

        for i in u.student:
            if i.ID == id_num:
                u.remove_students(i)
                break
        else:
            print('No details found')
    elif ch == 5:
        id_num = input('Enter ID to be removed: ')

        for i in u.staff:
            if i.ID == id_num:
                u.remove_staff(i)
                break
        else:
            print('No details found')
    elif ch == 6:
        for i in u.student:
            i.get_details()
        for i in u.staff:
            i.get_details()
    elif ch == 7:
        id_num = input('Enter ID: ')
        for i in u.student:
            if i.ID == id_num:
                i.get_details()
        else:
            print('No details found')
    elif ch == 8:
        print('THANK YOU')
        break






















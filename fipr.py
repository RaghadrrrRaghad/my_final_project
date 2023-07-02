import uuid
"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : "Raghad Haniya"
Delivery Date : 22-6-23
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
class Course:
    def __init__(self, name, mark):
        self.course_id = str(uuid.uuid4().int)
        self.course_name = name
        self.course_mark = mark


class Student:
    # TODO 3 define static variable indicates total student count
    student_count = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number):
        self.student_count += 1
        self.student_id = str(uuid.uuid4().int)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []


    # TODO 5 define a method to enroll new course to student courses list
    def enroll_new_course(self, name, mark):
        new_course = Course(name, mark)
        self.courses_list.append(new_course)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for i in self.courses_list:
            print(f"Course : {i.course_name} , Mark : {i.course_mark}")

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        marks = 0
        for i in self.courses_list:
            marks += i.course_mark
        if self.courses_list:
            return marks / len(self.courses_list)
        else:
            return 0


# in Global Scope
# TODO 8 declare empty students list
students_list = []
while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:

        # TODO 10 make sure that Student number is not exists before
        student_number = input("Enter Student Number")
        for i in students_list:
            if student_number == i.student_number:
                print(f'{student_number} is exists')
                break

        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 11 create student object and append it to students list
        new_student = Student(student_name, student_age, student_number)
        students_list.append(new_student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
        x = False
        for i in students_list:
            if i.student_number == student_number:
                students_list.remove(i)
                x = True
                break
        if x:
            print("Student Deleted Successfully")
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses

    else:
        # TODO 16 call a function to exit the program
        pass
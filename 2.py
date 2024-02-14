
# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name, student_id და courses(კურსების სია, რომელშიც სტუდენტი არის ჩარიცხული).
# აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები. შექმენით რამდენიმე ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.

class Student:

    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses

    def showStudentsPersonalInformation(self, name):
        print(f"Name: {self.name}\nStudentID: {self.student_id}")

    def showStudentsCourses(self, name):
        print(f"Name: {self.name}\nCourses: {self.courses}")

    def addStudentToCourse(self, name, studentsCourse):
        if self.name == name:
            self.courses.append(studentsCourse)
            print(f"{self.name} added to a course '{studentsCourse}'.\nStudent's current courses:{self.courses}")


student = Student("Adam", 1, [])
student.showStudentsPersonalInformation("Adam")
student.showStudentsCourses("Adam")
student.addStudentToCourse("Adam", "Math")
student.showStudentsCourses("Adam")
student.addStudentToCourse("Adam", "English")
student.showStudentsCourses("Adam")


student = Student("Brian", 2, [])
student.showStudentsPersonalInformation("Brian")
student.showStudentsCourses("Brian")
student.addStudentToCourse("Brian", "Biology")
student.showStudentsCourses("Brian")
student.addStudentToCourse("Brian", "English")
student.showStudentsCourses("Brian")









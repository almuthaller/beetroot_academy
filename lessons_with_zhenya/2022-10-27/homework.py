"""
Create classes that will describe a Bus Driver, a Student and a Patient of the Hospital. 
Add any attributes and methods essential for each one in your opinion. 
By desire you may use an inheritance principle to gather common attributes and methods into some parent class. 
"""

from datetime import date


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def talk(self):
        print("Hi there!")

    def birthday(self):
        self.age += 1

    def compare_age(self, other):
        if not isinstance(other, Person):
            raise TypeError("This method takes an instance of Person as its argument.")

        comparison = "the same age as"
        if other.age > self.age:
            comparison = "older than"
        if other.age < self.age:
            comparison = "younger than"

        return f"{other.name} is {comparison} me."


class BusDriver(Person):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.people_onboard = 0

    def pick_up(self, number_of_people):
        if type(number_of_people) != int:
            raise TypeError("This method takes an integer as its argument.")

        self.people_onboard += number_of_people

    def drop_off(self, number_of_people):
        if type(number_of_people) != int:
            raise TypeError("This method takes an integer as its argument.")

        if number_of_people > self.people_onboard:
            raise ValueError(
                "You are trying to drop of more people than you have onboard"
                "right now. Might want to count again..."
            )

        self.people_onboard -= number_of_people

    def finish_work(self):
        if self.people_onboard > 0:
            print("Hooold up, you forgot to drop someone off.")

        else:
            print("Nice work! Have a good rest now :)")


class Student(Person):
    def __init__(self, name, gender, age, school, major):
        super().__init__(name, gender, age)
        self.school = school
        self.major = major
        self.year = 1

    def finish_year(self):
        self.year += 1

    def find_study_buddies(self, *others):
        if any(not isinstance(student, Student) for student in others):
            raise TypeError("This method takes instances of Student as arguments.")

        same_major = []
        for student in others:
            if student.major == self.major:
                same_major.append(student.name)

        return f"These students major in the same subject: {same_major}"


class Patient(Person):
    def __init__(self, name, gender, age, department, patient_number):
        super().__init__(name, gender, age)
        self.department = department
        self.patient_number = patient_number
        self.patient_history = f"Patient history for patient number {patient_number}:\n"

    def transfer(self, new_department):
        self.patient_history += f"transferred from {self.department} to {new_department} on {date.today()}\n"
        self.department = new_department


busdriver1 = BusDriver("Bob", "man", 52)
student1 = Student("Hannah", "other", 24, "Harvard", "law")
student2 = Student("Laura", "woman", 19, "Stockholm University", "law")
student3 = Student("Max", "man", 22, "Stockholm University", "psychology")
patient1 = Patient("Kim", "woman", 67, "neurology", 27961)

student1.talk()
print(student1.compare_age(busdriver1))

student1.finish_year()
print(student1.year)

print(student1.find_study_buddies(student2, student3))

busdriver1.pick_up(4)
busdriver1.pick_up(12)
busdriver1.drop_off(3)
busdriver1.drop_off(13)
busdriver1.finish_work()

patient1.transfer("surgery")
print(patient1.patient_history)

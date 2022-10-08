"""
School

Make a class structure in python representing people at school. 
Make a base class called Person, a class called Student, and another one called Teacher. 
Try to find as many methods and attributes as you can which belong to different classes, 
and keep in mind which are common and which are not. 
For example, the name should be a Person attribute, while salary should only be available to the teacher.
"""


class Person:
    def __init__(self, name, age, hometown, number_of_pets):
        self.name = name
        self.age = age
        self.hometown = hometown
        self.number_of_pets = number_of_pets

    def talk(self, string=""):
        pets_str = self.number_of_pets if self.number_of_pets != 0 else "no"
        string_to_print = string + " " if string else ""
        print(
            f"Hi, my name is {self.name}, I am {self.age} years old, {string_to_print}and I have {pets_str} pets."
        )


class Student(Person):
    def __init__(self, name, age, hometown, number_of_pets, year, classroom):
        super().__init__(name, age, hometown, number_of_pets)
        self.year = year
        self.classroom = classroom

    def goes_to_class(self):
        return self.classroom

    def talk(self):
        string = f"I'm in year {self.year}"
        Person.talk(self, string)


class Teacher(Person):
    def __init__(
        self, name, age, hometown, number_of_pets, teaching_subject, has_children
    ):
        super().__init__(name, age, hometown, number_of_pets)
        self.teaching_subject = teaching_subject
        self.has_children = has_children

    def talk(self):
        string = f"I'm a {self.teaching_subject} teacher"
        Person.talk(self, string)


def are_classmates(*students):
    return len(set([s.goes_to_class() for s in students])) == 1


anna = Student("Anna", 9, "Stockholm", 0, 4, "215")
elsa = Student("Elsa", 10, "Täby", 3, 4, "215")
olaf = Student("Olaf", 13, "Helsinborg", 1, 7, "102")
tim = Teacher("Tim", 43, "Täby", 0, "biology", False)
almut = Person("Almut", 21, "Berlin", 3)

print(are_classmates(anna, elsa, olaf))
tim.talk()
elsa.talk()
almut.talk()

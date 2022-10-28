"""
Create a class that describes a cat. The class must have attributes “name”, “age”, “coat_color” at least. 
Also this class will define the method “voice” that prints the string “Meow!”. 
Feel free to add any other attributes or methods that are essential for a cat in your opinion. 
Create two instances of this class, call “voice” method on both of them, change the initial value of “age” for one of them and “name” for another. 
"""


class Cat:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def voice(self):
        print("Meow!")


cat1 = Cat("Lily", 12, "black")
cat2 = Cat("Bobby", 4, "white")
cat1.voice()
cat2.voice()
cat1.age = 13
cat2.name = "Bob"

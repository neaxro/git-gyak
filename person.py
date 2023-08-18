
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self):
        print("Hello my name is", self.name, "and I am ", self.age, "year(s) old!")
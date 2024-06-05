class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

class PersonBuilder:
    def __init__(self):
        self.person = Person('', 0, '')

    def set_name(self, name):
        self.person.name = name
        return self

    def set_age(self, age):
        self.person.age = age
        return self

    def set_gender(self, gender):
        self.person.gender = gender
        return self

    def build(self):
        return self.person

builder = PersonBuilder()
person = builder.set_name('Alice').set_age(30).set_gender('Female').build()

print(person)

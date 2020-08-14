class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f" Hi! {self.name}")


class Male(Person):
    def __init__(self):
        print("under male")


person1 = Person(input("Name: "))
person1.talk()
mohan = Male();
mohan.name= 'Mohan'
mohan.talk()
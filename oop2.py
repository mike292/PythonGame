class Person:
    number_of_people = 0 #Class Attribute

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1 #Calls the class attribute and Increments the class attribute everytime an instance is made
        Person.add_person() #Calling the class method

    @classmethod #To create a class method
    def get_number_of_people(cls): #cls is refering to the class itself not instance
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
# print(p1.number_of_people)
p2 = Person("Jill")
# print(p2.number_of_people)
print(Person.get_number_of_people())
class Student:
    def __init__(self, name, dateofbirth, height, is_on_drugs):
        self.name=name
        self.dateofbirth=dateofbirth
        self.height=height
        self.is_on_drugs=is_on_drugs
person1= Student("Jim","17 October 1999",190,False)
print(person1.dateofbirth)


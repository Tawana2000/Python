#Q1.WAP to count the number of objects created
class Student :
    counter = 0
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        Student.counter += 1
    def printDetails(self) :
        print(self.name,self.age,"years old")
student1 = Student('Tawana',22)
student2 = Student('Mahmoud',24)
student3 = Student('Bassel',23)
print("Total number of objects created: ",Student.counter)

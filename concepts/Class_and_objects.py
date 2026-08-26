class Student:
    def getdata(self):
        self.name = input("Enter name: ")

    def display(self):
        print("Name = ",self.name)

s = Student()
s.getdata()
s.display()
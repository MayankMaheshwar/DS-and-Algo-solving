class Student:
    @classmethod
    def clsmethod(cls):
        print("I am class method", cls)

    @staticmethod
    def stamethod():
        print("I am static method")


mayank = Student()
mayank.clsmethod()
mayank.stamethod()
Student.clsmethod()

Student.stamethod()

# x = 10
# class Student:
#     pass # no thing in this class
#
# ## take instance or object
# s = Student()

# ## add properties to the class
# ## object factory
# class Student:
#     def __init__(self):  # ## customize how the object will be created --->
#         # __init__ : initialize the object  ---> is the constructor
#         print(self)  # self  ---> is the object address in the memory
#         print("The object will be created now ")
#         self.name = "Ahmed"
#         self.email = 'ahmed@gmail.com'
#
#
# s = Student()
#
#
# noha = Student()

##############################3 modify the constructor

# l = [3,4,5]  # object from type class list
# class Student:
#     def __init__(self, firstname, std_email):  # ## customize how the object will be created --->
#         # __init__ : initialize the object  ---> is the constructor
#         print(self)  # self  ---> is the object address in the memory
#         print("The object will be created now ")
#         self.name = firstname
#         self.email = std_email
#
#
# s = Student("Ali", "Ali@gmail.com")


######################################################
#
# class Student:
#     def __init__(self, firstname, std_email):  # ## customize how the object will be created --->
#         # __init__ : initialize the object  ---> is the constructor
#         print(self)  # self  ---> is the object address in the memory
#         print("The object will be created now ")
#         self.name = firstname  # instance variables ===(their values depend on the instance )
#         self.email = std_email
#
#
# std =  Student("Ahmed", "ahmed@gmail.com")
# # access object content using objectname
# # ## modify the data in the object properties
# print(std.name)
# print(std.email)
# std.name = "Mohamed"
# # modify the object structure in the runtime
# std.level = 10
#
# std2 = Student("Noha", "noha@gmaail.com")
# std2.name = "Ali"
# std2.city = "Cairo"
#
#
# # OOP principles , all objects from the same class must have the same properties
#


# ######################### class variable
# common variable shared  between all the instances in the classes
# class Summertraing:
#     status = 'Student'  # class variable  #can be accessed using class name
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# s1 = Summertraing("Ahmed", "ahmed@gmail.com")
# # s2 = Summertraing("omar", "omar@gmail.com")
# print(Summertraing.status)
# Summertraing.status = "undergraduate"
# s2 = Summertraing("omar", "omar@gmail.com")
# print("----------------------------------")
# s2.status = "graduate" # create new property in the object with the name status ...
#
# Summertraing.status = "itian "  # is a comman varaible class variable
# print("------------------")
#
# mohamed = Summertraing("mohamed", "mohamed@gmail.com")
# print("------------------")
###############################################

# class Employee:
#     empcount = 0
#     def __init__(self, name, emp_dept):
#         self.name = name
#         self.dept = emp_dept
#         Employee.empcount += 1
#         print(f"-------empcount = {Employee.empcount}---------------")
#
#
# e = Employee("Ahmed", "python")
#
# m = Employee("Mohmaed", "Django")
#
# n = Employee("Ali", "test")


##########################
### what is object ---> instance from sometype ---> has  some properties, can do some function
# object wrap data and functionality
#
# class Employee:
#     empcount = 0
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Employee.empcount +=1
#
#     # instance method --> its behaviour depends on the called instance
#     def speak(self):  # represent the instance
#         # self represent the instance
#         print(f"Emp name = {self.name}")
#
#     def greet(self, message):
#         print(f"{message}, {self.name}")
#
# e = Employee("noha", "noha@gmail.com")
# print(e.name)
# e.speak()
# e.greet("Nice to meet you ")
#
# e2 = Employee("Ahmed", "ahmed@gmail.com")
# e2.speak()
# e2.greet("Welcome ... ")


##############################3

### instance variable   ## class variable
### instance method ?   ## class method
# class Employee:
#     empcount = 0
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Employee.empcount +=1
#
#     # instance method --> its behaviour depends on the called instance
#     def speak(self):  # represent the instance
#         # self represent the instance
#         print(f"Emp name = {self.name}")
#
#     def greet(self, message):
#         print(f"{message}, {self.name}")
#
#     # method --> its behaviour depends on the class
#     @classmethod
#     def get_emp_count(cls):  # represent the current class
#         print(cls, cls.empcount)
#         print(Employee.empcount)
#
#     # class method can be used to create new object
#     @classmethod
#     def objectCreator(cls):
#         return cls("default", "defualt@gmail.com")
#
# Employee.get_emp_count()
# e = Employee("ahmed", "ahmed@gmail.com")
#
# e2 = Employee.objectCreator()

# #########################################  static method

class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

    ## helper function
    @staticmethod
    def calnetsal(salary):
        return salary*.86


e = Employee("Ahmed", 10000)
# cal net sal
print(Employee.calnetsal(e.salary))
print(Employee.calnetsal(2000000))

# def calnetsal(salary):
#     return salary*.86
#
# emp_sal = calnetsal(e.salary)
# print(emp_sal)
#
# print(calnetsal(999999))

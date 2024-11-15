# class Employee:
#     pass
# emp1 = Employee()
# emp1.n = input("name:")
# emp1.a =int( input("age:"))
# emp1.s = int(input("salary:"))
# print(emp1.n)
# print(emp1.a)
# print(emp1.s)

# class Manager:
#     def __init__(self,name,departent,salary):
#         self.name = "Ankit"
#         self.departent = departent
#         self.salary = 23333333333

# name=input("name:")
# name=input("departent:")
# name=input("age:")

# class car:
#     def __init__(self):
#         self.name=""
#         def setName(self,name):
#             self.name = name
#         def setName(self):
#             return self.name   

# Honda = Car()
# carname=input("car name")


# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
# name = input("s1 name:")
# age = int(input("s1 age"))

# class person:
#     def __init__(self):
#         self.name = ""
#         def setName(self,name):
#             self.name = name
#         def getName(self):   
#             return self.name
        
# p1 = person()
# # p2 = person()
# name1 = input('p1 name:')
# # name2 = input('p2 name:')
# p1.setName(name1)
# # p2.setName(name2)
# print("p1 name:",p1.getName())

# class greeting:
#     def sayHello(self,name=None,wish=None):
#         if name and wish:
#             print(f"Hello{name}{wish}")
#         elif name:    
#             print(f"Hello{name}")
#         else:    
#             print("Hello!")

# greet = greeting()
# a=input()
# b=input()
# greet.sayHello(a)
# greet.sayHello(a,b)

# class Employee:
#     company="Google"
#     salary=45376
#     name="Ankit"
# Ankit=Employee()    
# Ankit.company="Microsoft"
# print(Ankit.salary,Ankit.company)
# class Employee:
#     company="Microsoft"
#     salary=87778887
#     def getMethod(self):
#         print("Your name is Ankit")
#     def __init__(self):
#         print("Your are good student")    
#     def greet(self):
#         print("Goodmorning")


# Ankit=Employee()
# # # print(Ankit.salary,Ankit.company)
# Ankit.getMethod()
# Ankit.greet()

# class Employee:
#     company="Google"
#     salary=4576646
#     name="ABC"
#     # def getsalary():
#     #     print("Good pachages")
#     # def greet():    
#     #     print(f"you get good salary of {Ankit.salary}")
#     # def __init__(self,name,salary,company):
#     #     self.name=name
#     #     self.salary=salary
#     #     self.company=company
#         # print("I am creating object")
#     def greet(self):    
#         print("Self.bbbb")
         
# Ankit=Employee()
# # Ankit=Employee("Ankit",54488,"Google")
# # Employee.getsalary()
# Employee.greet()
# # Ankit.company="Microsoft"
# # print(Ankit.salary,Ankit.company)

# class Employee:
#   company = "Google"
#   def getSalary(self):
#       print("Salary is not there")  

# Ankit=Employee()
# Employee.getSalary(Ankit)

# class Emplyee:
#     company="Google"
#     salary=65995896    

#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         print("Ther is huge salary")

# Ankit=Emplyee("Ankit",20,58456598)        
# print(Ankit.salary,Ankit.age,Ankit.name)

# class Abc:
# #     a=54548
#     def greet():
#         print("hello")

# # Ankit=Abc()    
# # Ankit.a=0
# Abc.greet()
# print(Ankit.a)

# class Train:
#     def __init__(self,tobookticket,getstatus,getinformation):
#         self.tobookticket=tobookticket
#         self.getstatus=getstatus
#         self.getinformation=getinformation
#         print("kvvvvz")

# Savarmati=Train("ticket","no of seats","where is Train")  
# print(Savarmati.getinformation,Savarmati.getstatus,Savarmati.tobookticket)      


# class Emplyee:
#     compaany="Google"
#     salary=666689759
#     age=20
# class programme(Emplyee):
# Ankit=Emplyee()    
# Ankit.compaany="Microsoft"
# print(Ankit.age,Ankit.compaany)

# class car:
#     def model(self,engine):
#         self.engine=engine
#     def getenginemodel(self):
#         print(f"{self.engine}")    

# class Honda(car):
#     def setcarmodel(self,model):
#         self.model=model
#     def getcarmodel(self):    
#         print(f"{self.model}")

# mycar=Honda()        
# mycar.model("EK-1")
# mycar.setcarmodel("V6")
# print("car.Detail")
# mycar.getenginemodel
# mycar.getcarmodel

# class person:
#     def setname(self,name):
#         self.name=name
#     def getname(self):    
#         print(f"{self.name}")
# class Student(person):
#     def setage(self,age):
#         self.age=age
#     def getage(self):    
#         print(f"{self.age}")
# class address(Student):        
#     def setaddress(self,address):
#         self.address=address
#     def getaddress(self):    
#         print(f"{self.address}")

# class vehicle:
#     def __init__(self,name,price,regno):
#         self.name=name
#         self.price=price
#         self.regno=regno

# class car(vehicle):
#     def __init__(self, name, price, regno,gear):
#         super().__init__(name, price, regno)
#         self.gear=gear

# class boat(vehicle):
#     def __init__(self, name, price, regno):
#         super().__init__(name, price, regno,)

# class hover(car,boat):        
#     def __init__(self, name, price, regno, gear):
#         super().__init__(name, price, regno, gear)

# c1=car("toyota")

# class employee:
#     a=1
#     name="Aman"
#   @classmethod
#     def AA(self):
#         print(f"{self.name,self.a} is good boy")
# abc=employee()        
# abc.a=45
# abc.AA()

# class Emolyee:
#     a=1
#     @classmethod
#     def function(cls):
#         print(f"{cls.a}")

# Ankit=Emolyee()
# Ankit.a=45
# Ankit.function()

# class Number:
#     def __init__(self,n):
#         self.n=n

#     def _mul_(self,num):
#         return  self.n + num

# n=Number(1)        
# m=Number(2)
# print(n * m)

# class oneDvector:
#     a=67
#     def cl(self,name):
#         self.name=name
# class threeDvector(oneDvector):
#     b=34
#     def ok(self):
#         print(f"b {self.b}")

# a=threeDvector()
# a.ok()

# class Animal:
#     def ob(self):
#         pass
# class pet(Animal):
#     def ok(self):
#         pass
# class dog(pet):
#     @staticmethod
#     def lk():
#         print("bow bow!")
# a=dog()       
# a.lk()

# class Emplyee:
#     name="ANkit"
#     age=20
#     company="Google"
#     def y(self):

        

# ABC=Emplyee()
# ABC.company="Microsoft"
# print(ABC.age,ABC.name,ABC.company)

# class Emplyee:
#     def __init__(self,name,age,salary,department):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.department=department
#     # def showdetail(self,)    

# z=Emplyee(input(),input(),input(),input())
# print(z.name,z.age,z.salary,z.department)

# class car:
#     def showdetail(self,carname,carmodel):
#         self.carname=carname
#         self.carmodel=carmodel

# class carworker(car):
#     def showdetail(self, carname, carmodel,gearno):
#         super().showdetail(carname, carmodel)
#         self.grearno=gearno

# class carworker1(carworker):
#     def showdetail(self, carname, carmodel, gearno,drivername):
#          super().showdetail(carname, carmodel, gearno)
#          self.drivername=drivername         
# a=carworker1()     
# a.showdetail("bmw","gkvl",5,"ABC")     
# print(a.carname,a.carmodel,a.grearno,a.drivername)

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self_group="ECE"
#         self_report="fail"
#     def setdetails(self,group,report):
#         self_group=group
#         self_report=report
#     def  getdetails(self):
#         print(self.name,self.age,self._group,self._report)       

# name=input()
# age=int(input())
# group=input()
# report=input("pass/fail: ")

# a=student()
# print(a.age,a.name,a._group,a._report)

# print("student report card")

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def welcome(self):
#         print("Welcome student")    
#     def getmarks(self):
#          return self.name
# s1=student("Ankit",98)
# s1.welcome()
# # s1.getmarks()
# print(s1.name)
# s1.getmarks()

# class student:
#     def __init__(self,name,maths,phy,che):
#         self.name=name
#         self.maths=maths
#         self.phy=phy
#         self.che=che
#     def method(self):    
#         average=((self.maths+self.phy+self.che)/3)
#         print(average)
# a=student("Ankit",2,2,2) 
# a.method()       

# class Account:
#     balnce=548754        
#     accountno=56759
#     def Money(self,debit,credit):
#         self.debit=debit
#         self.credit=credit
#         print("you bank balace is:")
# a=Account()
# a.Money()


        
                





        
        







        
        






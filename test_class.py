# class Animal(object):
#     type_account=100
#     def __init__(self,name,age):
#         print('Animal is initialized')
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(self.name+'Eating')
#
#     def sleep(self):
#         print(self.name+'sleeping')
# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         self.has_tail = True
#
#     def bark(self):
#         print(self.name+'barking')
#
# class human(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         self.has_tail = False
#
#     def read(self):
#         print(self.name+'reading')
#
#     def sleep(self):
#         print(self.name + 'sleeping at class of human')
#
# Tom=human("Tom",10)#每次实例化都会调用一次__init__
# Tom.eat()
# Tom.sleep()
# Gary=Dog('Gary',200)
# Gary.bark()
# Gary.sleep()
# print(Tom.type_account)
# print(Gary.has_tail)

#人力系统
class humansystem:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_info(self):
        print("Name:",self.name)
        print("ID:",self.id)

class FullTimeEmployee(humansystem):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(humansystem):
    def __init__(self,name,id,daily_salary,workdays):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.workdays=workdays
    def calculate_salary(self):
        return self.daily_salary*self.workdays

zhangsan=FullTimeEmployee("zhangsan",101,10000)
wangwu=PartTimeEmployee("wangwu",102,100,30)
zhangsan.print_info()
print("salary: "+str(zhangsan.calculate_salary()))

wangwu.print_info()
print("salary: "+str(wangwu.calculate_salary()))

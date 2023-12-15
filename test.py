# import sys
#
# #  python --version
# # python
# # exit()
# # IDLE
#
# print('Hello World')
#
# message = 'Hello World'
# print(message) #'Hello World'
#
# message = "Bobby's World"  # or 'Bobby\'s World'
#
# multi_line_message = """This ia a multiple line text
#  prints in multiple lines"""
# print(multi_line_message)
#
# # Slicing
# message='Hello World'
# print(len(message)) # 11
# print(message[0]) # H
# print(message[0:4]) # Hell
# print(message[6:]) # World
# print(message[:2]) #He
#
# #methods
# message = 'Hello World'
# print(message.lower()) #hello world
# print(message.upper()) #HELLO WORLD
# print(message.count('Hello')) #1
# print(message.count('l')) #3
# print(message.find('World')) #6 returns starting index of that character
# print(message.find('Universe')) #-1 returns -1 if the word does not exists
# print(message.replace('World','Universe'))
#
# new_message = message.replace('World','Universe')
# print(new_message)
#
# greeting = 'Hello'
# name = 'Sai'
# message = greeting + ', ' + name + '. Welcome'
# print(message)
#
# #formated string
# message = '{}, {}. Welcome'.format(greeting, name)
# print(message)
#
# #fstring
# message = f'{greeting}, {name}. Welcome'
# print(message)
# message = f'{greeting}, {name.upper()}. Welcome'
# print(message)
#
# #returns all the methods that are available for the variable name
# print(dir(name))
#
# #returns all the methods that are available for string datatype
# print(help(str))
#
# #returns the description for lower method
# print(help(str.lower))
#
# #Arithmetic Operations
# print(3 + 2) #5
# print(3 - 2) #1
# print(3 * 2) #6
# print(3 / 2) #1.5
# print(3 // 2) #1
# print(3 % 2) #1
# print(3 ** 2) #9
#
# num = 1
# num = num+1
# print(num) #2
# num = 1
# num += 1
# print(num) #2
#
# print(abs(-3)) #3
# print(round(3.75)) #4 rounds the number to the nearest integer
# print(round(3.25)) #3
# print(round(3.75,1)) #3.8
#
# num_1 = 3
# num_2 = 2
# print(num_1 == num_2) #False
# print(num_1 != num_2) #True
# print(num_1 > num_2) #True
# print(num_1 < num_2) #False
# print(num_1 >= num_2) #True
# print(num_1 <= num_2) #False
#
# num_1 = '100'
# num_2 = '200'
# print(num_1 + num_2) #100200
# num_1 = int(num_1)
# num_2 = int(num_2)
# print(num_1 + num_2) #300
#
# #List
# courses = ['English', 'Math', 'History', 'CompSci']
# print(courses) #['English', 'Math', 'History', 'CompSci']
# print(len(courses)) #4
# print(courses[0]) #English
# print(courses[0:2]) #['English', 'Math']
# print(courses[:2]) #['English', 'Math']
# print(courses[2:]) #['History', 'CompSci']
#
# #List Methods
# courses.append('Art') #it appends the value at the end of the list
# print(courses) #['English', 'Math', 'History', 'CompSci', 'Art']
# courses.insert(0,'Physics') #it inserts the value at 0 position
# print(courses) #['Physics', 'English', 'Math', 'History', 'CompSci', 'Art']
# courses_2 = ['Dance', 'Music']
# courses.insert(0,courses_2)
# print(courses) #[['Dance', 'Music'], 'Physics', 'English', 'Math', 'History', 'CompSci', 'Art']
# print(courses[0]) #['Dance', 'Music']
# courses = ['Physics', 'English', 'Math', 'History', 'CompSci', 'Art']
# courses_2 = ['Dance', 'Music']
# courses.extend(courses_2)
# print(courses) #['Physics', 'English', 'Math', 'History', 'CompSci', 'Art', 'Dance', 'Music']
# courses.remove('Math')
# print(courses) #['Physics', 'English', 'History', 'CompSci', 'Art', 'Dance', 'Music']
# courses.pop()
# print(courses) #['Physics', 'English', 'History', 'CompSci', 'Art', 'Dance']
# popped = courses.pop()
# print(popped) #Dance
# courses.reverse()
# print(courses) #['Art', 'CompSci', 'History', 'English', 'Physics']
# courses.sort()
# print(courses) #['Art', 'CompSci', 'English', 'History', 'Physics']
# num = [1, 4, 6, 2, 0]
# num.sort()
# print(num) #[0, 1, 2, 4, 6]
# num.sort(reverse=True)
# print(num) #[6, 4, 2, 1, 0]
# courses = ['Physics', 'English', 'History', 'CompSci', 'Art', 'Dance']
# sorted_courses = sorted(courses)
# print(courses) #['Physics', 'English', 'History', 'CompSci', 'Art', 'Dance']
# print(sorted_courses) #['Art', 'CompSci', 'Dance', 'English', 'History', 'Physics']
# print(min(num)) #0
# print(max(num)) #6
# print(sum(num)) #13
# print(courses.index('History')) #2
# #print(courses.index('Civics')) #ValueError: 'Civics' is not in list
# print('Art' in courses) #True
# print('Civics' in courses) #False
#
# for item in courses:
#     print(item)
#
# for index, item in enumerate(courses):
#     print(index, item)
#
# for index, item in enumerate(courses, start=1):
#     print(index,item)
#
# str_joined = ' - '.join(courses)
# print(str_joined) #Physics - English - History - CompSci - Art - Dance
# new_list = str_joined.split(' - ')
# print(new_list) #['Physics', 'English', 'History', 'CompSci', 'Art', 'Dance']
#
# #Lists are mutable and tuples are immutable
# #Tuples:
#
# #Mutable
# list_1 = ['Physics', 'English', 'History']
# list_2 = list_1
# print(list_1)
# print(list_2)
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)
#
# #Immutable
# tuple_1 = ('Physics', 'English', 'History')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# #tuple_1[0]='Art' #'tuple' object does not support item assignment because it is immutable
#
# #Sets
# courses = {'Physics', 'English', 'History'}
# print(courses) #{'Physics', 'History', 'English'} every time when we execute order will change
# courses = {'Physics', 'English', 'History', 'English'} #sets remove duplicates
# print(courses) #{'English', 'Physics', 'History'}
# print('History' in courses) #True
# courses_2 = {'Dance', 'Music', 'English'}
# print(courses.intersection(courses_2)) #{'English'}
# print(courses.difference(courses_2)) #{'History', 'Physics'}
# print(courses.union(courses_2)) #{'Music', 'History', 'Physics', 'English', 'Dance'}
#
# #How to create empty list, tuple, and sets
# empty_list = []
# empty_list = list()
#
# empty_tuple = ()
# empty_tuple = tuple()
#
# empty_set = set()
#
# #Disctionaries
# empty_dict = {}
# empty_dict = dict()
# student = {'name':'Rajitha', 'Age':28, 'courses':['Python', 'SQL']}
# print(student) #{'name': 'Rajitha', 'Age': 28, 'courses': ['Python', 'SQL']}
# print(student['name']) #Rajitha
# print(student['courses']) #['Python', 'SQL']
# #print(student['phone']) #KeyError: 'phone'
# print(student.get('name')) #Rajitha
# print(student.get('phone')) #None
# print(student.get('phone', 'Not Found')) #Not Found
#
# student['phone'] = '71652436'
# print(student) #{'name': 'Rajitha', 'Age': 28, 'courses': ['Python', 'SQL'], 'phone': '71652436'}
# student['name'] = 'Raji'
# print(student) #{'name': 'Raji', 'Age': 28, 'courses': ['Python', 'SQL'], 'phone': '71652436'}
#
# student.update({'name':'Rajitha', 'phone': '8333838910', 'courses': ['Python', 'SQL', 'Tableau']})
# print(student) #{'name': 'Rajitha', 'Age': 28, 'courses': ['Python', 'SQL', 'Tableau'], 'phone': '8333838910'}
#
# del student['Age']
# print(student) #{'name': 'Rajitha', 'courses': ['Python', 'SQL', 'Tableau'], 'phone': '8333838910'}
#
# popped_phone = student.pop('phone')
# print(popped_phone) #8333838910
#
# print(len(student)) #2
# print(student.keys()) #dict_keys(['name', 'courses'])
# print(student.values()) #dict_values(['Rajitha', ['Python', 'SQL', 'Tableau']])
# print(student.items()) #dict_items([('name', 'Rajitha'), ('courses', ['Python', 'SQL', 'Tableau'])])
#
# for key in student:
#     print(key)
#
# for key, value in student.items():
#     print(key, value)
#
# #Conditions
#
# if True:
#     print('condition was true')
#
# if False:
#     print('contion was true')
#
# language = 'S'
# if language == 'Python':
#     print('language is python')
# elif language == 'Java':
#     print('language is Java')
# elif language == 'SQL':
#     print('language is SQL')
# else:
#     print('No Match')
#
# user = 'admins'
# logged_in = 0
# if user == 'admin' and logged_in:
#     print('admin page')
# else:
#     print('bad credentials')
#
# if not logged_in:
#     print('Please login')
# else:
#     print('Welcome')
#
# a = [1,2,3]
# b = [1,2,3]
# print(a == b) #True
# print(a is b) #False it compares id of a to id of b
# print(id(a) == id(b)) #False
# a = [1,2,3]
# b = a
# print(id(a) == id(b)) #True
# print(a is b) #True
#
# condition=False #condition is False
# condition = None #condition is False
# condition = 0 #condition is False
# condition = 10 #condition is True
# condition = '' #any empty sequence ex: '',(),[], {}  #condition is False
# condition = {} #condition is False
#
# if condition:
#     print('condition is True')
# else:
#     print('condition is False')
#
# #For Loop
nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     print(num)
#
# #break statement
# for num in nums:
#     if num == 4:
#         print('Found!')
#         continue
#     print(num)
#
# #continue statement
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)
#
# #Loop inside another loop
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

#
# for i in range(10):
#     print(i)
#
# for i in range(1,11):
#     print(i)
#
# x = 0
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1
#
# #Functions
# def hello_func():
#     pass
# print(hello_func) #<function hello_func at 0x000001F2FF7B6F20>
# print(hello_func()) #None

#
# def hello_fun():
#     print('Hello')
#
# hello_fun() #Hello
# #DRY don't repeat yourself
#
# def hello_function():
#     return 'Hello Function.'
#
# print(hello_function()) #Hello Function.
# print(hello_function().upper()) #HELLO FUNCTION.
#
# def message_function(name):
#     return 'Hello, {}.'.format(name)
#
# print(message_function('Rajitha')) #Hello, Rajitha.

# def hello_func(greeting, name='You'):
#     return '{}, {}.'.format(greeting, name)
#
# print(hello_func('Hi', 'Rajitha')) #Hi, Rajitha.
# print(hello_func(name='Rajitha', greeting='Hi')) #Hi, Rajitha.
# print(hello_func('Hi')) #Hi, You.
#
# def student_info(*args, **kwargs):
#     print(args) #('Art', 'Math', 'Science')
#     print(kwargs) #{'name': 'Raji', 'Age': 28}
#
# student_info('Art', 'Math', 'Science', name = 'Raji', Age=28) #print(args) #('Art', 'Math', 'Science')
#                                                                     #print(kwargs) #{'name': 'Raji', 'Age': 28}
# courses = ['Art', 'Math', 'Science']
# details = {'name': 'Raji', 'Age': 28}
# student_info(courses, details) #(['Art', 'Math', 'Science'], {'name': 'Raji', 'Age': 28})
#                                      #{}
# student_info(*courses, **details) #('Art', 'Math', 'Science')
#                                         #{'name': 'Raji', 'Age': 28}
#
# #Finding month_days of a month
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# def leap_year(year):
#     '''Returns True if it is leap year'''
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# def find_month_days(year, month):
#     if not (month >= 1 and month <=12):
#         return 'Not Valid Month'
#     elif leap_year(year) and month==2:
#         return 29
#     else:
#         return month_days[month]
#
# print(find_month_days(2017, 12))
#

# #Importing Modules
# # import test
# # print(test.find_month_days(2000,1))
# #
# # import test as t
# # print(t.find_month_days(2000,12))
# #
# # from test import find_month_days, courses
# # print(find_month_days(2000, 12))
#
# # print(sys.path)
# #
# # import sys
# # sys.path.append('E:')
# # # print(find_month_days(2000, 12))
#
# import random
# cources = ['math', 'science', 'physics', 'art']
# random_course = random.choice(courses)
# print(random_course)
#
# import math
# rads = math.radians(90)
# print(rads) #1.5707963267948966
# print(math.sin(rads)) #1.0
#
# import datetime
# import calendar
# today = datetime.date.today()
# print(today) #2023-11-07
# print(calendar.isleap(2020)) #True
#
# import os
# print(os.getcwd()) #C:\Users\PC\PycharmProjects\pythonProject
#
# #OS Module
# import os
# #print(dir(os))
# print(os.getcwd()) #C:\Users\PC\PycharmProjects\pythonProject
# os.chdir("C:\\Users\PC\PycharmProjects\pythonProject")
# print(os.getcwd()) #C:\Users\PC\PycharmProjects
# print(os.listdir())
# # os.mkdir('my_dir') #if we have to create single folder use mkdir
# # os.makedirs('my_dir\\my_sub_dir') #if we have multiple sub dir inside one dir then go for makedirs
# # os.rmdir('my_sub_dir')
# # os.removedirs('my_dir\\my_sub_dir')
# # os.rename('test.py', 'test1.py')
# # os.rename('test1.py', 'test.py')
# print(os.stat('test.py'))
# print(os.stat('test.py').st_size) #12134 bytes
# print(os.stat('test.py').st_mtime) #1699376878.6562054
# last_modified_time = os.stat('test.py').st_mtime
# time_converted = datetime.datetime.fromtimestamp(last_modified_time)
# print(time_converted) #2023-11-07 22:41:41.090198
#
# # for dirpath, dirnames, filenames in os.walk('C:\\Users\PC\PycharmProjects\pythonProject'):
# #     print('path: ', dirpath)
# #     print('dirnames: ', dirnames)
# #     print('filenames: ', filenames)
# #     print()
#
# # print(os.environ)
# print(os.environ.get('HOME'))
# new_path = os.path.join('C:\\Users\PC\PycharmProjects\pythonProject','test1.py')
# print(new_path) #C:\Users\PC\PycharmProjects\pythonProject\test1.py
# print(os.path.split('C:\\Users\PC\PycharmProjects\pythonProject\test1.py'))
# print(os.path.exists('C:\\Users\PC\PycharmProjects\pythonProject'))
# print(os.path.isdir('C:\\Users\PC\PycharmProjects'))
# print(os.path.isfile('C:\\Users\PC\PycharmProjects\pythonProject\test1.py')) #False
# print(os.path.splitext('C:\\Users\PC\PycharmProjects\pythonProject\test1.py')) #('C:\\Users\\PC\\PycharmProjects\\pythonProject\test1', '.py')
# print(dir(os.path))

#File Objects

# f = open('text.txt') #by default it will open with read mode
# f = open('text.txt', 'r') #read mode
# f = open('text.txt', 'w') #write mode
# f = open('text.txt', 'r+') #read and write mode
# f = open('text.txt', 'a') #append mode

# f = open('text.txt', 'r')
# print(f.name) #text.txt
# print(f.mode) #r
# print(f.read())
# f.close()

# with open('text.txt', 'r') as f:
#     print(f.name) #text.txt
#     f_contents = f.read()
#     print(f_contents)
# # print(f.read()) #error
#
# with open('text.txt','r') as f:
#     print(f.readlines()) #['This is Python text file\n', 'this is File Objects topic\n', 'it has multiple lines of data\n']
#
# with open('text.txt','r') as f:
#     print(f.readline(), end='')
#     print(f.readline())

# with open('text.txt','r') as f:
#     for line in f:
#         print(line, end='')

# with open('text.txt','r') as f:
#     f_contents = f.read(100)
#     print(f_contents)
#     f_contents = f.read(100)
#     print(f_contents)
#     f_contents = f.read(100)
#     print(f_contents)

# with open('text.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#
#     while len(f_contents) > 0:
#         print(f_contents, end='')
#         f_contents = f.read(size_to_read)
#     print(f.tell()) #it prints which position we are in

# with open('text.txt', 'r') as f:
#     f_contents = f.read(10)
#     print(f_contents)
#
#     f.seek(0)
#
#     f_contents = f.read(10)
#     print(f_contents)

# with open('testfiles.txt','w') as f: #it is going to create the file with the given name,
#                                      # if the file is already exists it is going to over write it
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# with open('text.txt', 'r') as rf:         #use 'rb', 'wb' for image files like '.jpg'
#     with open('text_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('test.jpg','rb') as rf:
#     with open('text_copy.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = f.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = f.read(chunk_size)

# Python Object-Oriented Programming
#------------------------------------
# class Employee:
#     no_of_Employees = 0
#     raise_amount = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         Employee.no_of_Employees += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_empstr(cls, emp_str):   #here this class method acting like a alternative constructer
#         cls.emp_str = emp_str
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#     #Dunder Methods
#     def __str__(self):
#         return self.fullname()
#     def __repr__(self):
#         return "('{}', '{}', {})".format(self.first, self.last, self.pay)
#     def __add__(self, other):
#         return self.pay + other.pay
#     def __len__(self):
#         return len(self.fullname())
#
#
# class Developer(Employee):
#     raise_amount = 1.05
#
#     def __init__(self, first, last, pay, prog_lan):
#         super().__init__(first, last, pay)
#         self.prog_lan = prog_lan
#
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emp(self):
#         for emp in self.employees:
#             print('-->' , emp.fullname())

# print(help(Developer)) #prints method resolution order for developer class

# Method Resolution Order

# emp_1 = Employee('Rajitha', 'Palla', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.email) #Rajitha.Palla@company.com
# print(emp_1.fullname()) #Rajitha Palla
# print(Employee.fullname(emp_1)) #Rajitha Palla
# print(Employee.raise_amount) #1.04
# print(emp_1.raise_amount) #1.04
# print(emp_2.raise_amount) #1.04

# Employee.raise_amount = 1.05
# print(Employee.raise_amount) #1.05
# print(emp_1.raise_amount) #1.05
# print(emp_2.raise_amount) #1.05

# emp_1.raise_amount = 1.07
# print(Employee.raise_amount) #1.04
# print(emp_1.raise_amount) #1.07
# print(emp_2.raise_amount) #1.04

# print(emp_1.pay) #50000
# emp_1.apply_raise()
# print(emp_1.pay) #52000

# print(Employee.__dict__)
# print(Employee.no_of_Employees) #2

# print(Employee.raise_amount) #1.04
# print(emp_1.raise_amount) #1.04
# print(emp_2.raise_amount) #1.04
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount) #1.05
# print(emp_1.raise_amount) #1.05
# print(emp_2.raise_amount) #1.05

# new_emp1_str = 'John-Doe-70000'
# first, last, pay = new_emp1_str.split('-')
# new_emp1 = Employee(first, last, pay)
# print(new_emp1.email) #John.Doe@company.com

# new_emp1_str = 'John-Doe-70000'
# new_emp1 = Employee.from_empstr(new_emp1_str)
# print(new_emp1.email) #John.Doe@company.com

# import datetime
# day = datetime.date(2023, 11, 13) #True
# print(Employee.is_workday(day))

# dev_1 = Developer('Rajitha', 'Palla', 10000)
# print(dev_1.pay) #10000
# dev_1.apply_raise()
# print(dev_1.pay) #10500

# dev_1 = Employee('Rajitha', 'Palla', 10000)
# print(dev_1.pay) #10000
# dev_1.apply_raise()
# print(dev_1.pay) #10400

# dev_1 = Developer('Rajitha', 'Muppuri', 10000, 'Python')
# print(dev_1.prog_lan) #Python

# dev_1 = Developer('Rajitha', 'Palla', 50000, 'Python')
# dev_2 = Developer('Test', 'User', 20000, 'Java')
# mgr_1 = Manager('Sue', 'Smith', 60000, [dev_1])
# print(mgr_1.email) #Sue.Smith@company.com
# mgr_1.print_emp() #--> Rajitha Palla
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emp()

# print(isinstance(mgr_1, Manager)) #True
# print(isinstance(mgr_1, Employee)) #True
# print(isinstance(mgr_1, Developer)) #False

# print(issubclass(Developer, Employee)) #True
# print(issubclass(Manager, Employee)) #True
# print(issubclass(Manager, Developer)) #False
# print(issubclass(Employee, Manager)) #False

# emp_1 = Employee('Rajitha', 'Palla', 50000)
# emp_2 = Employee('Test', 'User', 60000)
# print(emp_1 + emp_2) #110000
# print(len(emp_1)) #13
# print(emp_1.__repr__()) #('Rajitha', 'Palla', 50000)
# print(emp_1.__str__()) #Rajitha Palla
# print(emp_1) #Rajitha Palla

# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         #self.email = first + '.' + last + '@company.com'
#     @property
#     def email(self):
#         return '{}.{}@company.com'.format(self.first, self.last)
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print('Employee Deleted')
#         self.first = None
#         self.last = None
#
# emp_1 = Employee('Rajitha', 'Palla')
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())
# emp_1.first = 'Raji'
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())
# emp_1.fullname = 'Test User'
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
# del emp_1.fullname
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# CSV Module
#-----------------------
# import csv

# with open('names.csv', 'r') as csv_names:
#     csv_reader = csv.reader(csv_names)
#     # next(csv_reader)
#     for line in csv_reader:
#         # print(line)
#         print(line[2])

# with open('names.csv','r') as csv_readfile:
#     csv_reader = csv.reader(csv_readfile)
#     with open('new_names.csv', 'w') as csv_writefile:
#         csv_writer = csv.writer(csv_writefile, delimiter='-')
#         for line in csv_reader:
#             csv_writer.writerow(line)
#
# with open('new_names.csv', 'r') as f:
#     csv_reader = csv.reader(f, delimiter='-')
#     for line in csv_reader:
#         print(line)

# Using DictReader and DictWriter
# with open('names.csv', 'r') as csv_read:
#     csv_reader = csv.DictReader(csv_read)
#     for line in csv_reader:
#         # print(line)
#         print(line['email'])

# with open('names.csv','r') as csv_readfile:
#     csv_reader = csv.DictReader(csv_readfile)
#     with open('new_names.csv', 'w') as csv_writefile:
#         field_names = ['first_name', 'last_name', 'email']
#         csv_writer = csv.DictWriter(csv_writefile, fieldnames=field_names, delimiter='\t')
#         csv_writer.writeheader()
#         for line in csv_reader:
#             csv_writer.writerow(line)

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('new_names.csv', 'w') as new_file:
#         fieldnames = ['first_name', 'last_name']
#
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             del line['email']
#             csv_writer.writerow(line)

# Date Time Module
# import datetime
# d = datetime.date(2023, 11, 16)
# print(d)
# today = datetime.date.today()
# print(today)
# print(today.day)
# print(today.year)
# print(today.month)
# print(today.weekday()) #Monday 0 Sunday 6
# print(today.isoweekday()) #Monday 1 Sunday 7
# tdelta = datetime.timedelta(days=7)
# print(today - tdelta) #2023-11-14
# print(today + tdelta) #2023-11-28
# date2 = date1 + tdelta
# tdelta = date1 + date2
# bday = datetime.date(2024, 10, 24)
# till_bday = bday - today
# print(till_bday) #338 days, 0:00:00
# print(till_bday.days) #338
# print(till_bday.total_seconds()) #29203200.0
# time = datetime.time(10, 40, 50, 10000)
# print(time) #10:40:50.010000
# print(time.hour) #10
# dt = datetime.datetime(2019, 2, 15, 8, 45, 50, 10000)
# print(dt) #2019-02-15 08:45:50.010000
# print(dt.date()) #2019-02-15
# print(dt.time()) #08:45:50.010000
# print(dt.year) #2019
# print(dt + tdelta) #2019-02-22 08:45:50.010000
# tdelta = datetime.timedelta(hours=12)
# print(dt + tdelta) #2019-02-15 20:45:50.010000
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today) #2023-11-21 07:28:55.302574
# print(dt_now) #2023-11-21 07:28:55.302574
# print(dt_utcnow) #2023-11-21 01:58:55.310627

# itertools
import itertools

# count = itertools.count()
# print(next(count)) #0
# print(next(count)) #1
# print(next(count)) #2
# print(next(count)) #3
# count = itertools.count(start=5, step=5)
# print(next(count)) #5
# print(next(count)) #10
# print(next(count)) #15
# print(next(count)) #20
# count = itertools.count(start=5, step=-2.5)
# print(next(count)) #5
# print(next(count)) #2.5
# print(next(count)) #0.0
# print(next(count)) #-2.5

# l = [100, 200, 300, 400]
# data = list(zip(itertools.count(), l))
# print(data) #[(0, 100), (1, 200), (2, 300), (3, 400)]
# data = list(zip(range(7), l))
# print(data) #[(0, 100), (1, 200), (2, 300), (3, 400)]
# data = list(itertools.zip_longest(range(7), l))
# print(data) #[(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None)]

# counter = itertools.cycle([1, 2, 3])
# print(next(counter)) #1
# print(next(counter)) #2
# print(next(counter)) #3
# print(next(counter)) #1
#
# counter = itertools.cycle(('On', 'Off'))
# print(next(counter)) #On
# print(next(counter)) #Off
# print(next(counter)) #On

# counter = itertools.repeat(2)
# print(next(counter)) #2
# print(next(counter)) #2
# print(next(counter)) #2

# counter = itertools.repeat(2, times=2)
# print(next(counter)) #2
# print(next(counter)) #2
# print(next(counter)) #Error

# Finding Squares
# squares = list(map(pow, range(10), itertools.repeat(2)))
# print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
# print(list(squares)) #[0, 1, 4]

# l = ['a', 'b', 'c', 'd']
# Combination of values where order does not matters
# result = itertools.combinations(l, 2)
# print(list(result)) #[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
#
# # Combination of values where order matters
# result = itertools.permutations(l, 2)
# print(list(result)) #[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]

# l = [1, 2, 3]
# result = itertools.product(l, repeat=3)
# print(list(result))
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1), (3, 3, 2), (3, 3, 3)]

# l = [1, 2, 3]
# result = itertools.combinations_with_replacement(l, 3)
# print(list(result)) #[(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]

# letters = [1, 2]
# alphabets = ['a', 'b']
# names = ['Raji', 'Palla']
# result = letters + alphabets + names
# print(result)
# result = itertools.chain(letters, alphabets, names)
# for item in result:
#     print(item)

# result = itertools.islice(range(10), 5)
# print(list(result)) #[0, 1, 2, 3, 4]
# result = itertools.islice(range(10), 1, 5)
# print(list(result)) #[1, 2, 3, 4]
# result = itertools.islice(range(10), 1, 5, 2)
# print(list(result)) #[1, 3]

# with open('test.log', 'r') as f:
#     header = itertools.islice(f, 3)
#     for line in header:
#         print(line, end='')

# l = ['a', 'b', 'c', 'd']
# selectors = [True, True, False, True]
# result = itertools.compress(l, selectors)
# print(list(result)) #['a', 'b', 'd']

# def lessthan2(n):
#     if n < 2:
#         return True
#     return False
# numbers = [0, 1, 2, 3, 4]
# result = filter(lessthan2, numbers)
# print(list(result)) #[0, 1]
# result = itertools.filterfalse(lessthan2, numbers)
# print(list(result)) #[2, 3, 4]
#
# numbers = [0, 1, 2, 3, 2, 1, 0]
# result = itertools.dropwhile(lessthan2, numbers)
# print(list(result)) #[2, 3, 2, 1, 0]
# result = itertools.takewhile(lessthan2, numbers)
# print(list(result)) #[0, 1]

# numbers = [1, 2, 3, 4]
# result = itertools.accumulate(numbers)
# print(list(result)) #[1, 3, 6, 10] running_sum
#
# import operator
# result = itertools.accumulate(numbers, operator.mul)
# print(list(result)) #[1, 2, 6, 24] running product

'''list of people'''
# people = [
#     {
#         'name': 'John Doe',
#         'city': 'Gotham',
#         'state': 'NY'
#     },
#     {
#         'name': 'Jane Doe',
#         'city': 'Kings Landing',
#         'state': 'NY'
#     },
#     {
#         'name': 'Corey Schafer',
#         'city': 'Boulder',
#         'state': 'CO'
#     },
#     {
#         'name': 'Al Einstein',
#         'city': 'Denver',
#         'state': 'CO'
#     },
#     {
#         'name': 'John Henry',
#         'city': 'Hinton',
#         'state': 'WV'
#     },
#     {
#         'name': 'Randy Moss',
#         'city': 'Rand',
#         'state': 'WV'
#     },
#     {
#         'name': 'Nicole K',
#         'city': 'Asheville',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jim Doe',
#         'city': 'Charlotte',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jane Taylor',
#         'city': 'Faketown',
#         'state': 'NC'
#     }
# ]

# def get_state(person):
#     return person['state']
# #
# result = itertools.groupby(people, get_state)
# for key, group in result:
#     print(key)
#     for item in group:
#         print(item)
#     print('')

# for key, group in result:
#     print(key, len(list(group)))

# copy_1, copy_2 = itertools.tee(result)
# for key, group in copy_1:
#     print(key, group)


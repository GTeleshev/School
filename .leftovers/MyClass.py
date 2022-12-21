import ConnectDb
import User
import teacher
import Session
from tabulate import tabulate

user = User.User(1)

print(user.get_firstname())
print(user.get_lastname())

connect = ConnectDb.ConnectDb()

data = connect.select_columns_where('Tasks', 'TaskID', 'TeacherID', 2)

table_id = 'Reports'
num = 1
data = connect.select_where(table_id, 'TaskID', num)
print(data)
data.insert(0, ('ReportID', 'TaskID', 'Comment', 'Mark'))
print(data)
print(tabulate(data))
# print('среднегеом: ', (3 * 4 * 5) ** (1/3))
# Поля таблицы Tasks: 'TaskID', 'Name', 'DueDay', 'DueMonth', 'SubjectID',
# 'StudentID', 'TeacherID', 'Feedback'
#
# data = connect.select_columns_where('Tasks', 'TaskID, SubjectID, StudentID, Name, DueMonth, DueDay, TeacherID', 'TeacherID', 2)
# data.insert(0, ('TaskID', 'SubjectID', 'StudentID', 'Name', 'DueMonth', 'DueDay', 'TeacherID'))
# print(tabulate(data))

# connect.update_where(table='Users', columns='Password',
#                      values='000', where='UserID', wherevalue='7')
#
# data = connect.get_tables()
# print('Tables: ', data)
#
# tablename = 'Users'
#
# columns1 = connect.get_columns(table=tablename)
# print('Columns: ', columns1)
#
# data_select = connect.select_from_table(table=tablename)
# print(f'Select from {tablename}: ', data_select)
# print(type(data_select))
# print(len(data_select))
# for item in data_select:
#     print(item[1])
# data_where = connect.select_where(table=tablename, column='UserID', value='1')
# print(data_where)




# dat = connect.select_from_table('Users')
# headers = connect.get_columns('Users')
# dat.insert(0, headers)


# for row in dat:
#     maxlen = 0
#     for el in row:
#         if len(str(el)) > maxlen:
#             maxlen = len(str(el))
#
# column_width = maxlen + 5
# separator = "-"
#
# for row in dat:
#     elrow = "|"
#
#     count = 1
#     for el in row:
#         count += 1
#         elrow = elrow + str(el).ljust(column_width, " ") + "|"
#     print(elrow)
#
# print(separator * column_width * count)






# connect.insert_in_table(tablename, "Login, Password", "'teacher1', '777'")
# print(connect.select_from_table(tablename))

#
# Добавление пользователя:
# us_er = input('Введите логин пользователя: ')
# pass_word = input('Введите пароль: ')
# type_id = input('Введите тип пользователя: ')
#
# print(f"User: {us_er}, password: {pass_word}, Type: {type_id}")
#
# cols_str = "Login, Password, TypeID"
# vals_str = "'" + str(us_er) + "', '" + str(pass_word) + "', '" + str(type_id) + "'"
# connect.insert_in_table(tablename, cols_str, vals_str)
# print(connect.select_from_table(tablename))

# data3 = zip(columns1, *data_select)
# print(*data3)
# import User
# import sqlite3
# import datetime
#
# schoolDB = sqlite3.connect('School.db')
# cursor = schoolDB.cursor()
# current_time = datetime.datetime.now()
#
# cursor.execute("INSERT INTO Session (UserID, Start) Values (0, 'Now')")


# # Illustration of creating a class
# # in Python with input from the user
# class Student:
#     'A student class'
#     stuCount = 0
#
#     # initialization or constructor method of
#     def __init__(self):
#
#         # class Student
#         self.name = input('enter student name:')
#         self.rollno = input('enter student rollno:')
#         Student.stuCount += 1
#
#     # displayStudent method of class Student
#     def displayStudent(self):
#         print("Name:", self.name, "Rollno:", self.rollno)
#
#
# stu1 = Student()
# stu2 = Student()
# stu3 = Student()
# stu1.displayStudent()
# stu2.displayStudent()
# stu3.displayStudent()
# print('total no. of students:', Student.stuCount)
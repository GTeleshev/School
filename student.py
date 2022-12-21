import Session
import ConnectDb
import User
from tabulate import tabulate


class student:
    def __init__(self, user, session):
        self.user = user
        self.session = session
        self.connect = ConnectDb.ConnectDb()
        self.main_menu()

    def check_numeric(message, min_, max_):
        out = -100
        check = False
        while not check or out > max_ or out < min_:
            str_out = input(message)
            if not str_out.isdigit():
                check = False
            else:
                out = int(str_out)
                check = True
        return out

    def check_menu(opt=1):
        print(f'Работает функция #{opt}')

    def print_subjects(self):
        table_name = 'Subjects'
        self.connect.print_with_headers(table_name)

    def print_table_columns(self):
        table_to_print = input('Введите название таблицы: ')
        data = self.connect.get_columns(table_to_print)
        print(data)

    def print_tasks(self):
        table_name = 'Tasks'
        data = self.connect.select_columns_where('Tasks', 'TaskID, SubjectID, TeacherID, Name, DueMonth, DueDay',
                                                 'StudentID', self.user.UserID)
        data.insert(0, ('TaskID', 'SubjectID', 'Teacher', 'Name', 'DueMonth', 'DueDay'))
        print(tabulate(data))

    def check_reports(self):
        table_name = 'Reports'
        # self.
        self.connect.print_with_headers(table_name)

    def student_tasks(self):
        data = self.connect.select_columns_where('Tasks', 'TaskID', 'StudentID', self.user.UserID)
        lst = []
        for item in data:
            lst.append(item[0])
        return lst

    def check_menu(opt=1):
        print(f'Работает функция #{opt}')

    def create_create_report(self):
        table_name = 'Reports'
        task_id = input("Введите ID задания: ")
        comm = input("Введите комментарий (решение): ")
        self.connect.insert_in_table(table_name, 'TaskID, Comment', f"'{task_id}','{comm}'")

    def student_reports(self):
        student_tasks = self.student_tasks()
        table_name = 'Reports'
        for num in student_tasks:
            lst = self.connect.select_where(table_name, 'TaskID', num)
            lst.insert(0, ('ReportID','TaskID','Comment','Mark'))
            print('TaskID = ', num)
            print(tabulate(lst))

    def main_menu(self):
        print(f"Меню ученика: {0.1}")
        options = {1: "Показать список предметов",
                   2: "Вывести список заданий",
                   3: "Создать отчёт по заданию",
                   4: "Показать мои отчёты"}
        functions = {1: self.print_subjects,
                     2: self.print_tasks,
                     3: self.create_create_report,
                     4: self.student_reports}
        for iter in options.keys():
            print(iter, options[iter])
        option = student.check_numeric("Выберите действие: ", 1, 8)
        print("Выбрано: ", options[option])
        functions[option]()  # можно передавать без аргумента "()"
        user_dec = input('Продолжить - Enter, выйти - exit: ')
        if user_dec == 'exit':
            self.session.session_end()
            print('\n' * 150)
            new_session = Session.Session()
        else:
            student.main_menu(self)
        return option

import Session
import ConnectDb
import User
from tabulate import tabulate


class teacher:
    def __init__(self, user, session):
        self.user = user
        self.session = session
        self.connect = ConnectDb.ConnectDb()
        teacher.main_menu(self)

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

    def print_students(self):
        table_name = 'Users'
        data = self.connect.select_columns_where(table_name, 'lastname, firstname, UserID', 'TypeID', '3')
        data.insert(0, ('Lastname','Firstname','ID'))
        column_width = 5
        for row in data:
            maxlen = 0
            for el in row:
                if len(str(el)) > maxlen:
                    maxlen = len(str(el))
            column_width = maxlen + 5
        for row in data:
            elrow = ""
            for el in row:
                elrow = elrow + str(el).ljust(column_width, " ")
            print(elrow)

    def print_subjects(self):
        table_name = 'Subjects'
        self.connect.print_with_headers(table_name)

    def print_table_list(self):
        data = self.connect.get_tables()
        print(data)

    def print_table_columns(self):
        table_to_print = input('Введите название таблицы: ')
        data = self.connect.get_columns(table_to_print)
        print(data)

    def create_task(self):
        # Поля таблицы Tasks: 'TaskID', 'Name', 'DueDay', 'DueMonth', 'SubjectID',
        # 'StudentID', 'TeacherID', 'Feedback'
        table_name = 'Tasks'
        self.print_subjects()
        subject_id = input('Введите ID предмета: ')
        theme = input('Введите тему задания: ')
        student_id = input('Введите ID ученика: ')
        due_month = input('Введите дату сдачи (месяц): ')
        due_day = input('Введите дату сдачи (день): ')
        self.connect.insert_in_table(table_name, 'SubjectID, Name, StudentID, DueMonth, DueDay, TeacherID',
                                     f"'{subject_id}', '{theme}', '{student_id}', {due_month}, {due_day}, {self.user.UserID}")
    def print_tasks(self):
        table_name = 'Tasks'
        data = self.connect.select_columns_where('Tasks', 'TaskID, SubjectID, StudentID, Name, DueMonth, DueDay', 'TeacherID', self.user.UserID)
        data.insert(0, ('TaskID', 'SubjectID', 'StudentID', 'Name', 'DueMonth', 'DueDay'))
        print(tabulate(data))

    def check_reports(self):
        print("")
        self.connect.print_with_headers('Reports')

    def teacher_tasks(self):
        data = self.connect.select_columns_where('Tasks', 'TaskID', 'TeacherID', self.user.UserID)
        lst = []
        for item in data:
            lst.append(item[0])
        print(lst)
        return lst


    def check_reports(self):
        teacher_tasks = self.teacher_tasks()
        table_name = 'Reports'
        for num in teacher_tasks:
            lst = self.connect.select_where(table_name, 'TaskID', num)
            lst.insert(0, ('ReportID','TaskID','Comment','Mark'))
            print('TaskID = ', num)
            print(tabulate(lst))

    def main_menu(self):
        print(f"Меню учителя: {0.1}")
        options = {1: "Показать список учеников",
                   2: "Показать список предметов",
                   3: "Создать задание",
                   4: "Вывести список заданий",
                   5: "Проверить выполненные задания"}
        functions = {1: self.print_students,
                     2: self.print_subjects,
                     3: self.create_task,
                     4: self.print_tasks,
                     5: self.check_reports}
        for iter in options.keys():
            print(iter, options[iter])
        option = teacher.check_numeric("Выберите действие: ", 1, 8)
        print("Выбрано: ", options[option])
        functions[option]()  # можно передавать без аргумента "()"
        user_dec = input('Продолжить - Enter, выйти - exit: ')
        if user_dec == 'exit':
            self.session.session_end()
            print('\n' * 150)
            new_session = Session.Session()
        else:
            teacher.main_menu(self)
        return option

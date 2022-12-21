import Session
import ConnectDb


class SysAdmin:
    def __init__(self, user, session):
        self.user = user
        self.session = session
        self.connect = ConnectDb.ConnectDb()
        SysAdmin.main_menu(self)

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

    def print_users(self):
        table_name = 'Users'
        self.connect.print_with_headers(table_name)

    def add_user(self):
        user_login = input('Введите логин: ')
        user_password = input('Введите пароль: ')
        user_type = input('Введите роль пользователя (1 - администратор, 2 - учитель, 3 - ученик): ')
        firstname = input('Введите имя: ')
        lastname = input('Введите фамилию: ')
        connstring1 = 'Login, Password, Firstname, Lastname, TypeId'
        connstring2 = f"'{user_login}','{user_password}','{firstname}','{lastname}','{user_type}'"
        self.connect.insert_in_table('Users', connstring1, connstring2)
        self.print_users()

    def delete(self):
        UserID = input('Введите ID пользователя: ')
        self.connect.delete_where('Users', 'UserID', UserID)
        self.print_users()

    def change_user(self):
        UserID = input('Введите ID пользователя: ')
        newpass = input('Введите новый пароль: ')
        self.connect.update_where(table='Users', column='Password',
                                  values=str(newpass), where='UserID', wherevalue=UserID)
        self.print_users()

    def print_table_list(self):
        data = self.connect.get_tables()
        print(data)

    def print_table_columns(self):
        table_to_print = input('Введите название таблицы: ')
        data = self.connect.get_columns(table_to_print)
        print(data)

    def print_table_with_columns(self):
        table_to_print = input('Введите название таблицы: ')
        self.connect.print_with_headers(table_to_print)

    def flush_table(self):
        table_to_flush = input('Введите название таблицы: ')
        self.connect.flush_table(table_to_flush)
        self.connect.update_where(table='sqlite_sequence', column='seq',
                                  values='0', where='name', wherevalue=table_to_flush)

    def main_menu(self):
        print(f"Меню администратора: {0.1}")
        options = {1: "Показать список пользователей",
                   2: "Добавить пользователя",
                   3: "Удалить пользователя",
                   4: "Изменить пароль пользователя",
                   5: "Вывести все таблицы базы",
                   6: "Вывести поля таблицы",
                   7: "Печатать таблицу с заголовками",
                   8: "Очистить таблицу"}
        functions = {1: self.print_users,
                     2: self.add_user,
                     3: self.delete,
                     4: self.change_user,
                     5: self.print_table_list,
                     6: self.print_table_columns,
                     7: self.print_table_with_columns,
                     8: self.flush_table}
        for iter in options.keys():
            print(iter, options[iter])
        option = SysAdmin.check_numeric("Выберите действие: ", 1, 8)
        print("Выбрано: ", options[option])
        functions[option]()  # можно передавать без аргумента "()"
        user_dec = input('Продолжить - Enter, выйти - exit: ')
        if user_dec == 'exit':
            self.session.session_end()
            print('\n' * 150)
            new_session = Session.Session()
        else:
            SysAdmin.main_menu(self)
        return option

import User
import sqlite3
import datetime
import uuid
import sysadmin
import teacher
import student
import ConnectDb

schoolDB = sqlite3.connect('School.db')
cursor = schoolDB.cursor()
current_time = datetime.datetime.now()


class Session:
    def __init__(self, session_ID=None, session_type=None, userID=None, session_uuid=None):
        self.session_ID = session_ID
        self.session_type = session_type
        self.UserID = self.session_login()
        self.session_uuid = uuid.uuid4()
        if self.UserID is not None:
            cursor.execute(
                f"INSERT INTO Sessions (UserID, uuid, Start) Values ('{self.UserID}', '{self.session_uuid}', '{current_time}')")
            schoolDB.commit()
            session_user = User.User(self.UserID)
            print(f'Здравствуйте {session_user.get_lastname()} {session_user.get_firstname()}')
            if session_user.get_user_type() == '1':
                adm = sysadmin.SysAdmin(session_user, self)
            elif session_user.get_user_type() == '2':
                teach = teacher.teacher(session_user, self)
            elif session_user.get_user_type() == '3':
                stud = student.student(session_user, self)
            self.session_end()
            cursor.close()
            schoolDB.close()

    def session_end(self):
        end_time = datetime.datetime.now()
        print('Завершаем сессию: ', self.session_uuid)
        cursor.execute(f"""update Sessions set end = '{end_time}' where uuid = '{self.session_uuid}'""")
        schoolDB.commit()

    def session_login(self):
        while True:
            greeting = 'Добро пожаловать'
            print(greeting)
            print("-" * len(greeting))
            login = input('Введите имя пользователя (exit для выхода): ')
            cursor.execute(f"select * from Users where Login = '{login}'")
            row = cursor.fetchall()
            if login.lower() == 'exit':
                exit()
            elif not row and login.lower() != 'exit':
                print('Имя пользователя не существует')
            else:
                password = input('Введите пароль: ')
                if row[0][2] == password:
                    break
                else:
                    print('Неверный пароль')
        if row:
            self.UserID = row[0][0]
        else:
            self.UserID = None
        return self.UserID

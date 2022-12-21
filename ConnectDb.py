import sqlite3

dbname = 'School.db'


class ConnectDb:
    def __init__(self, name_file=dbname):
        self.connstring = f'{name_file}'

    def get_columns(self, table):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        columns_query = f"""PRAGMA table_info({table})"""
        cursor.execute(columns_query)
        data = cursor.fetchall()
        lst = []
        for item in data:
            lst.append(item[1])
        cursor.close()
        conn.close()
        return lst

    def get_tables(self):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        sql_query = """SELECT name FROM sqlite_master WHERE type='table'"""
        cursor.execute(sql_query)
        data = cursor.fetchall()
        lst = []
        for item in data:
            lst.append(item[0])
        cursor.close()
        conn.close()
        return lst

    def print_with_headers(self, table_name):
        select_data = self.select_from_table(table_name)
        headers = self.get_columns(table_name)
        select_data.insert(0, headers)
        for row in select_data:
            maxlen = 0
            for el in row:
                if len(str(el)) > maxlen:
                    maxlen = len(str(el))
            column_width = maxlen + 5
        for row in select_data:
            elrow = ""
            for el in row:
                elrow = elrow + str(el).ljust(column_width, " ")
            print(elrow)

    def select_from_table(self, table):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        data_select = cursor.execute(f'''SELECT * FROM {table};''')
        table_data = data_select.fetchall()
        cursor.close()
        conn.close()
        return table_data

    def select_where(self, table, column, value):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        data_select = cursor.execute(f"""SELECT * FROM {table} WHERE {column} = '{value}';""")
        table_data = data_select.fetchall()
        cursor.close()
        conn.close()
        return table_data

    def select_columns_where(self, table, columns, column, value):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        data_select = cursor.execute(f"""SELECT {columns} FROM {table} WHERE {column} = '{value}';""")
        table_data = data_select.fetchall()
        cursor.close()
        conn.close()
        return table_data

    def flush_table(self, table):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        cursor.execute(f'''DELETE FROM {table};''')
        conn.commit()
        conn.close()

    def insert_in_table(self, table, columns, values):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        dbstring = f'''INSERT INTO {table} ({columns}) VALUES ({values})'''
        cursor.execute(dbstring)
        conn.commit()
        conn.close()

    def delete_where(self, table, where, value):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        cursor.execute(f'''DELETE FROM {table} WHERE {where} = '{value}';''')
        conn.commit()
        conn.close()

    def update_where(self, table, column, values, where, wherevalue):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        dbstring = f"""Update {table} set {column} = '{values}' WHERE {where} = '{wherevalue}'"""
        cursor.execute(dbstring)
        conn.commit()
        conn.close()

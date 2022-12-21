import ConnectDb

connect = ConnectDb.ConnectDb()


class User:
    def __init__(self, UserID=None):
        self.UserID = UserID
        self.TypeID = self.get_user_type()
        print('UserID: ', self.UserID)
        print('TypeID: ', self.TypeID)


    def get_user_type(self):
        data = connect.select_where('Users', 'UserID', self.UserID)
        # print('get_user_type, data', data)
        if len(data[0]) > 5:
            return data [0][5]
        else:
            return None

    def get_lastname(self):
        data = connect.select_where('Users', 'UserID', self.UserID)
        # print('get_lastname, data', data[0][4])
        if len(data[0]) > 5:
            return data[0][4]
        else:
            return None

    def get_firstname(self):
        data = connect.select_where('Users', 'UserID', self.UserID)
        # print('get_firstname, data', data[0][3])
        return data[0][3]

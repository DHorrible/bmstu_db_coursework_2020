import mysql.connector as conn


class DataBase:
    def __init__(self,
                 host='localhost',
                 port=3307,
                 user='root',
                 password='02042000'):
        self.__conn = conn.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            database='bank'
        )
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.close()

    def select_table(self, table, *fields):
        self.__cursor.execute(str.format(
            'select\n' +
            ('*' if len(fields) == 0 else ('`t`.`{}`' + ',`t`.`{}`' * (len(fields) - 1))) + '\n' +
            'from `' + table + '` as `t`', *fields))
        return tuple(x for x in self.__cursor)

    def exec(self, cmd):
        self.__cursor.execute(cmd)
        ret = tuple(x for x in self.__cursor)
        if len(ret) == 1:
            all_none = True
            for x in ret[0]:
                if x is not None:
                    all_none = False
                    break
            if all_none:
                return None
        return ret

    def call_procedure(self, procedure, args=''):
        return self.exec(
            str.format('call %s(%s)',
                       procedure,
                       args))

    def call_function(self, function, args=''):
        return self.exec(
            str.format('select %s(%s)',
                       function,
                       args))

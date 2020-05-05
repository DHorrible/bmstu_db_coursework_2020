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
            database='port'
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

    def get_result(self, is_proc=False):
        if is_proc:
            res = self.__cursor.stored_results()
            last = None
            for x in res:
                last = x
            if last is None:
                return None, None
            ret = tuple(x for x in last)
            met = last.column_names
        else:
            ret = tuple(x for x in self.__cursor)
            met = self.__cursor.column_names
        if len(ret) == 0:
            return None, None
        if len(ret) == 1:
            all_none = True
            for x in ret[0]:
                if x is not None:
                    all_none = False
                    break
            if all_none:
                return None, None
        return ret, met

    def exec(self, cmd):
        try:
            self.__cursor.execute(cmd)
        except conn.Error:
            return None, None
        return self.get_result()

    def call_procedure(self, procedure, *args):
        try:
            self.__cursor.callproc(procedure, list(args))
        except conn.Error:
            return None, None
        return self.get_result(is_proc=True)

    def call_function(self, function, args=''):
        return self.exec(f'select {function}({args})')

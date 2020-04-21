import mysql.connector as conn


class DataBase:
    def __init__(self,
                 host='localhost',
                 port=3307,
                 user='root',
                 password='02042000'):
        self._conn = conn.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            database='bank'
        )
        self._cursor = self._conn.cursor()

    def select_table(self, table, *fields):
        self._cursor.execute(str.format(
            'select\n' +
            ('*' if len(fields) == 0 else ('`t`.`{}`' + ',`t`.`{}`' * (len(fields) - 1))) + '\n' +
            'from `' + table + '` as `t`', *fields))
        return tuple(x for x in self._cursor)

    def exec(self, cmd):
        self._cursor.execute(cmd)
        return tuple(x for x in self._cursor)

    def call_procedure(self, procedure):
        self._cursor.execute('call ' + procedure)
        return tuple(x for x in self._cursor)

    def call_function(self, procedure):
        self._cursor.execute('select ' + procedure)
        return tuple(x for x in self._cursor)

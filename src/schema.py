import src.utility as utility


class TableMetadata:
    def __init__(self, table_name):
        self.__table_name = utility.copy_str(table_name)
        self.__attrs = []
        self.__attr_map = dict()
        self.__end_table = False

    # Add attribute in table metadata (don't use method)
    def add_attr(self, attr_name, attr_type):
        if not self.__end_table:
            self.__attrs.append({
                'name': attr_name,
                'type': attr_type
            })
            self.__attr_map[attr_name] = self.__attrs[len(self.__attrs) - 1]
            self.__setattr__(attr_name, utility.copy_str(attr_name))

    # Disable adding into table metadata (don't use method)
    def end_table(self):
        self.__end_table = True

    # Get number of attributes
    @property
    def count_attr(self):
        return len(self.__attrs)

    # Check the existence of an attribute in a table
    def exist_attr(self, attr_name):
        return attr_name in self.__attr_map

    # Get attributes tuple
    @property
    def attrs(self):
        return tuple([attr['name'] for attr in self.__attrs])

    # Get table name
    @property
    def table_name(self):
        return utility.copy_str(self.__table_name)

    # Get attribute type
    def get_attr_type(self, attr_name):
        attr = self.__attr_map.get(attr_name)
        return None if attr is None else utility.copy_str(attr['type'])


# Client table
client = TableMetadata('client')
client.add_attr('id', 'integer')
client.add_attr('firstname', 'varchar(45)')
client.add_attr('secondname', 'varchar(45)')
client.add_attr('birthday', 'date')
client.add_attr('phone', 'varchar(14)')
client.add_attr('address', 'varchar(45)')
client.add_attr('date', 'date')
client.end_table()

# Account table
account = TableMetadata('account')
account.add_attr('id', 'integer')
account.add_attr('client_id', 'integer')
account.add_attr('currency_id', 'integer')
account.add_attr('balance', 'float')
account.add_attr('changed', 'datetime')
account.end_table()

# Account history table
account_history = TableMetadata('account_history')
account_history.add_attr('id', 'integer')
account_history.add_attr('account_id', 'integer')
account_history.add_attr('old_balance', 'float')
account_history.add_attr('balance', 'float')
account_history.add_attr('reason_id', 'integer')
account_history.add_attr('datetime', 'datetime')
account_history.end_table()

# Transaction history table
transaction_history = TableMetadata('transaction_history')
transaction_history.add_attr('id', 'integer')
transaction_history.add_attr('from_account_id', 'integer')
transaction_history.add_attr('to_account_id', 'integer')
transaction_history.add_attr('currency_rate_id', 'integer')
transaction_history.add_attr('amount', 'float')
transaction_history.add_attr('datetime', 'datetime')
transaction_history.end_table()

# Currency table
currency = TableMetadata('currency')
currency.add_attr('id', 'integer')
currency.add_attr('name', 'varchar(3)')
currency.end_table()

# Reason table
reason = TableMetadata('reason')
reason.add_attr('id', 'integer')
reason.add_attr('name', 'varchar(128)')
reason.end_table()

# Currency rate table
currency_rate = TableMetadata('currency_rate')
currency_rate.add_attr('id', 'integer')
currency_rate.add_attr('sell_id', 'integer')
currency_rate.add_attr('buy_id', 'integer')
currency_rate.add_attr('amount', 'float')
currency_rate.add_attr('datetime', 'datetime')
currency_rate.end_table()

# Reports table
reports = TableMetadata('reports')
reports.add_attr('row_id', 'integer')
reports.add_attr('id', 'varchar(36)')
reports.add_attr('account_id', 'integer')
reports.add_attr('currency_id', 'integer')
reports.add_attr('expenses', 'float')
reports.add_attr('incomes', 'float')
reports.add_attr('month', 'integer')
reports.add_attr('year', 'integer')
reports.end_table()

# Report info table
report_info = TableMetadata('report_info')
report_info.add_attr('id', 'integer')
report_info.add_attr('report_id', 'integer')
report_info.add_attr('client_id', 'integer')
report_info.add_attr('last_update', 'datetime')
report_info.end_table()


tables = (
    client,
    account,
    account_history,
    transaction_history,
    currency,
    reason,
    currency_rate,
    reports,
    report_info,
)


# Queries
query_1 = TableMetadata('query_1')
query_1.add_attr('month', 'integer')
query_1.add_attr('transactions', 'integer')
query_1.end_table()

query_2 = TableMetadata('query_2')
query_2.add_attr('id', 'integer')
query_2.add_attr('transactions', 'integer')
query_2.end_table()

query_3 = TableMetadata('query_3')
query_3.add_attr('account_id', 'integer')
query_3.add_attr('currency_name', 'varchar(45)')
query_3.add_attr('income', 'float')
query_3.end_table()

query_4 = client

query_5 = account

query_6 = account

queries = (
    query_1,
    query_2,
    query_3,
    query_4,
    query_5,
    query_6,
)

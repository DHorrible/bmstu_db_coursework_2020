import src.utility as utility


class TableMetadata:
    def __init__(self, table_name):
        self._table_name = utility.copy_str(table_name)
        self._attrs = []
        self._attr_map = dict()
        self._end_table = False

    # Add attribute in table metadata (don't use method)
    def add_attr(self, attr_name, attr_type):
        if not self._end_table:
            self._attrs.append({
                'name': attr_name,
                'type': attr_type
            })
            self._attr_map[attr_name] = self._attrs[len(self._attrs) - 1]

    # Disable adding into table metadata (don't use method)
    def end_table(self):
        self._end_table = True

    # Get number of attributes
    def count_attr(self):
        return len(self._attrs)

    # Check the existence of an attribute in a table
    def exist_attr(self, attr_name):
        return attr_name in self._attr_map

    # Get attributes tuple
    def get_attrs(self):
        return tuple(utility.copy_str(attr['name']) for attr in self._attrs)

    # Get table name
    def get_table_name(self):
        return utility.copy_str(self._table_name)

    # Get attribute type
    def get_attr_type(self, attr_name):
        attr = self._attr_map.get(attr_name)
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


def get_tables():
    return (
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

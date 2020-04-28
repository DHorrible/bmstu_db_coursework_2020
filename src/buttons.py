class Button:
    def __init__(self, name, href, active=True):
        self._name = name
        self._href = href
        self._active = active

    def unset_active(self):
        self._active = False

    def set_active(self):
        self._active = True

    @property
    def name(self):
        return self._name

    @property
    def href(self, *args):
        return str.format(self._href, *args)

    @property
    def active(self):
        return self._active


# Queries
query_1 = Button('Показать отчет о переводах денег в заданном году', 'query/1')
query_2 = Button('Показать колличество переводов с каждого из счетов клиента по определенной фамилии', 'query/2')
query_3 = Button('Показать общую сумму переводов на заданый счет клиента', 'query/3')
query_4 = Button('Показать все сведения о самом молодом клиенте', 'query/4')
query_5 = Button('Показать все сведения о счетах, с которых ни разу не переводились деньги на другие счета', 'query/5')
query_6 = Button('''Показать все сведения о счетах, с которых ни разу не переводились
 деньги в заданом месяце заданного года''', 'query/6')

query_buttons = (
    query_1,
    query_2,
    query_3,
    query_4,
    query_5,
    query_6,
)

# Report
create_report = Button('создайте отчет', 'report')
update_report = Button('Обновить отчет', 'report/update/{}')
get_report = Button('Получить последний отчет', 'report/get/{}')

report_buttons = (
    create_report,
    update_report,
    get_report,
)

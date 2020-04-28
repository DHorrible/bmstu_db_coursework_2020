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


query_buttons = (
    Button('Показать отчет о переводах денег в заданном году', 'query/1'),
    Button('Показать колличество переводов с каждого из счетов клиента по определенной фамилии', 'query/2'),
    Button('Показать общую сумму переводов на заданый счет клиента', 'query/3'),
    Button('Показать все сведения о самом молодом клиенте', 'query/4'),
    Button('Показать все сведения о счетах, с которых ни разу не переводились деньги на другие счета', 'query/5'),
    Button('Показать все сведения о счетах, с которых ни разу не переводились\
            деньги в заданом месяце заданного года', 'query/6'),
)

report_buttons = (
    Button('Обновить отчет', 'report/update/{}'),
    Button('Получить последний отчет', 'report/get/{}'),
)

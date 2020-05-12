import src.buttons as buttons
import src.utility as utility
from src.database import DataBase
from flask import Flask, request, render_template

app = Flask(__name__)
db = DataBase()


@app.route('/')
def main_page():
    return render_template('index.html',
                           query_buttons=buttons.query_buttons,
                           to_report_button=buttons.create_report)


@app.route('/query/<int:num>', methods=['GET', 'POST'])
def exec_query(num):
    if num < 0 or num > 6:
        return '{"status": "error", "msg": "incorrect number"}'
    if num == 3 and request.method == 'GET':
        return render_template('query_form.html')
    query = utility.get_query(num)
    if num == 3 and request.method == 'POST':
        query = str.format(query, request.form['account_id'])
    res, met = db.exec(query)
    return render_template('table.html',
                           result=res,
                           metadata=met,
                           error='Нет данных, удволетворяющих запросу')


@app.route('/report', methods=['GET', 'POST'])
def update_report():
    if request.method == 'POST':
        client_id = request.form['client_id']
        db.call_procedure('update_report', client_id)
        res, met = db.call_procedure('get_last_report', client_id)
        return render_template('table.html',
                               result=res,
                               metadata=met,
                               error='Нет клиента с таким номером договора')
    else:
        return render_template('report_form.html')


if __name__ == '__main__':
    app.run()

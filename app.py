import src.buttons as buttons
import src.utility as utility
import src.schema as schema
from src.database import DataBase
from flask import Flask, request, render_template

app = Flask(__name__)
db = DataBase()


@app.route('/')
def main_page():
    return render_template('index.html',
                           query_buttons=buttons.query_buttons,
                           to_report_button=buttons.create_report)


@app.route('/query/<int:num>')
def exec_query(num):
    if num < 0 or num > 6:
        return '{"status": "error", "msg": "incorrect number"}'
    return render_template('table.html',
                           result=db.exec(utility.get_query(num)),
                           metadata=schema.queries[num - 1].attrs)


@app.route('/function')
def exec_func(name):
    # args = request.args.get('args', type=str, default='')
    # res = db.call_function(name, args)
    return '{"status": "ok", "msg": "coming soon"}'


@app.route('/report', methods=['GET', 'POST'])
def update_report():
    client_id = request.args.get('client_id')
    if request.method == "POST":
        client_id = request.args.get('client_id')
        db.call_procedure('update_report', client_id)
        return render_template('table.html',
                               result=db.call_procedure('get_last_report', client_id),
                               metadata=schema.reports.attrs)
    else:
        return render_template('report_form.html')


if __name__ == '__main__':
    app.run()

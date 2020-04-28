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
                           buttons=buttons.query_buttons)


@app.route('/query/<int:num>')
def exec_query(num):
    if num < 0 or num > 6:
        return '{"status": "wrong", "error": "incorrect number"}'
    return render_template('table.html',
                           result=db.exec(utility.get_query(num)),
                           metadata=schema.get_queries()[num - 1].attrs)


@app.route('/function/<string:name>')
def exec_func(name):
    # args = request.args.get('args', type=str, default='')
    # res = db.call_function(name, args)
    return '{"status": "ok", "text": "coming soon"}'


@app.route('/report')
def report_page():
    return render_template('report.html')


@app.route('/report/update/<int:client_id>')
def update_report(client_id):
    db.call_procedure('update_report', str(client_id))
    return render_template('report.html')


@app.route('/report/get/<int:client_id>')
def get_report(client_id):
    res = db.call_procedure('get_last_report', str(client_id))
    return render_template('report.html')


if __name__ == '__main__':
    app.run()

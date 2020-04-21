from src.database import DataBase
from flask import Flask, request, render_template

app = Flask(__name__)
db = DataBase()


@app.route('/')
def main_page():
    pass


@app.route('/query/<int:num>')
def exec_query(num):
    res = db.exec('')
    pass


@app.route('/function/<string:name>')
def exec_func(name):
    args = request.args.get('args', type=str, default='')
    res = db.call_function(name, args)
    pass


@app.route('/report')
def report_page():
    pass


@app.route('/report/update/<int:client_id>')
def update_report(client_id):
    db.call_procedure('update_report', str(client_id))
    pass


@app.route('/report/get/<int:client_id>')
def get_report(client_id):
    res = db.call_procedure('get_last_report', str(client_id))
    pass


if __name__ == '__main__':
    app.run()

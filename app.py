from src.database import DataBase
from flask import Flask, request, render_template

app = Flask(__name__)
db = DataBase()

query = '''
    select
        `e`.*
    from `employee` as `e`
    left join `port_history` as `ph`
        on `e`.`id` = `ph`.`employee_id`
    group by `e`.`id`
    having min(
        `ph`.`id` is null
        or not (year(`ph`.`arrival`) = {} 
            and month(`ph`.`arrival`) = {})) = true
'''


@app.route('/', methods=['GET', 'POST'])
def update_report():
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        res, met = db.exec(str.format(query, year, month))
        return render_template('table.html',
                               result=res,
                               metadata=met,
                               error='Нет данных, удволетворяющих запросу')
    else:
        return render_template('query_form.html')


if __name__ == '__main__':
    app.run()

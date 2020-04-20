import src.schema as schema
from src.database import DataBase
from flask import Flask

app = Flask(__name__)


@app.route('/main')
def hello_world():
    db = DataBase()
    account = db.show_table('account')
    out = ''

    for x in account:
        out += str(x) + '\n'
    return out


if __name__ == '__main__':
    app.run()



import src.schema as schema
from src.database import DataBase
from flask import Flask, render_template

app = Flask(__name__)
db = DataBase()


@app.route('/')
def hello_world():
    account = db.select_table('account', schema.account.id, schema.account.client_id)
    out = ''

    for x in account:
        out += str(x) + '\n'
    return out


if __name__ == '__main__':
    app.run()

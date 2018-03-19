from flask import Flask

from database import db_session, init_db
from controllers import newspaper

app = Flask(__name__)

app.register_blueprint(newspaper.get_company)
app.register_blueprint(newspaper.save_company)

init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

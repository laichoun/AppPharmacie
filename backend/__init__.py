from flask import Flask

def create_app():
    app = Flask(__name__)
    # existing code omitted

    app.config.from_mapping(DATABASE='./instance/pharmaapp.sqlite')

    from . import db
    db.init_app(app)

    return app
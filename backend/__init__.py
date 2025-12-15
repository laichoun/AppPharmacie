from flask import Flask
from flask import request, jsonify
import sqlite3

def checkInDb(mol):
    conn = sqlite3.connect('./instance/pharmaapp.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM medecine WHERE molecule LIKE ?", (mol,))
    rows = c.fetchall()
    conn.close()
    return (rows)


def create_app():
    app = Flask(__name__)
    # existing code omitted

    app.config.from_mapping(DATABASE='./instance/pharmaapp.sqlite')

    from . import db
    db.init_app(app)

    @app.route('/api/search/med', methods=['GET'])
    def search():
        if 'molecule' in request.args:
            mol = request.args['molecule'] + "%"
            result = checkInDb(mol)
            return jsonify(result)
        else:
            return ("Error: No molecule entered")
    
    return app

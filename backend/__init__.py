from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import sqlite3

def checkInDb(mol):
    conn = sqlite3.connect('./backend/instance/pharmaapp.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM medecine WHERE molecule LIKE ?", (mol,))
    rows = c.fetchall()
    conn.close()
    result = [{"id": r[0], "molecule": r[1], "marque": r[2]} for r in rows]
    return result



def create_app():
    app = Flask(__name__)
    # existing code omitted
    CORS(app, origins=["http://localhost:5173"])

    app.config.from_mapping(DATABASE='./instance/pharmaapp.sqlite')

    from . import db
    db.init_app(app)

    @app.route('/api/search/med', methods=['GET'])
    def search():
        mol = request.args.get('molecule', '').strip()
    
        if mol:
            result = checkInDb(f"%{mol}%")  # ← Recherche PARTIELLE partout
            if not result:
                return jsonify({"error": "Aucun médicament trouvé"}), 404
            return jsonify(result)
        else:
            return jsonify({"error": "No molecule entered"}), 400
    # def search():
    #     #mol = request.args.get('molecule', '')
    #     #if (mol):

    #     if 'molecule' in request.args:
    #         mol = request.args['molecule'] + "%"
    #         result = checkInDb(mol)
    #         return jsonify(result)

    #     else:
    #         return jsonify({"error": "No molecule entered"}), 400
    
    return app

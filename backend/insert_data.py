import sqlite3

#ouvre le classeur
conn = sqlite3.connect('./instance/pharmaapp.sqlite')

#sert d'intermediaire à la db pour insérer, supprimer etc, exec des commandes à la db
c = conn.cursor()

medicaments = [
    ('Fluvastatine', 'LESCOL'),
    ('Pravastatine', 'ELISOR'),
    ('Rosuvastatine', 'CRESTOR'),
    ('Simvastatine', 'ZOCOR'),
    ('Atorvastatine/amlodipine', 'CADUET'),
    ('Atorvastatine/ézétimibe', 'LIPTRUZET'),
]

for mol, brand in medicaments:
    c.execute("SELECT id FROM medecine WHERE molecule = ?", (mol,))
    if (c.fetchone() is None):
        c.execute("INSERT INTO medecine (molecule, brand) VALUES (?, ?)", (mol, brand))

#ecrit definitivement sur le disque
conn.commit()

#repose le stylo et ferme le classeur 
conn.close()

print("Données insérées !")

import sqlite3

conn = sqlite3.connect('./instance/pharmaapp.sqlite')
c= conn.cursor()

c.execute('DELETE FROM medecine')

conn.commit()
conn.close()

print("Données effacées !")
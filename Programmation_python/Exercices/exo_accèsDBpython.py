import sys
import MySQLdb

#connexion au serveur Mysql

try:
    conn=MySQLdb.connect(host="localhost",
                         user="user",
                         passwd="password",
                         db="database")
except MySQL.db.Error,e:
    print("Erreur %d : %s" % (e.args[0],e.args[1])
    sys.exit(1)


#créé la table animal et peuple

try:
    cursor=conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS animal")
    cursor.execute("""CREATE TABLE animal
        (name CHAR(40), category CHAR(40))
        """)
    cursor.execute("""INSERT INTO animal (name, category)
        VALUES
            ("serpent, "reptile")"""


"""A finir"""

#boucle de récupération utilisant fetchall() -> Requête SELECT

cursor.execute("SELECT name, category FROM animal")
rows = cursor.fetchall()
for row in rows:
    print("%s, %s" % (row[0], row[1])
print("Nombre de lignes renvoyées : %d" % cursor.rowcount)

"""A finir"""

cursor.close()
conn.commit()
conn.close()

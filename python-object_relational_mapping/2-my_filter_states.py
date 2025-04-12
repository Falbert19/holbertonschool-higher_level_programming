#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Usage: ./2-my_filter_states.py <mysql_user> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Recoger argumentos
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Conectar a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Crear cursor y ejecutar consulta usando .format()
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Mostrar resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar conexión
    cur.close()
    db.close()

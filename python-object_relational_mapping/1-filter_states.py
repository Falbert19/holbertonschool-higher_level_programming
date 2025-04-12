#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Argumentos de conexión
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Conexión a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Cursor y ejecución del query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Mostrar resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar conexión
    cur.close()
    db.close()

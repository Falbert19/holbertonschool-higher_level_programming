#!/usr/bin/python3
"""
Safe script that displays all values in the states table where name matches the argument,
protecting against SQL injection.
Usage: ./3-my_safe_filter_states.py <mysql_user> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Argumentos
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Conexión segura
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Cursor y consulta segura usando parámetro
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Mostrar resultados
    for row in cur.fetchall():
        print(row)

    # Cierre
    cur.close()
    db.close()

#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa, with their state name.
Usage: ./4-cities_by_state.py <mysql_user> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Conectar a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Crear cursor
    cur = db.cursor()

    # Ejecutar solo una vez
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Mostrar resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar conexión
    cur.close()
    db.close()

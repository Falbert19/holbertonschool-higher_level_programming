#!/usr/bin/python3
"""
Lists all cities of a given state from
the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql_user>
<mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Conexión a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Crear cursor
    cur = db.cursor()

    # Ejecutar consulta segura y solo una vez
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Obtener resultados
    cities = cur.fetchall()

    # Mostrar como cadena separada por coma
    print(", ".join(city[0] for city in cities))

    # Cierre
    cur.close()
    db.close()

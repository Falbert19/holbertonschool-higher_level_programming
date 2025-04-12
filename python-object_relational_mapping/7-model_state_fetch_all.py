#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py
<mysql_user> <mysql_password> <database_name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Obtener argumentos
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Crear engine de conexión
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, db_name), pool_pre_ping=True)

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener todos los estados ordenados por id
    states = session.query(State).order_by(State.id).all()

    # Mostrar resultados
    for state in states:
        print(f"{state.id}: {state.name}")

    # Cerrar sesión
    session.close()

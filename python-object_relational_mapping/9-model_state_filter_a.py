#!/usr/bin/python3
"""
Lists all State objects that contain the
letter 'a' from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py
<mysql_user> <mysql_password> <database_name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Argumentos
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Conexión
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, db_name), pool_pre_ping=True)

    # Sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: estados con 'a' en el nombre
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Mostrar resultados
    for state in states:
        print(f"{state.id}: {state.name}")

    # Cerrar sesión
    session.close()

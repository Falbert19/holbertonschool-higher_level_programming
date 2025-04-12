#!/usr/bin/python3
"""
Prints the first State object
from the database hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py
<mysql_user> <mysql_password> <database_name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Recoger argumentos
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Crear engine y sesión
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener el primer estado por id
    first_state = session.query(State).order_by(State.id).first()

    # Imprimir resultado
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Cerrar sesión
    session.close()

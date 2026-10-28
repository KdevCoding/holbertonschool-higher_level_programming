#!/usr/bin/python3
"""print states from States table
"""
from sqlalchemy.orm import Session
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id)[0:1]:
        print("{}: {}".format(state.id, state.name))
    session.close()

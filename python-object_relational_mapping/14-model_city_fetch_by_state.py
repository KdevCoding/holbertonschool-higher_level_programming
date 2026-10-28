#!/usr/bin/python3
"""delete states containing a
"""
from sqlalchemy.orm import Session
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id)
    for state_name, city_id, city_name in query:
        print("{}: ({}) {}".format(state_name, city_id, city_name))
    session.commit()
    session.close()

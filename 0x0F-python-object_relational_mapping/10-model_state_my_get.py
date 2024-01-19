#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    match = sys.argv[4]
    state = session.query(State).filter(State.name == match).first()
    print("Not found" if not state else "{}".format(state.id))

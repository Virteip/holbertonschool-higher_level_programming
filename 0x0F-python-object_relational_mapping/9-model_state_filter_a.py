#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)

    for result in query:
        print("{}: {}".format(result.id, result.name))

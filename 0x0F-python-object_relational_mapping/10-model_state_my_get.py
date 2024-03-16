#!/usr/bin/python3
"""prints the State object with the name passed as argument"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state= session.query(State).filter(State.name == argv[4]).order_by(State.id).all()
    if state:
        print("{}".format(state[0].id))
    else:
        print("Not found")
    session.close()

#!/usr/bin/python3
"""List all states"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name="California" )
    new_city = City(name="San Francisco", state=new_state)
    new_state.cities.append(new_city)
    
    session.add(new_state)
    session.commit()
    session.close()

#!/usr/bin/python3
"""Lists States and Cities from DB"""
from sys import argv
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City

if __name__ == '__main__':
    ngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=ngine)
    sess = Sess()
    new_state = State(name='California')
    to_get = session.query(City).order_by(City.id).all()
    for city in to_get:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    sess.close()

#!/usr/bin/python3
"""Adds State and City to DB"""
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
    new_city = City(name='San Francisco', state=new_state)
    sess.add(new_city)
    sess.commit()
    sess.close()

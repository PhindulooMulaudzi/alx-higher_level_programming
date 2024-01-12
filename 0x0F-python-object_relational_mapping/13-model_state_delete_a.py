#!/usr/bin/python3
"""Adds 'a' state iteratively to DB"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    ngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=ngine)
    sess = Sess()
    states = sess.query(State).filter(State.name.contains('a')).all()
    for i in states:
        sess.delete(i)
    sess.commit()
    sess.close()

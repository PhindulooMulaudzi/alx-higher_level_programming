#!/usr/bin/python3
"""Adds a state to DB"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    ngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=ngine)
    sess = Sess()
    second = sess.query(State).filter_by(id=2).first()
    second.name = 'New Mexico'
    sess.commit()
    sess.close()

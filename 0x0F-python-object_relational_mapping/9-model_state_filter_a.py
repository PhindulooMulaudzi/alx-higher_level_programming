#!/usr/bin/python3
"""Lists States from a database"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    ngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=ngine)
    sess = Sess()
    for i in sess.query(State).order_by(State.id).all():
        if 'a' in i.name:
            print('{}: {}'.format(i.id, i.name))
    sess.close()

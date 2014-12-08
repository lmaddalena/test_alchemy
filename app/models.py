__author__ = 'maddalena'

from sqlalchemy import Column, Integer, String, Sequence
from app import modelbase


class User(modelbase):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(64))
    email = Column(String(120), index=True, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.email)

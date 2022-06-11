from sqlalchemy import Column, Integer, String
from db import Base

from .import hashing


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))

    def __init__(self, username, email, password, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)

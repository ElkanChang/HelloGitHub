#! /usr/bin/env python3
import os
import sys
import re

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,ForeignKey,Table,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

engine = create_engine('mysql://root:@localhost/test')
Base = declarative_base()
session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    email = Column(String(64))
    def__repr__(self):
        return'<User(name=%s)>'%self.name

class Stationery(Base):
    __tablename__ = 'stationery'
    item_id = Column(Integer,primary_key=True)
    item = Column(String(255))
    def__repr__(self):
        return'<Stationery(name=%s)>' % self.name

class History_book(Base):
    __tablename__ = 'history_book'
    id = Column(Integer,primary_key=True)
    username = Column(String(64))


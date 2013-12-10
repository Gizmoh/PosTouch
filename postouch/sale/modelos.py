# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, VARCHAR

Base = declarative_base()
Database = "sqlite///pos.db"


class Product(Base):
	__tablename__ = "product"

	id = Column(Integer, primary_key=True)
	name = Column(VARCHAR)
	gross_price = Column(VARCHAR)
	supplier_code = Column(VARCHAR)


class User(Base):
	__tablename__= "auth_user"

	id = Column(Integer, primary_key=True)
	username = Column(VARCHAR)
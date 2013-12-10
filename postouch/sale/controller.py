# -*- coding: utf-8 -*-

import sqlalchemy
import modelos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pos.db', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def get_products():
	"""
	Obtiene productos
	"""
	products = session.query(modelos.Product).filter(modelos.Product.id < 51)
	return products

def get_users():
	"""
	Obtiene Usuarios
	"""
	users = session.query(modelos.User)
	return users
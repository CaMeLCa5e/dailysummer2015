from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, create_session 

from flask import current_app 
import unittest 
from myapp import create_app 
from myapp.database import db_session, create_all, drop_all 

db_session = scoped_session(lambda: create_session(bind=current_app.db_engine))

class TestCase(unittest.TestCase):
	def setUp(self): 
		self.app = create_app("test.cfg")
		self.client = self.app.test_client()
		self.ctx = self.app.test_request_context()
		self.ctx.push()
		create_all()

	def tearDown(self):
		db_session.remove()
		drop_all()
		self.ctx.pop()

engine = None
sessionmaker = sa.orm.sessionmaker()
session = sa.orm.scoped_session(sessionmaker)

def configure_engine(url):
	global sessionmaker, engine, session 

	engine = sa.create_engine(url)
	session.remove()
	sessionmaker.configure(bind=engine)
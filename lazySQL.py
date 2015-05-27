from sqlalchemy import crete_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine("sqlite:///myapp.db")

# db_session = scoped_session(sessionmaker(bind=engine))

engine = None

db_session = scoped_session(lambda: create_session(bind=engine))

def init_engine(uri, **kwargs):
	global engine 
	engine = create_engine(uri, **kwargs)
	return engine

def create_app(config):
	app = Flask(__name__)
	app.config.from_pyfile(config)

	init_engine(app.config['DATABASE_URI'])

	return app  
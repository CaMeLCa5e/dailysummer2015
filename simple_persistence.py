from __future__ import with_statement 

import shelve 
from os import path 
from cPickle import HIGHEST_PROTOCOL 
from contextlib import closing

from flask import Flask 

SHELVE_DB = 'shelve.db'

app = Flask(__name__)
app.config.from_object(__name__)

db = shelve.open(path.join(app.root_path, app.config['SHELVE_DB'])
					protocol=HIGHEST_PROTOCOL.)
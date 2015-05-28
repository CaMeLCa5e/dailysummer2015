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
					protocol=HIGHEST_PROTOCOL, writeback=True)

@app.route('/<message>')
def write_and_list(message): 
	db.setdefault('messages', [])
	db['messages'].append(message)
	return app.response_class('\n'.join(db['messages']),
								mimetype='text/plain')

with closing(db): 
	app.run()
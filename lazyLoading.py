from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index(): 
	pass 

@app.route('/user/<username>')
def user(username): 
	pass 


import random
import string

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
   	search_username = request.args.get('name')
   	search_job = request.args.get('job')
   	if (search_username != None) & (search_job != None):
   		subdict = {'users_list' : []}
   		for user in users['users_list']:
   			if (user['name'] == search_username) & (user['job'] == search_job):
   				subdict['users_list'].append(user)
   		return subdict
   	elif search_username :
   		subdict = {'users_list' : []}
   		for user in users['users_list']:
   			if user['name'] == search_username:
   				subdict['users_list'].append(user)
   		return subdict
   	return users
   elif request.method == 'POST':
   	userToAdd = request.get_json()
   	userToAdd["id"] = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(6)])
   	users['users_list'].append(userToAdd)
   	resp = jsonify(userToAdd)
   	resp.status_code = 201
   	return resp
   elif request.method == 'DELETE':
   	userToDel = request.get_json()
   	for user in users['users_list']:
   		if user["name"] == userToDel["name"]:
   			users['users_list'].remove(user)
   			resp = jsonify(users['users_list'])
   			resp.status_code = 201
   			return resp
   	return jsonify(success=False)		



@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users

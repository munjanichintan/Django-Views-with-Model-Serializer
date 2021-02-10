import requests
import json

# URL = "http://localhost:8000/stuinfo/"
URL = "http://localhost:8000/stuinfoclass/"

def get_data(id=None):
	data = {}
	if id is not None:
		data = {'id': id}
	json_data = json.dumps(data)
	r = requests.get(url=URL, data=json_data)
	data = r.json()
	print(data)

# get_data(30)

def post_data():
	data = {
	   'name': 'Jack',
	   'roll': 35,
	   'city': 'Bhavnagar'
	}

	json_data = json.dumps(data)
	r = requests.post(url=URL, data=json_data)
	data = r.json()
	print(data)

# post_data()

def update_data():
	data = {
	   'id': 28,
	   'name': 'jack',
	   'roll': 109,
	   'city': 'Tokyo'
	}

	json_data = json.dumps(data)
	r = requests.put(url=URL, data=json_data)
	data = r.json()
	print(data)

update_data()

def delete_data():
	data = {'id': 24}

	json_data = json.dumps(data)
	r = requests.delete(url=URL, data=json_data)
	data = r.json()
	print(data)

# delete_data()
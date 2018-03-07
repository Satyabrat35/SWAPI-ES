import requests
import random
from flask import Flask,render_template,request
import json
from elasticsearch import Elasticsearch 
es = Elasticsearch([{'host':'localhost','port':9200}])
app = Flask(__name__)

#Peoples
i = 1
while res.status_code == 200:
	res = requests.get('https://swapi.co/api/people/' + str(i))
	es.index(index='sw',doc_type='people',id=i,body=json.loads(res.content))
	i = i + 1
	print(i)


#Planets		
i = 1
while res.status_code == 200:
	res = requests.get('https://swapi.co/api/planets/' + str(i))
	es.index(index='sw',doc_type='planets',id=i,body=json.loads(res.content))
	i = i + 1
	print(i)

#Starships
i = 1
while res.status_code == 200:
	res = requests.get('https://swapi.co/api/starships/' + str(i))
	es.index(index='sw',doc_type='starships',id=i,body=json.loads(res.content))
	i = i + 1
	print(i)


@app.route('/')
def status():
	res = requests.get('http://localhost:9200/')
	if res.status_code == 200:
		print('The Force is with u')	
		return render_template('base.html')	
	else:
		print('Bad day :(')


@app.route('/who')
def who():
	x = random.randint(1,89)
	data = es.get(index='sw',doc_type='people',id=x)
	print(data)
	return 'Hola'



if __name__ == "__main__":
	app.run(debug=True)
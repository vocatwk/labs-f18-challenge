import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>/')
def index(query):
	request = requests.get('http://pokeapi.co/api/v2/pokemon/' + query)

	# check if pokemon info for query exists
	if request.status_code != 200:
		return render_template('errorPage.html')

	if query.isnumeric():
		name = request.json()['name']
		return render_template('pokemonNameInfo.html', name=name, id=query)
	else:
		id = str(request.json()['id'])
		return render_template('pokemonIdInfo.html', name=query, id=id)

if __name__ == '__main__':
    app.run()

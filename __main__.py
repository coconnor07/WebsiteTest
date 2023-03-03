from flask import Flask, request, jsonify
from urllib.request import urlopen
import json

app = Flask(__name__, static_folder='game')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    message = data.get('message')

    message = input("response")

    response = {'status': 'success', 'message': message}

    return jsonify(response)

@app.route('/api/submit/setword', methods=['POST'])
def setWordOfTheDay():
    data = request.get_json()

    addWordToList(data.get('word'), data.get('definition'))

    return jsonify({ 'status': 'success' })

@app.route('/api/submit/getword', methods=['POST'])
def getWordOfTheDay():
    data = request.get_json()

    current = getCurrentWord()

    word = current.get('word')
    definition = current.get('definition')

    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word

    return jsonify({ 'status': 'success', 'word': word, 'definition': definition })

def addWordToList(word, definition):
    text = ''
    with open(r'wordOfTheDayList.txt', 'r') as file:
        text = file.read()
        text += ', ' + word + ':' + definition

    with open(r'wordOfTheDayList.txt', 'w') as file:
        file.write(text)

def getCurrentWord():
    with open(r'wordOfTheDayList.txt', 'r') as file:
        text = file.read()
        try:
            list = text.split(", ")
            list = list[len(list) - 1].split(":")
            word = list[0]
            definition = list[1]
            return { 'word': word, 'definition': definition }
        except:
            print(Exception('Parsing error'))
            return { 'word': 'error', 'definition': 'error' }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
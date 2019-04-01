#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

# load json file
with open('AVChanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']

@app.route('/')
def home():
    return jsonify (components)


@app.route('/<filename>')
def detail(filename): 
    

if __name__ == '__main__':
    app.run(debug=True)

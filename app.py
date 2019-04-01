#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

# load json file
with open('AVChanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']
print(type(components))


@app.route('/')
def home():
    return jsonify (components)


@app.route('/component')
def detail():
    x = []
    for c in components:
        for key, value in c.items():
            if key == 'name':
                x.append(value)

    return (str(x))


@app.route('/<component>')
def get_comp_attrs():
    pass


if __name__ == '__main__':
    app.run(debug=True)

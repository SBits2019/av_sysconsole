#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

# load json file
with open('avchanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']
print(type(components))


@app.route('/')
def home():
    return jsonify (components)


@app.route('/components')
def list_components():
    comps = []
    with open('avchanges/component_files.json') as f:
        data = json.load(f)
        for key, value in data.items():
           comps.append((key, value)) 

        return str(comps)


@app.route('/components/<det_component>')
def get_comp_attrs(det_component):
    x = []
    for c in components:
        for key, value in c.items():
            if key == 'name':
                x.append(value)

    # return (str(x))


if __name__ == '__main__':
    app.run(debug=True)

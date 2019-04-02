#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

# load json file
with open('avchanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']
print(len(components))


@app.route('/')
def home():
    return jsonify(components)


@app.route('/components')
def list_components():
    comps = []

    with open('avchanges/component_files.json') as f:
        data = json.load(f)

    comps = [(k, v) for k, v in data.items()]

    return jsonify(comps)


@app.route('/components/<det_component>')
def get_comp_attrs(det_component):
    return get_configfiles(det_component)


def get_configfiles(config_comp):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == config_comp:
                return jsonify([c['file_name'] for c in comp['config_files']])


if __name__ == '__main__':
    app.run(debug=True)

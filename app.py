#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# load json file
with open('avchanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']
print(len(components))
# print(type(components))


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
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == det_component:
                for c in comp['config_files']:
                    x.append(c['file_name'])

    return str(x) 

    #xml_name = components[0][det_component]
    #if os.path.exists('avchanges/'+xml_name):
     #   return 'exists'
    #else:
     #   return "not exists"


#    print(components['config_files']['file_name'])


if __name__ == '__main__':
    app.run(debug=True)

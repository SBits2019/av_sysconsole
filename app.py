#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify, render_template, url_for
import json
import os

app = Flask(__name__)

# load json file
with open('avchanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']
# print(type(components))


@app.route('/')
def home():
    return jsonify(components)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/components')
def list_components():
    component_list = []

    with open('avchanges/component_files.json') as f:
        data = json.load(f)

    for key, value in data.items():
        component_list.append((key, value))

    return render_template('components.html', components=component_list)


@app.route('/components/<detail_component>')
def get_comp_attrs(detail_component):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == detail_component:
                return render_template('comp_detail.html', component_files=[c['file_name'] for c in comp['config_files']])
                #return jsonify([c['file_name'] for c in comp['config_files']])



@app.route('/component_detail')
def update_configs():
    pass

    #xml_name = components[0][det_component]
    #if os.path.exists('avchanges/'+xml_name):
     #   return 'exists'
    #else:
     #   return "not exists"


#    print(components['config_files']['file_name'])


if __name__ == '__main__':
    app.run(debug=True)

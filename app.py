#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify, render_template, url_for
import json

app = Flask(__name__)

# load json file
with open('avchanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']
<<<<<<< HEAD
print(len(components))
=======
# print(type(components))
>>>>>>> e17f14c837aa69371359b1347630f74989f346d2


@app.route('/')
def home():
    return jsonify(components)
<<<<<<< HEAD
=======


@app.route('/index')
def index():
    return render_template('index.html')
>>>>>>> e17f14c837aa69371359b1347630f74989f346d2


@app.route('/components')
def list_components():
    component_list = []

    with open('avchanges/component_files.json') as f:
        data = json.load(f)

<<<<<<< HEAD
    comps = [(k, v) for k, v in data.items()]
=======
    for key, value in data.items():
        component_list.append((key, value))
>>>>>>> e17f14c837aa69371359b1347630f74989f346d2

    return render_template('components.html', components=component_list)


<<<<<<< HEAD
@app.route('/components/<det_component>')
def get_comp_attrs(det_component):
    return get_configfiles(det_component)


def get_configfiles(config_comp):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == config_comp:
                return jsonify([c['file_name'] for c in comp['config_files']])
=======
@app.route('/components/<detail_component>')
def get_comp_attrs(detail_component):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == detail_component:
                return render_template('comp_detail.html', component_files=[c['file_name'] for c in comp['config_files']])
                #return jsonify([c['file_name'] for c in comp['config_files']])


>>>>>>> e17f14c837aa69371359b1347630f74989f346d2

@app.route('/component_detail')
def update_configs():
    pass

if __name__ == '__main__':
    app.run(debug=True)

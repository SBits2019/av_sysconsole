#!/Users/pankaj/Projects/ActiveVideo/bin/python
from flask import Flask, jsonify, render_template, url_for
import json

app = Flask(__name__)

# load json file
with open('avchanges/json_AV-2.13.json') as f:
    data = json.load(f)

components = data['product']['components']


@app.route('/')
def home():
    return jsonify(components)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/components')
def list_components():
    comps = []

    with open('avchanges/component_files.json') as f:
        data = json.load(f)

    comps = [(k, v) for k, v in data.items()]

    return render_template('components.html', components=comps)


@app.route('/components/<detail_component>')
def get_comp_attrs(detail_component):
    return render_template('comp_detail.html', component_files=get_configfiles(detail_component))


def get_configfiles(config_comp):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == config_comp:
                return [c['file_name'] for c in comp['config_files']]


@app.route('/component_detail')
def update_configs():
    pass


if __name__ == '__main__':
    app.run(debug=True)

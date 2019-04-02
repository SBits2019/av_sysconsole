from flask import Flask, jsonify, render_template, redirect, url_for
import json

app = Flask(__name__)


# load json file
with open('avchanges/json_AV-2.13.json') as f:
    data = json.load(f)

# separate individual components from the json
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

    changed_comps = get_allconfigfiles()

    return render_template('components.html', components=comps, changed_components=changed_comps)


@app.route('/components/<detail_component>/<detail_file>')
def get_file_attrs(detail_component, detail_file):
    for c in components:
        for key, value in c.items():
            if key == 'name' and value == detail_component:
                files = c['config_files']
                for i in files:
                    if i['file_name'] == detail_file:
                        return jsonify(i['attribute_modifications'])


def get_configfiles(config_comp):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == config_comp:
                return [c['file_name'] for c in comp['config_files']]


def get_allconfigfiles():
    for comp in components:
        return [c['file_name'] for c in comp['config_files']]


@app.route('/component_detail')
def update_configs():
    pass


if __name__ == '__main__':
    app.run(debug=True)

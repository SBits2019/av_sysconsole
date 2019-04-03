from flask import Flask, jsonify, render_template
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
    with open('avchanges/component_files.json') as f:
        data = json.load(f)
    # get the configs in each component that have changes
    changed_comps = [(k, v) for k, v in data.items()]
    # get all the configs
    all_files = get_allconfigfiles()
    # print(all_files)

    return render_template('components.html', changed_components=changed_comps, components=all_files)


@app.route('/components/<detail_component>/<detail_file>')
def get_file_attrs(detail_component, detail_file):

    with open('avchanges/component_files.json') as f:
        data = json.load(f)
    comps = [(k, v) for k, v in data.items()]
    changed_comps = get_allconfigfiles()

    for c in components:
        for key, value in c.items():
            if key == 'name' and value == detail_component:
                files = c['config_files']
                for i in files:
                    if i['file_name'] == detail_file:
                        return render_template('comp_detail.html',
                                               attribute_modifications=i['attribute_modifications'],
                                               file_name=i['file_name'], components=comps,
                                               changed_components=changed_comps)


def get_configfiles(config_comp):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == config_comp:
                return [c['file_name'] for c in comp['config_files']]


def get_allconfigfiles():
    x = []
    for comp in components:
        if 'config_files' in comp:
            for c in comp['config_files']:
                x.append(c['file_name'])
    return x


@app.route('/component_detail')
def update_configs():
    pass


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, render_template
import json
from helper_tools import helper_tools

app = Flask(__name__)


# load json file
with open('avchanges/2.13_final.json') as f:
    data = json.load(f)

# separate individual components from the json
components = data['product']['components']


@app.route('/')
def index():
    return render_template('index.html', changes=helper_tools.get_summary())


@app.route('/components')
def list_components():
    return render_template('components.html', changed_components=helper_tools.get_comp_dict(),version=helper_tools.get_version_details())


@app.route('/components/<detail_component>/<detail_file>')
def get_file_attrs(detail_component, detail_file):

    return render_template('comp_detail.html',
                           attribute_modifications=helper_tools.get_attribute_modifications(detail_component, detail_file), file_name=detail_file, changed_components=helper_tools.get_comp_dict(), version=helper_tools.get_version_details())


@app.route('/component_detail')
def update_configs():
    pass


if __name__ == '__main__':
    app.run(debug=True)

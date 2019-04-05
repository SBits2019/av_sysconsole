import json


# load json file
with open('avchanges/2.13_final.json') as f:
    json_data = json.load(f)

with open('avchanges/component_files.json') as f:
    comp_all_files = json.load(f)

components = json_data['product']['components']


def get_comp_dict():
    comp_dict = {}
    for c in components:
        comp_dict[c['name']] = [(x, True) for x in get_configfiles(c['name'])]

    all_files = get_allconfigfiles()

    comp_dict_new = {}

    for key in comp_dict.keys():
        for f in all_files:
            if f[0] == key:
                for elem in f[1]:
                    if elem not in [x[0] for x in comp_dict[key]]:                    
                        comp_dict[key].append((elem, False))
            elif f[0] not in comp_dict.keys():
                comp_dict_new[f[0]] = [(i, False) for i in f[1]]

    comp_dict_final = {**comp_dict, **comp_dict_new}
    return comp_dict_final


def get_configfiles(config_comp):
    for comp in components:
        for key, value in comp.items():
            if key == 'name' and value == config_comp:
                return [c['file_name'] for c in comp['config_files']]


def get_allconfigfiles():
    x = []
    for k, v in comp_all_files.items():
        x.append((k, v))
    return x


def get_attribute_modifications(comp_name, comp_file_name):
    for c in components:
        for key, value in c.items():
            if key == 'name' and value == comp_name:
                files = c['config_files']
                for i in files:
                    if i['file_name'] == comp_file_name:
                        return i['attribute_modifications']


def get_summary():
     return json_data['product']['summary_of_changes'].split('-')

def get_version_details():
    base = json_data['product']['base_config_version']
    new = json_data['product']['new_config_version']
    return (base, new)

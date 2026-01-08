from flask import (Blueprint, send_from_directory, current_app, url_for, jsonify)
import os, json

data_bp = Blueprint('data', __name__)

# Route .txt
# ======================
@data_bp.route('/robots')
def robots():
    return send_from_directory('static', 'robots.txt')

# Route .json
# ======================

# Sampling
def load_data():
    json_path = os.path.join(current_app.static_folder, 'data_sample.json')

    with open(json_path, encoding='utf-8') as file:
        data = json.load(file)

    return data

@data_bp.route('/sampling')
def sampling_data():
    sampling = load_data()

    return jsonify(sampling)

# Data Sections
@data_bp.route('/data')
def project_data():
    data = load_data()

    # Ambil list project dari key 'project'
    projects_list = data.get("project", [])

    # checking protected path
    for i, p in enumerate(projects_list):
        # real path json
        print(f"\n{i} url real data image \t\t: {p['img']}")

        # replace with protected image path
        p['img'] = url_for('file.protected_image', filename=p['img'])   
        print(f"{i} url replace protected image \t: {p['img']}")

    return jsonify(projects_list)

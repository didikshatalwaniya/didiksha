from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

@app.route('/tenant', methods=['POST'])
def create_tenant():
    # Get tenant data from request
    tenant_data = request.get_json()
    # Save tenant data to MongoDB
    tenant_id = mongo.db.tenant.insert_one(tenant_data).inserted_id
    return jsonify({'tenant_id': str(tenant_id)}), 201

@app.route('/project_metadata', methods=['POST'])
def create_project_metadata():
    # Get project metadata from request
    metadata = request.get_json()
    # Save project metadata to MongoDB
    metadata_id = mongo.db.project_metadata.insert_one(metadata).inserted_id
    return jsonify({'metadata_id': str(metadata_id)}), 201

if __name__ == '__main__':
    app.run()

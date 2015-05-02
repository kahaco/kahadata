import os
from flask import Flask, Response, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

import models
import schemas

def _get_data(district, resource_types=''):
    resource_for = request.args.get('for', None)
    query_filter = models.KahaResource.query
    if (district != 'all'):
        query_filter = query_filter.filter_by(district=district)
    if (resource_for):
        query_filter = query_filter.filter_by(resource_for=resource_for)
    if resource_types:
        query_filter = query_filter.join(models.KahaResource.types).filter(models.KahaResourceType.resource_type.in_(resource_types.split(',')))
   
    datalist = query_filter.all()
    serializer = schemas.KahaResourceSchema(many=True)
    result = serializer.dump(datalist)
    return jsonify({'resources':result.data})

@app.route("/")
def hello():
    return "Visit kaha.co"

@app.route("/resources/<district>")
def get_resources(district):
    return _get_data(district)
 
@app.route("/resources/<district>/<resource_types>")
def get_resource_of_types(district, resource_types):
    return _get_data(district, resource_types)

@app.route("/resource/<uuid>")
def get_resource(uuid):
    data = models.KahaResource.query.filter_by(uuid=uuid).first()
    if data:
        serializer = schemas.KahaResourceSchema()
        result = serializer.dump(data)
        return jsonify((result.data))#; //{'data':result.data})
if __name__ == "__main__":
    print "Running app"
    app.run(host='0.0.0.0')

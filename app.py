import os
from flask import Flask,jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

import models
import schemas

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data/<district>")
def get_data(district):
    datalist = models.KahaResource.query.filter_by(district=district).all()

    serializer = schemas.KahaResourceSchema(many=True)
    result = serializer.dump(datalist)
    return jsonify({'data':result.data})
    
if __name__ == "__main__":
    print "Running app"
    app.run()

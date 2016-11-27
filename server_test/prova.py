from flask import Flask, jsonify, abort, request
from model import db, Record
from schema import ma, record_schema, records_schema

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///record_collection"
db.init_app(app)
ma.init_app(app)


@app.route("/")
def get_records():
    records = Record.query.all()
    return records_schema.jsonify(records)

@app.route("/<int:index>", methods=['GET', 'POST'])
def get_record(index):
    if request.method == 'POST':
        abort(405)
    record = Record.query.filter(Record.index == index).first_or_404()
    return record_schema.jsonify(record)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(
        error="Not Found",
        status_code=404
    )

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(
        error="Method Not Allowed",
        status_code=405
    )

if __name__ == '__main__':
  app.run()

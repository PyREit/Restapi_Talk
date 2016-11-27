from flask_marshmallow import Marshmallow
from model import Record

ma = Marshmallow()


class RecordSchema(ma.ModelSchema):
    class Meta:
        model = Record

record_schema = RecordSchema()
records_schema = RecordSchema(many=True)

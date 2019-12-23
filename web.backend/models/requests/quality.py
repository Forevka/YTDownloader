from marshmallow import Schema, fields

class RequestQuality(Schema):
    links = fields.List(fields.Url())


request_quality_schema = RequestQuality()

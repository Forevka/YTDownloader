from marshmallow import Schema, fields


class RequestQuality(Schema):
    link = fields.Url()
    quality = fields.Int()

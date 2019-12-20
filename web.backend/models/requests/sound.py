from marshmallow import Schema, fields

class RequestLink(Schema):
    link = fields.Url()


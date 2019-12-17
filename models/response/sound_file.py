from marshmallow import Schema, fields

class ResponseFile(Schema):
    file_base64 = fields.String()


response_schema_file = ResponseFile()
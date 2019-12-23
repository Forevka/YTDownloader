from marshmallow import Schema, fields


class AvailableQuality(Schema):
    id = fields.Int()
    mime_type = fields.Str()
    resolution = fields.Str()
    fps = fields.Str()


class VideoQuality(Schema):
    link = fields.Url()
    available_quality = fields.List(fields.Nested(AvailableQuality))


class ResponseQuality(Schema):
    links = fields.List(fields.Nested(VideoQuality))


response_quality_schema = ResponseQuality()

from marshmallow import Schema, fields
from utils.base_model import BaseModel

class RequestQuality(BaseModel):
    links = fields.List(fields.Url())


request_quality_schema = RequestQuality()

from pydantic import BaseModel, AnyUrl
import typing

class RequestQuality(BaseModel):
    links: typing.List[AnyUrl]

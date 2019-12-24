from pydantic import BaseModel, AnyUrl
import typing

class AvailableQuality(BaseModel):
    id: int
    mime_type: str
    resolution: typing.Optional[str]
    fps: str


class VideoQuality(BaseModel):
    link: AnyUrl
    available_quality: typing.List[AvailableQuality]


class ResponseQuality(BaseModel):
    links: typing.List[VideoQuality]

from pydantic import BaseModel, AnyUrl

class RequestLink(BaseModel):
    link: AnyUrl

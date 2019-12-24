from pydantic import BaseModel, AnyUrl
import typing

class ResponseFile(BaseModel):
    file_base64: str

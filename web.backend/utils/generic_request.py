from typing import TypeVar, Generic
from aiohttp import web

T = TypeVar('T')

class GRequest(web.Request, Generic[T]):
    def get_model(self,) -> T:
        return self.get('object_model')

    @staticmethod
    def from_request(req: web.Request):
        r = GRequest(req.message, req.protocol, task = req.task, loop = req.loop, protocol = req.protocol, payload_writer = None)
        r.__dict__ = req.__dict__
        return r

@web.middleware
async def generic_request_middleware(request, handler):
    request = GRequest.from_request(request)
    return await handler(request)
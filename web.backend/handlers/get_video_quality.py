import pytube
from loguru import logger
from aiohttp import web
import config
from aiohttp_apispec import (
    docs, request_schema, response_schema
)

from models.requests.quality import RequestQuality
from models.response.quality import ResponseQuality



@docs(
    tags=["quality"],
    summary="get quality",
    description="return list of available quality for provided video",
)
@request_schema(RequestQuality)
@response_schema(ResponseQuality, 200)
async def get_quality(request: web.Request):
    if request.body_exists:
        yt_links = await request.json()
        logger.info(yt_links)
        links = []
        for link in yt_links['links']:
            video = pytube.YouTube(link)
            links.append({"link": link, 
                            "available_quality": [
                                {
                                    "id": i.itag, 
                                    "mime_type": i.mime_type, 
                                    "resolution": i.res, 
                                    "fps": i.fps
                                } for i in video.streams.all()
                            ]
                        })
        return web.json_response(data=links)
    return web.Response(status=406)

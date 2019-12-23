from pytube import YouTube
from loguru import logger
from aiohttp import web
import config
from aiohttp_apispec import (
    docs, request_schema, setup_aiohttp_apispec, validation_middleware,
    response_schema)
from models.requests.quality import RequestQuality, request_quality_schema
from models.response.quality import ResponseQuality

@docs(
    tags=["quality"],
    summary="get quality",
    description="return list of available quality for provided video",
)
@request_schema(RequestQuality())
@response_schema(ResponseQuality, 200)
async def get_quality(request: web.Request):
    if request.body_exists:
        yt_links = request_quality_schema.load(await request.json())
        links = []
        for link in yt_links['links']:
            y = YouTube(link)
            links.append({"link": link, "available_quality": [{"id": i.itag, "mime_type": i.mime_type, "resolution": i.res, "fps": i.fps} for i in y.streams.all()]})
        logger.info(links)
        return web.json_response(data=links)
    return web.Response(status=406)



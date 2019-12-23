from pytube import YouTube
from loguru import logger
from aiohttp import web
import config
from aiohttp_apispec import (
    docs, querystring_schema, setup_aiohttp_apispec, validation_middleware)
from models.requests.quality import RequestQuality


@docs(
    tags=["link"],
    summary="get link",
    description="convert and download sound by YouTube video link",
)
@querystring_schema(RequestQuality)
async def get_quality(request: web.Request):
    link_pull = request.json.loads()
    logger.info(request)
    if link_pull["data"]:
        quality = []
        for i in link_pull["data"]:
            y = YouTube(i)
            quality.append([i, y.streams.all()])
        web.json_response(data=quality)
    return web.Response(status=406)



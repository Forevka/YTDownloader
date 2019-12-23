from contextvars import ContextVar
import os

from aiohttp import web
from aiohttp import web
from aiohttp_apispec import (
    docs, querystring_schema, setup_aiohttp_apispec, validation_middleware)
from loguru import logger
import youtube_dl
import routes

from models.requests.sound import RequestLink

file_name = ContextVar('filename')


def downloaded_hook(d):
    if d['status'] == 'finished':
        logger.info('downloaded')
        file_name.set(d['filename'])


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
    'progress_hooks': [downloaded_hook],
}


@docs(
    tags=["link"],
    summary="get link",
    description="convert and download sound by YouTube video link",
)
@querystring_schema(RequestLink)
async def get_sound_by_yt_link(request: web.Request):
    link_obj: RequestLink = request["querystring"]
    if link_obj:
        logger.info('link found!')
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        logger.info('downloading file')
        ydl.download([link_obj['link']])
        logger.info('converted')

        pre, ext = os.path.splitext(file_name.get())

        return web.FileResponse(path=pre + '.mp3')
    return web.Response(status=406)



if __name__ == '__main__':
    app = web.Application()
    routes.create(app)
    app.middlewares.append(validation_middleware)
    setup_aiohttp_apispec(
        app=app,
        title="My Documentation",
        version="v1",
        url="/api/docs/swagger.json",
        swagger_path="/api/docs",
    )

    web.run_app(app, port=9999)

from aiohttp import web
from aiohttp_apispec import (
    docs,
    querystring_schema,
    setup_aiohttp_apispec,
    validation_middleware,
)
from aiohttp import web
import youtube_dl
from contextvars import ContextVar
import os

from models.requests.sound import RequestLink
from loguru import logger

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
    return web.Response(status=415)



app = web.Application()

app.add_routes([web.get('/sound', get_sound_by_yt_link)])

app.middlewares.append(validation_middleware)


if __name__ == '__main__':
    setup_aiohttp_apispec(
        app=app, 
        title="My Documentation", 
        version="v1",
        url="/api/docs/swagger.json",
        swagger_path="/api/docs",
    )

    web.run_app(app, port=9999)
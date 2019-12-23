import config
from models.requests.quality import RequestQuality
from loguru import logger
from aiohttp import web
from pytube import YouTube
from aiohttp_apispec import (
    docs, querystring_schema, setup_aiohttp_apispec, validation_middleware)
from contextvars import ContextVar

file_name = ContextVar('filename')


def downloaded_hook(d):
    if d['status'] == 'finished':
        logger.info('downloaded')
        file_name.set(d['filename'])


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': '{}',
        'preferredquality': '{}',
    }],
    'progress_hooks': [downloaded_hook],
}

@docs(
    tags=["link"],
    summary="get link",
    description="convert and download sound by YouTube video link",
)
@querystring_schema(RequestQuality)
async def get_sound_by_yt_link(request: web.Request):
    data = request.json.loads()
    logger.info(request)
    link_pull =  []
    for i in data:

        link: RequestQuality = i
        link_pull.append(link)
    logger.info(request)
    if link_pull:
        for i in link_pull:
            logger.info('link found!')
            ydl = YouTube(i)
            ydl.streams.filter(subtype=i['quality']).download(i['link'])

            #я хуй зна чі воно буде робить но скарей всього нет

            pre, ext = os.path.splitext(file_name.get())
            path_to_file = pre + '.mp3'
            path_to_file.replace(" ", "%20")
            logger.info(path_to_file)
            url ="http://{}:{}/download?link={}".format(config.host, config.port, path_to_file)
        return web.Response(json={"download_link": url})
    return web.Response(status=406)
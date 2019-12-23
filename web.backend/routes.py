from aiohttp import web
from handlers.get_sound_by_yt_link import get_sound_by_yt_link
from handlers.get_video_quality import get_quality

def create(app):
    app.add_routes([web.post('/sound', get_sound_by_yt_link),
                    web.post('/quality', get_quality)])

    

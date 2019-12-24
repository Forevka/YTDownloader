import typing

import pytube
from loguru import logger

from app import app
from models.requests.quality import RequestQuality
from models.response.quality import ResponseQuality, VideoQuality, AvailableQuality
from config import API_URL


@app.post(f'{API_URL}/quality', response_model=ResponseQuality)
async def get_quality(request: RequestQuality):
    logger.info(request.links)
    resp = ResponseQuality(links=[])
    for link in request.links:
        video = pytube.YouTube(str(link))
        resp.links.append(
            VideoQuality(link=link, 
                            available_quality=[
                                AvailableQuality(
                                    id=i.itag, 
                                    mime_type=i.mime_type, 
                                    resolution=i.res, 
                                    audio_quality=i.audioQuality,
                                    fps=i.fps) for i in video.streams.all()
                                ]
                            )
                        )
    
    return resp



from utils.video_downloader_abc import Downloader
from services.yt_downloader import YouTubeDownloader

async def DownloaderFabric(link_to: str) -> Downloader:
    if link_to is None and not link_to.any():
        raise RuntimeError("link can`t be empty or null")
    
    if 'youtube.com' in link_to.lower() or 'youtu.be' in link_to.lower():
        d = YouTubeDownloader(link_to)
        await d.prefetch_init()
        
        return d
        
    return Downloader()
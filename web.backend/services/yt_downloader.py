from async_pytube import YouTube
from utils.video_downloader_abc import Downloader

class YouTubeDownloader(YouTube, Downloader):
    def find_by_id(id: int):
        return self.streams.get_by_itag(str(id))

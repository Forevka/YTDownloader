from async_pytube import YouTube, Stream
from utils.video_downloader_abc import Downloader, StreamResult

import typing

class YouTubeResultStream(Stream, StreamResult):
    async def download(self, output_path: str = None, filename: str = None, filename_prefix: str = None) -> None:
        await self.download(output_path, filename, filename_prefix)
    
    def filename(self,) -> str:
        return self.title
    
    @staticmethod
    def from_obj(obj: Stream) -> 'YouTubeResultStream':
        r = YouTubeResultStream()
        r.__dict__ = obj.__dict__
        return r

class YouTubeDownloader(YouTube, Downloader):
    def find_by_id(self, id: int) -> YouTubeResultStream:
        return YouTubeResultStream.from_obj(self.streams.get_by_itag(str(id)))

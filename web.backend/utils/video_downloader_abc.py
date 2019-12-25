from abc import ABCMeta, abstractmethod
import io
import typing

class StreamResult(metaclass = ABCMeta):
    def __bool__(self,) -> bool:
        return False

    @abstractmethod
    async def download_file(self, output_path: str = None, filename: str = None, filename_prefix: str = None):
        pass
    
    @abstractmethod
    async def to_buffer(self,) -> io.BytesIO:
        pass
        
    @property
    @abstractmethod
    def filename(self,) -> str:
        pass
        
        
    @classmethod
    @abstractmethod
    def _from_obj(obj: typing.Any):
        pass

class Downloader(metaclass = ABCMeta):
    def __bool__(self,) -> bool:
        return False

    @abstractmethod
    def find_by_id(self, id: int,) -> StreamResult:
        pass


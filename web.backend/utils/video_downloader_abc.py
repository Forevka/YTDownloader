from abc import ABCMeta, abstractmethod
import typing

class Downloader(metaclass = ABCMeta):
    def __bool__(self,) -> bool:
        return False

    @abstractmethod
    def find_by_id(self, id: int,):
        pass

class StreamResult(metaclass = ABCMeta):
    def __bool__(self,) -> bool:
        return False

    @abstractmethod
    async def download(self, output_path: str = None, filename: str = None, filename_prefix: str = None):
        pass
    
    @abstractmethod
    def filename(self,) -> str:
        pass
        
        
    @classmethod
    @staticmethod
    def from_obj(obj: typing.Any):
        pass
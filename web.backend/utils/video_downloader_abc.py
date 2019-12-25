from abc import ABCMeta, abstractmethod

class Downloader(metaclass = ABCMeta):
    def __bool__(self,) -> bool:
        return False

    @abstractmethod
    def find_by_id(id: int):
        pass




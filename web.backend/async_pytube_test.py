import asyncio

import urllib.parse
import json
import pprint

from loguru import logger
import async_pytube
import async_pytube.mixins as _mixins
from utils.downloader_fabric import DownloaderFabric

async def main():
    y = await DownloaderFabric("https://www.youtube.com/watch?v=GIXFsy924BI")
    print(y.streams.all())
    await y.streams.first().download()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
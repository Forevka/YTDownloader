import asyncio

import urllib.parse
import json
import pprint

from loguru import logger
from utils.patch import patch; patch()

import async_pytube
import async_pytube.mixins as _mixins

async def main():
    y = async_pytube.YouTube("https://www.youtube.com/watch?v=WPo3MkMyWBc")
    await y.prefetch_init()
    print(y.streams.all())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
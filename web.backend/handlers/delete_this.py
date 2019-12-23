from pytube import YouTube
from loguru import logger


if __name__ == "__main__":
    y = YouTube("https://www.youtube.com/watch?v=0wO8JUrU5C0&list=PLF7xV3VKKgBX-341o2zfZ4qwk8MTImxib&index=2&t=0s")
    logger.info(y.streams.all())

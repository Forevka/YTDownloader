# -*- coding: utf-8 -*-
# flake8: noqa
# noreorder
"""
Pytube: a very serious Python library for downloading YouTube Videos.
"""
__title__ = 'async_pytube'
__version__ = '9.5.3'
__author__ = 'Nick Ficano'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2019 Nick Ficano'

from async_pytube.logging import create_logger
from async_pytube.query import CaptionQuery
from async_pytube.query import StreamQuery
from async_pytube.streams import Stream
from async_pytube.captions import Caption
from async_pytube.contrib.playlist import Playlist
from async_pytube.__main__ import YouTube

logger = create_logger()
logger.info('%s v%s', __title__, __version__)

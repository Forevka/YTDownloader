# -*- coding: utf-8 -*-
"""Implements a simple wrapper around urlopen."""
import urllib.request
import aiohttp


from async_pytube.compat import urlopen
# 403 forbidden fix


async def get(
    url=None, headers=False,
    streaming=False, chunk_size=8 * 1024,
):
    """Send an http GET request.

    :param str url:
        The URL to perform the GET request for.
    :param bool headers:
        Only return the http headers.
    :param bool streaming:
        Returns the response body in chunks via a generator.
    :param int chunk_size:
        The size in bytes of each chunk.
    """

    # https://github.com/nficano/pytube/pull/465
    #req = #urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = {}
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #response = await resp.text()#urlopen(req)
            if streaming:
                return await async_response_read(resp, chunk_size)
            elif headers:
                # https://github.com/nficano/pytube/issues/160
                return {k.lower(): v for k, v in await resp.json().items()}
            return (
                await resp.text()#.decode('utf-8')
            )


def stream_response(response, chunk_size=8 * 1024):
    """Read the response in chunks."""
    while True:
        buf = response.read(chunk_size)
        if not buf:
            break
        yield buf
        
async def async_response_read(response, chunk_size=8 * 1024):
    while True:
        chunk = await resp.content.read(chunk_size)
        if not chunk:
            break
        yield chunk

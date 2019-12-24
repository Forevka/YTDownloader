import pytube.mixins as _mixins
import urllib.parse
import json
import pprint

from pytube.compat import parse_qsl
from pytube.compat import unquote
from loguru import logger

def patch():
    def new_apply_descrambler(stream_data, key):
        """Apply various in-place transforms to YouTube's media stream data.

        Creates a ``list`` of dictionaries by string splitting on commas, then
        taking each list item, parsing it as a query string, converting it to a
        ``dict`` and unquoting the value.

        :param dict dct:
            Dictionary containing query string encoded values.
        :param str key:
            Name of the key in dictionary.

        **Example**:

        >>> d = {'foo': 'bar=1&var=test,em=5&t=url%20encoded'}
        >>> apply_descrambler(d, 'foo')
        >>> print(d)
        {'foo': [{'bar': '1', 'var': 'test'}, {'em': '5', 't': 'url encoded'}]}

        """
        

        if key == 'url_encoded_fmt_stream_map' and not stream_data.get('url_encoded_fmt_stream_map'):
            formats = json.loads(stream_data['player_response'])['streamingData']['formats']
            formats.extend(json.loads(stream_data['player_response'])['streamingData']['adaptiveFormats'])
            try:
                stream_data[key] = [{u'url': format_item[u'url'],
                                    u'type': format_item[u'mimeType'],
                                    u'quality': format_item[u'quality'],
                                    u'itag': format_item[u'itag']} for format_item in formats]
            except:
                stream_data[key] = [{u'url': urllib.parse.unquote([url_item for url_item in format_item[u'cipher'].split("&") if "url=" in url_item][0].split("=")[1]),
                                    u'sp': urllib.parse.unquote([url_item for url_item in format_item[u'cipher'].split("&") if "sp=" in url_item][0].split("=")[1]),
                                    u's': urllib.parse.unquote([url_item for url_item in format_item[u'cipher'].split("&") if "s=" in url_item][0].split("=")[1]),
                                    u'type': format_item[u'mimeType'],
                                    u'quality': format_item[u'quality'],
                                    u'itag': format_item[u'itag']} for format_item in formats]
        else:
            stream_data[key] = [
                {k: unquote(v) for k, v in parse_qsl(i)}
                for i in stream_data[key].split(',')
            ]
        logger.debug(
            'applying descrambler\n%s',
            pprint.pformat(stream_data[key], indent=2),
        )

    #Patch
    _mixins.apply_descrambler = new_apply_descrambler
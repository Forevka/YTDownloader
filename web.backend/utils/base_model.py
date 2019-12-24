from marshmallow import Schema
from loguru import logger
from aiohttp.web import middleware
from addict import Dict as MDict


class BaseModel(Schema):
    list_of_models = {}

    def __new__(cls, *args, **kwargs):
        if cls.__name__ not in BaseModel.list_of_models:
            BaseModel.list_of_models[cls.__name__] = cls
            logger.info(f'adding new sublass {cls.__name__}')
        instance = super(BaseModel, cls).__new__(cls, *args, **kwargs)
        return instance
        


@middleware
async def serialize_middleware(request, handler):
    #request_model_name = dict(request.config_dict)['swagger_dict']['paths'][request.path][request.method.lower()]['parameters'][0]['schema']['$ref'].split('/')[-1]
    if request.get('data'):
        request['object_model'] = MDict(request['data'])
    else:
        request['object_model'] = None
    return await handler(request)
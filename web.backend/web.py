from aiohttp import web
from aiohttp_apispec import (setup_aiohttp_apispec, validation_middleware)
from loguru import logger
from utils.patch import patch; patch()
from utils.base_model import serialize_middleware
from utils.generic_request import generic_request_middleware
import routes
from services.dbservice import DBService
import config

async def start(app: web.Application) -> None:
    app['db']: DBService = DBService(**config.dboptions)
    await app['db'].connect(migrate=True)
    DBService.set_current(app['db'])


if __name__ == '__main__':
    app = web.Application()
    
    app.on_startup.append(start)
    
    routes.register(app)

    app.middlewares.append(validation_middleware)
    app.middlewares.append(serialize_middleware)
    app.middlewares.append(generic_request_middleware)

    setup_aiohttp_apispec(
        app=app,
        title="My Documentation",
        version="v1",
        url="/api/docs/swagger.json",
        swagger_path="/api/docs",
    )
    
    web.run_app(app, port=9999)
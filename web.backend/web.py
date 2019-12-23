from aiohttp import web
from aiohttp_apispec import (setup_aiohttp_apispec, validation_middleware)
from loguru import logger
from utils.patch import patch; patch()
import routes

if __name__ == '__main__':
    app = web.Application()

    routes.register(app)

    app.middlewares.append(validation_middleware)

    setup_aiohttp_apispec(
        app=app,
        title="My Documentation",
        version="v1",
        url="/api/docs/swagger.json",
        swagger_path="/api/docs",
    )

    web.run_app(app, port=9999)

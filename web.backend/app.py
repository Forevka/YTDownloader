from utils.context_mixin import ContextInstanceMixin, DataMixin
from fastapi import FastAPI
from loguru import logger
from services.dbservice import DBService
import config
import time
from starlette.requests import Request

class DataFastAPI(FastAPI, DataMixin, ContextInstanceMixin):
    pass

app = DataFastAPI()

@app.on_event("startup")
async def start() -> None:
    logger.info('on start')

    DataFastAPI.set_current(app)

    app['db']: DBService = DBService(**config.dboptions)
    DBService.set_current(app['db'])

    await app['db'].connect(migrate=True)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
from utils.context_mixin import ContextInstanceMixin, DataMixin
from fastapi import FastAPI
from loguru import logger
from services.dbservice import DBService
import config


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
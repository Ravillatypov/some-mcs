from logging import getLogger

from fastapi import FastAPI
from tortoise import Tortoise
from uvicorn import run

from settings import setting
from web.router import router

logger = getLogger('cli')


async def on_startup(*args, **kwargs):
    app.include_router(router)
    await Tortoise.init(
        db_url=setting.db_url,
        modules={'models': ['repositories.pg_models']},
    )
    await Tortoise.generate_schemas()
    logger.info('app is started')


async def on_shutdown(*args, **kwargs):
    await Tortoise.close_connections()
    logger.info('app stopped')


app = FastAPI(
    debug=setting.debug,
    title='Some mcs',
    description='Some microservice',
    version=setting.version,
    on_startup=[on_startup],
    on_shutdown=[on_shutdown],
)

if __name__ == '__main__':
    app.debug = True
    run(app)

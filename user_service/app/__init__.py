from sanic import Sanic
from settings import Settings
from gino.ext.sanic import Gino
import aiohttp
from sanic_openapi import swagger_blueprint

app = Sanic(__name__)
app.config.from_object(Settings())
app.blueprint(swagger_blueprint)

@app.listener('before_server_start')
async def init(app=None, loop=None):
    app.aiohttp_session = aiohttp.ClientSession(loop=loop)   

@app.listener('after_server_stop')
async def finish(app=None, loop=None):
    loop.run_until_complete(app.aiohttp_session.close())
    loop.close()
    
db = Gino()
db.init_app(app)

from app import routes
from .handlers import convert_to_json
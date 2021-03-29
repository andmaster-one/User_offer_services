from app import app
from sanic.exceptions import InvalidUsage, Unauthorized, NotFound
from sanic.response import json

@app.exception(InvalidUsage, Unauthorized, NotFound)
async def convert_to_json(request, exception):    
    return json(exception.args[0], exception.status_code)
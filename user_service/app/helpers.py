from cerberus import Validator
from sanic.exceptions import abort, InvalidUsage
from aiohttp.client_exceptions import ClientConnectorError
from app import app
from settings import ERROR_MESSAGES, OFFER_API_URLS

json_schema_register = {
    'username': {'type': 'string', "minlength": 2, "maxlength": 255,'required': True}, 
    'password':{'type': 'string', "minlength": 6, "maxlength": 255, 'required': True},
      "email": {
      "type": "string",
      "minlength": 2,
      "maxlength": 255,
      "required": True,
      "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    }
}

json_schema_auth = {
    'username': {'type': 'string', "maxlength": 255,'required': True}, 
    'password':{'type': 'string', "maxlength": 255, 'required': True}
}

validator_register = Validator(json_schema_register)
validator_auth = Validator(json_schema_auth)

async def validate_json(request, register=None):      
    try:
        data = request.json
    except InvalidUsage:
        abort(400, {'Error': ERROR_MESSAGES['ERROR_JSON']})
    validator = validator_register if register else validator_auth        
    if not data or not validator.validate(data):
        abort(400, {'Error': validator.errors or "Empty fields"} )   
    return data

async def get_offers(user_id):
    url = OFFER_API_URLS['offer']
    try:
        async with app.aiohttp_session.post(url, json={'user_id': user_id}) as response:
            offers = await response.json()
    except ClientConnectorError as e:
        abort(400, {'Error': 'Communication with service failed'})    
    return offers
    
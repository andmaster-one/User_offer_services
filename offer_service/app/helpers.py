from cerberus import Validator
from sanic.exceptions import abort, InvalidUsage
from aiohttp.client_exceptions import ClientConnectorError
from settings import ERROR_MESSAGES, USER_API_URLS
from app import app

json_schema_create_offer = {
    'user_id': {'type': 'integer', 'min': 1, 'required': True}, 
    'title': {'type': 'string', 'maxlength': 128, 'required': True},
    'text': {'type': 'string', 'maxlength': 450, 'required': True},    
}

json_schema_get_offers = {
    'user_id': {'type': 'integer', 'min': 1, 'required': False}, 
    'offer_id': {'type': 'integer', 'min': 1, 'required': False},
}

validator_create_offer = Validator(json_schema_create_offer)
validator_get_offers = Validator(json_schema_get_offers)

async def validate_json(request, create=None):      
    try:
        data = request.json
    except InvalidUsage:
        abort(400, {'Error': ERROR_MESSAGES['ERROR_JSON']})
    validator = validator_create_offer if create else validator_get_offers        
    if not data or not validator.validate(data) or len(data) in (0,2,):
        abort(400, {'Error': validator.errors or "Incorrect fields"})   
    return data

async def is_user_exists(user_id):
    url = USER_API_URLS['user']+ "/" +str(user_id)
    try:
        async with app.aiohttp_session.get(url) as response:
            user = await response.json()
            user_id = user.get('user_id', None)
    except ClientConnectorError as e:
        abort(400, {'Error': 'Communication with service failed'})
    if user_id is None:
        abort(400, {'Error': 'User_id is not valid'})
    return user_id





    

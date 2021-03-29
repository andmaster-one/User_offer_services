from sanic.response import json
from sanic.exceptions import abort
from app import app
from .models import User
from .helpers import validate_json, get_offers
from sanic_openapi import doc


@app.get("/user/<user_id:int>") 
@doc.summary("Get user")
@doc.produces(User)
async def get_user(request, user_id): 
    is_offer_request = request.headers.get('is_offer_service', None)
    if is_offer_request is not None:        
        id = await User.select('id').where(User.id == user_id).gino.scalar()
        return json({'user_id':id})  

    user = await User.get_or_404(user_id)
    offers = await get_offers(user_id)
    user_dict = user.to_dict()
    user_dict.pop('password_hash')
    user_dict.update(offers)
    return json(user_dict)


@app.post("/user/register") 
@doc.summary("Register user")
@doc.produces(User)
async def register_user(request):
    validated_data = await validate_json(request, register=True)
    user = await User.create_user(validated_data)
    user_dict = user.to_dict()
    user_dict.pop('password_hash')
    return json(user_dict, 201)


@app.post("/user/auth") 
@doc.summary("Auth user")
@doc.produces(User)
async def auth_user(request):
    validated_data = await validate_json(request)
    user = await User.auth_user(validated_data)    
    if user is not None:
        token = user.get_password_token() 
        return json({'user_id':user.id, 'token':token}, 200)        
    abort(401, {'Error': 'Incorrect username or password'})
    

from sanic.response import json
from sanic.exceptions import abort
from sanic_openapi import doc
from app import app
from .helpers import validate_json, is_user_exists
from .models import Offer

@app.post("/offer") 
@doc.summary("Get offer")
@doc.produces(Offer)
async def get_offer(request):  
    validated_data = await validate_json(request) 
    user_id = validated_data.get('user_id', None)
    if user_id and await is_user_exists(user_id):
        offers = await Offer.query.where(Offer.user_id == user_id).gino.all()
        offers_dict_list = [offer.to_dict() for offer in offers]
        dict_for_return = {'Offers': offers_dict_list}        
    else:
        offer = await Offer.get_or_404(validated_data['offer_id'])
        dict_for_return = {'Offer': offer.to_dict()}
    return json(dict_for_return)

@app.post("/offer/create")
@doc.summary("Create offer")
@doc.produces(Offer)
async def create_offer(request):
    validated_data = await validate_json(request, create=True)
    user_id = await is_user_exists(validated_data['user_id'])
    offer = await Offer.create(user_id = user_id, text = validated_data['text'], title = validated_data['title'])
    return json(offer.to_dict(), 201)


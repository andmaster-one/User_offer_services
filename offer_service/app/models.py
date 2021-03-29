from app import app
from app import db
#import jwt
from time import time
from sanic.exceptions import abort
from asyncpg.exceptions import UniqueViolationError
#from werkzeug.security import generate_password_hash, check_password_hash


class Offer(db.Model):
   __tablename__ = 'offers'

   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, index=True)
   title = db.Column(db.String(128))
   text = db.Column(db.String)

   def __repr__(self):
      return '<Offer {0}, user_id {1}>'.format(self.id, self.user_id)


   # def set_password(self, password):
   #    self.password_hash = generate_password_hash(password)

   # def check_password(self, password):
   #    return check_password_hash(self.password_hash, password)

   # def get_password_token(self, expires_in=6000):
   #    return jwt.encode(
   #          {'user_id': self.id, 'exp': time() + expires_in},
   #          app.config['SECRET_KEY'], algorithm='HS256')

   # @staticmethod
   # async def verify_password_token(token):
   #    try:
   #       id = jwt.decode(token, app.config['SECRET_KEY'],
   #                         algorithms=['HS256'])['user_id']
   #    except:
   #       return
   #    return await User.get(id)

   # @staticmethod
   # async def create_user(validated_data):
   #    user = User(username=validated_data['username'], email=validated_data['email'])
   #    user.set_password(validated_data['password'])
   #    try:
   #       return await user.create()
   #    except UniqueViolationError as e:
   #       abort(400, {'Error': e.message}) 
   #    except:
   #       abort(400, {'Error': 'Something went wrong!'})

   # @staticmethod
   # async def auth_user(validated_data):
   #    user = await User.query.where(User.username == validated_data['username']).gino.first()
   #    if (user is not None) and (user.check_password(validated_data['password'])):
   #       return user

   # def __repr__(self):
   #    return '<User {}>'.format(self.username)

   

     
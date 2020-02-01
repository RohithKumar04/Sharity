import datetime

from connexion import NoContent
from flask import request, g
from app.MethodView import SuperView
import datetime
import jwt

class UserView(SuperView):
    """ Create User service
    """
    method_decorators = []
    _decorators = []

    resource = 'user'
    projection = {'active': False, 'isAdmin': False, 'transations': False, 'password': False}

    def post(self):
      body = request.json
      '''currentUser= {
                "active":True , 
                "dateOfBirth":body["dateOfBirth"],
                "email":body["email"],
                "firstName":body["firstName"],
                "lastName":body["lastName"],
                "password":body["password"],
                "phone":body["phone"],
                "panNumber": body["panNumber"],
                "lastlogin":datetime.datetime.utcnow(),
                "isAdmin":False,
                "transations":[]
            }'''
      return self.insert(body)

    def put(self, userId):
      body = request.json
      print("put")
      return self.update(userId, body)

    def delete(self, userId):
      print("delete")
      return self.remove(userId)

    def get(self, userId):
      print("get")
      return self.retrieve(userId)

    def search(self,name=None, phoneNumber=None):
      body={}
      if name:
        body["firstName"]= name
      if phoneNumber:
        body["phone"]= phoneNumber
      return self.retrieveAll(body)
    
    
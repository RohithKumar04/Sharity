import datetime

from connexion import NoContent
from flask import request, g, jsonify
from app.MethodView import SuperView
import jwt

class AuthView(SuperView):
    """ Create auth service
    """
    method_decorators = []
    _decorators = []

    resource = 'auth'
    projection = {}


    def put(self, userId):
      body = request.json
      print("put")
      return self.update(userId, body)

    #def generatetoken(self, userId):  #not working
     # print("delete")
      #return "omg...its working"

    def get(self, user_id):
      token = {
          "userID":user_id,
      }
      return jwt.encode(token, "JWT_SECRET")

    def search(self):
      return self.retrieveAll(body)
    
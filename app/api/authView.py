import datetime

from connexion import NoContent
from flask import request, g, jsonify, session
from app.MethodView import SuperView
import jwt


class AuthView(SuperView):
    """ Create auth service
    """
    method_decorators = []
    _decorators = []

    resource = 'auth'
    projection = {}


    def put(self, user_id):

      return self.update(user_id)

    #def generatetoken(self, userId):  #not working
     # print("delete")
      #return "omg...its working"

    def get(self, user_id):
      token = {
          "userID":user_id,
      }
      head1 = jwt.encode(token, "JWT_SECRET")
      #session["token"] = str(head1.decode("utf-8"))
      return head1

    def search(self):
      print("auth search here")
      return self.retrieveAll(body)
    
    def post(self):
      return self.gridfstesting(body)

    def decode_token(self, token):
      try:
        return jwt.decode(token, "JWT_SECRET")
      except:
        return "Unauthorised", 401 

    def damnit(self):
      print("reached damnit")
      return "woohohohohoho",200
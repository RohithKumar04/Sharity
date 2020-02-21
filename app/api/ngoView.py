from connexion import NoContent
from flask import request, g
from app.MethodView import SuperView
import datetime
import gridfs

class NgoView(SuperView):
    """ Create NGO service
    """
    method_decorators = []
    _decorators = []

    resource = 'ngo' #collection name
    projection = { 'password': False,'bankDetails':False, 'documents':False,'tags':False}

    def post(self):
      body = request.json 
      return self.insert(body)

    def put(self, ngoId):
      body = request.json
      return self.update(ngoId, body)

    def delete(self, ngoId):
      return self.remove(ngoId)

    def get(self, ngoId):
      return self.coordinates(ngoId) 

    def documents(self, ngoId):       #ngo/{ngoId} => POST  action => adds docs to database and stores the IDs in current ngos data
      body = {}
      files = request.files.to_dict()
      for file in files:
        grid = self.gfs.put(files[file], filename= ngoId + file)
        body["documents." + file] = str(grid)
      return self.update(ngoId, body)

    def search(self, city= None, name= None, requiredItem=None,lowerLimit=0, upperLimit=None, latitude=80.5574,longitude=13.5655):
      body= {}
      if city:
        body["location.city"]= city
      if name:
        body["name"]= name
      if requiredItem:
        body["requirementList.name"]= requiredItem
      if lowerLimit:
        body["numberOfPeopleStaying"]= {"$gt": lowerLimit}
      if upperLimit:
        body["numberOfPeopleStaying"]= {"$lt": upperLimit}  
      
      return self.retrieveAll(body)
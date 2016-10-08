from flask import Flask
from flask import json
from flask import request
from flask import Response
import os
app = Flask(__name__)

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import utils


from simserver import SessionServer
#BEFORE TRAINING NEW MODEL - CHANGE PATH BELOW
service = SessionServer('/tmp/mirFlickr4500')

# FORMAT FOR DATA POSTED TO /index: {"id":NUMBER,"tokens":["STRING","STRING","STRING"]}

@app.route('/index', methods=['POST'])
def indexPhoto():
  print(request.json)
  service.index(request.json)
  return "Recieved: " + json.dumps(request.json)

#FORMAT FOR GET PARAMS: /query?id=PHOTO_ID

@app.route('/query', methods=['GET'])
def queryModel():
  id = str(request.args['id'])  
  tuples = service.find_similar(id, max_results=100)
  justIds = [x[0] for x in tuples]
  return Response(json.dumps(justIds), mimetype='application/json')

# TRAIN NEW MODEL

@app.route('/train', methods=['POST'])
def train():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "data/", "trainingCorpus.json")
  corpus = json.load(open(json_url))
  service.train(corpus, method='lsi')
  # service.index(corpus)
  return 'model trained'

# @app.route('/indexAll', methods=['GET'])
# def indexAll():
#   service.index(corpus)
#   return 'model indexed with whole corpus'




# corpus = [ { 'id': 0,
#     'tokens': 
#      [ 'decoration',
#        'pattern',
#        'ornate',
#        'art',
#        'traditional',
#        'design',
#        'religion',
#        'desktop',
#        'handmade',
#        'no person',
#        'craft',
#        'Easter',
#        'texture' ] },
#   { 'id': 1,
#     'tokens': 
#      [ 'recreation',
#        'water',
#        'travel',
#        'kayak',
#        'leisure',
#        'canoe',
#        'watercraft',
#        'adventure',
#        'woman',
#        'outdoors',
#        'boatman',
#        'people',
#        'paddle',
#        'water sports',
#        'mountain',
#        'fun' ] },
#   { 'id': 2,
#     'tokens': 
#      [ 'camel',
#        'Arabian camel',
#        'sitting',
#        'desert',
#        'train',
#        'Bedouin',
#        'people',
#        'two',
#        'travel',
#        'herder',
#        'silhouette',
#        'group',
#        'livestock',
#        'one',
#        'bulge',
#        'adult',
#        'no person',
#        'cavalry',
#        'three' ] },
#   { 'id': 3,
#     'tokens': 
#      [ 'water',
#        'travel',
#        'vacation',
#        'sea',
#        'people',
#        'outdoors',
#        'recreation',
#        'tourism',
#        'leisure',
#        'lake',
#        'seashore',
#        'sky',
#        'summer',
#        'landscape',
#        'boat',
#        'tourist' ] },
#   { 'id': 4,
#     'tokens': 
#      [ 'people',
#        'group',
#        'child',
#        'adult',
#        'woman',
#        'portrait',
#        'man',
#        'festival',
#        'facial expression',
#        'wear',
#        'race' ] },
#   { 'id': 5,
#     'tokens': 
#      [ 'water',
#        'fun',
#        'leisure',
#        'vacation',
#        'sea',
#        'swimming',
#        'summer',
#        'recreation',
#        'wet',
#        'travel',
#        'ocean',
#        'beach' ] },
#   { 'id': 6,
#     'tokens': 
#      [ 'seashore',
#        'water',
#        'no person',
#        'beach',
#        'sea',
#        'ocean',
#        'daylight',
#        'surf',
#        'travel',
#        'outdoors',
#        'wave',
#        'motion' ] },
#   { 'id': 7,
#     'tokens': 
#      [ 'architecture',
#        'outdoors',
#        'travel',
#        'building',
#        'city',
#        'people',
#        'tower',
#        'sky' ] },
#   { 'id': 8,
#     'tokens': 
#      [ 'mountain',
#        'travel',
#        'nature',
#        'landscape',
#        'rock',
#        'sky',
#        'dinosaur',
#        'outdoors',
#        'no person',
#        'tree',
#        'stone' ] },
#   { 'id': 9,
#     'tokens': 
#      [ 'water',
#        'sunset',
#        'sea',
#        'beach',
#        'reflection',
#        'dawn',
#        'river',
#        'ocean',
#        'boat',
#        'fisherman' ] },
#   { 'id': 10,
#     'tokens': 
#      [ 'water',
#        'beach',
#        'tropical',
#        'travel',
#        'ocean',
#        'sand',
#        'sea',
#        'summer',
#        'seashore',
#        'sky',
#        'relaxation',
#        'island',
#        'sun',
#        'exotic',
#        'vacation',
#        'idyllic',
#        'leisure',
#        'turquoise',
#        'seascape' ] },
#     {"id":"11","tokens":["people","indoors","adult","man","one","cooking","healthcare","woman","family","competition","room","wear","food","medicine","child","preparation","portrait","two","chef","industry"]} ]
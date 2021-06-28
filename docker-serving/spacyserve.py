import random
from pathlib import Path
import spacy
# from tqdm import tqdm # loading bar
# import random 
# import datetime as dt
import pandas as pd
# import PIL
# from PIL import Image
import json
import pickle
import os

model_name = 'model'

# path = os.environ["PY_MODEL_PATH"]

class SpacyNER:
    def initialize(self, path):
        
        self.path = path
    def predict(self, inputs: dict):  
        
        text =  inputs['text']
        
#         nlp2 = spacy.load(self.path)
        nlp2 = spacy.load('model')
        x = []

        doc = nlp2(text)

        for e in doc.ents:
            x.append({e.label_ :e.text})
            
        jsonData=json.dumps(x)
        
#         return jsonData
        return x
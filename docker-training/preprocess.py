import random
from pathlib import Path
import spacy
from tqdm import tqdm # loading bar
import random 
import datetime as dt
import pandas as pd
import PIL
from PIL import Image
import pickle
import os


def start():
    print("Training set is reading!")
    
#     for Ai core
    folder = os.environ["DATA_FOLDER"]
#     for own docker 

    print(folder)
    
#      The os walk to see if my file is there or not.
    
#     for root, dirs, files in os.walk(".", topdown = False):
#         for name in files:
#             print(os.path.join(root, name))
#             for name in dirs:
#                 print(os.path.join(root, name))
    
    # import the dataset 
#      start with absolute path.
    path = "."
#     for Ai core
    text = open(os.path.join(path,folder,'TRAIN_DATA.json')).read()
#      for own  docker
#     text = open(os.path.join(path,'TRAIN_DATA.json')).read()
    
#     text = open('TRAIN_DATA.txt').read()
    nlp=spacy.blank('en')
    doc=nlp(text)
    print(doc)    
    return doc
 
    
if __name__ == '__main__':
    start()
        
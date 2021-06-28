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

def test():

    """
    Evaluate the model by applying it on the test set
    Calculate the Accuracy and determine the confusion matrix
    """
    
    print("Evaluate the trained model by applying on a test set")
    folder = os.environ["MODEL_FOLDER"]
      
    
    model = pickle.load(open(os.path.join(folder, "model"),'rb'))
    
    
    text = """
    The Hardk Disk 2 TB is 800 gm and its EAN code 678686869879. 

    """
    nlp2 = spacy.load(folder)
    
    doc = nlp2(text)
    
    # Predict the model
       
    for e in doc.ents:
        print( e.label_ ,e.text )
               

if __name__ == '__main__':
    test()
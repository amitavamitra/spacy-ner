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
import json

max_iter = int(os.environ["NUMBER_OF_EPOCHS"])
# max_iter = 100
print(max_iter)
# print(os.getcwd())
# folder = os.environ["DATA_FOLDER"]
# print(folder)


def train():
    """
    Define variables for training
    """
    model = None
        
    
#     print(os.getcwd())
    folder = os.environ["DATA_FOLDER"]
#     folder = "/"
    path = "."
    with open(os.path.join(folder,'basic_data.json') ,encoding="utf8") as fp:
#     with open(os.path.join()'TRAIN_DATA.json' ,encoding="utf8") as fp:
        
        
        TRAIN_DATA = json.load(fp)
    TRAIN_DATA = TRAIN_DATA["annotations"]
#     max_iter = int(os.environ["NUMBER_OF_EPOCHS"])
#     print(max_iter)
        
#     folder = os.environ["OUT_FOLDER"]

    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    
#      create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    # prepare an empty model to train
    nlp = spacy.blank('en')
    nlp.vocab.vectors.name = 'demo'
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last = True)
    def create_blank_nlp(train_data):
        nlp = spacy.blank("en")
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
        ner = nlp.get_pipe("ner")
        for  texts,annotations in train_data:
            for ent in annotations.get("entities"):
                ner.add_label(ent[2])
        return nlp

    import datetime as dt

    from spacy.util import minibatch, compounding
    from spacy_lookups_data import en
    nlp = create_blank_nlp(TRAIN_DATA)
    optimizer = nlp.begin_training()
    for i in range(max_iter):
        losses = {}
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            texts, annotations = zip(*batch)
            nlp.update( 
            texts,  # batch of texts
            annotations,  # batch of annotations
            drop=0.2,  # dropout - make it harder to memorise data
            losses=losses,
             )
        print(f"Losses at iteration {i} - {dt.datetime.now()} {losses}")
    
         
    
#     output_dir = os.environ["MODEL_FOLDER"]
    
#     nlp.to_disk(output_dir)
    
    model_location = ('/app/model')
   
    folder = os.environ["MODEL_FOLDER"]
#     folder = "/"
    nlp.to_disk(folder)
    print("Saved model to" , folder)
    
    pickle.dump(model, open(os.path.join(folder, "model"), 'wb'))
#     ************************************************************************
    print("Evaluate the trained model by applying on a test set")
#     folder = os.environ["OUT_FOLDER"]
    
#     folder = "/"
    
    model = pickle.load(open(os.path.join(folder, "model"),'rb'))
       
    text = """
    The new product is of length 1000cm , 
    width 645 cm and height of 436 cm. It weighs 115 KG in Net and 120 KG with packaging.
    The EAN code is 55324324324387.
    """
    nlp2 = spacy.load(folder)
    
    doc = nlp2(text)
    
    # Predict the model
       
    for e in doc.ents:
        print( e.label_ ,e.text )
      
    
    
    
if __name__ == '__main__':
    train()
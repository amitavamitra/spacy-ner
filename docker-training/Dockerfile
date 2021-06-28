FROM ecoron/python36-sklearn

RUN pip install --upgrade pip
RUN pip3 install pandas
RUN pip3 install pillow
RUN pip3 install tqdm
# spaCy
########################################

RUN pip3 install spacy==2.3

RUN pip3 install spacy-lookups-data

# COPY preprocess.py preprocess.py
COPY . .
# COPY test.py test.py
# CMD [ "python","./train.py"]

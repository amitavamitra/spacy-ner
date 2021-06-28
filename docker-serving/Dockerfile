# https://github.wdf.sap.corp/ICN-ML/aicore/tree/master/centaur
# Generic/high-performance ML model serving runtime
FROM docker.wdf.sap.corp:50003/com.sap.aicore/centaur-cpu:1.2.0

ENV LANG C.UTF-8

RUN pip install --upgrade pip
RUN pip3 install pandas
RUN pip3 install pillow
RUN pip3 install tqdm
# spaCy
########################################


RUN pip3 install spacy==2.3

RUN pip3 install spacy-lookups-data

COPY requirements.txt ./

# create venv and install dependencies
COPY install_libs.sh ./
RUN ./install_libs.sh

COPY spacyserve.py /app/

COPY . .

CMD ["centaur"]
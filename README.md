# distractor_generation_api

This is a simple Flask API that returns alternative options (distractors) for an MCQ, given the correct answer. It uses Sense2Vec to determine the distractors.

## Steps to run:
1. Download and unzip Sense2Vec vectors to your project folder.
  >!wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
  
  >!tar -xvf  s2v_reddit_2015_md.tar.gz
2. Install dependencies to your python environment.
  >pip install -r requirements.txt 

3. Start the server.
  >python server.py


## Access the endpoints from your browser in the following ways:
(Default number of options is 5)
1. http://0.0.0.0:5002/distractor/london
2. http://0.0.0.0:5002/distractor/london/10

Replace london and 10 with your preferences.

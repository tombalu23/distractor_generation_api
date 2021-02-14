from flask import Flask, jsonify
import spacy
import sense2vec
from collections import OrderedDict

app = Flask(__name__)

nlp = spacy.load('en_core_web_sm')
s2v = sense2vec.Sense2Vec().from_disk('./sense2vec_old/s2v_old/')


def sense2vec_get_words(word, s2v, n):
    output = []
    word = word.lower()
    word = word.replace(" ", "_")

    sense = s2v.get_best_sense(word)
    most_similar = s2v.most_similar(sense, n)

    # print ("most_similar ",most_similar)

    for each_word in most_similar:
        append_word = each_word[0].split("|")[0].replace("_", " ").lower()
        if append_word.lower() != word:
            output.append(append_word.title())

    out = list(OrderedDict.fromkeys(output))
    return out


@app.route("/")
def hello_world():
  return "Distractor Generator Service"

# Get <n> distractors for <word>
@app.route('/distractor/<word>', methods=['GET'])
@app.route('/distractor/<word>/<int:n>', methods=['GET'])
def get_distractors(word, n=5):
    distractors = sense2vec_get_words(word, s2v, n)
    return jsonify({'distractors': distractors})

if __name__ == '__main__':
    app.run(host ='0.0.0.0',port=5002, debug = True)
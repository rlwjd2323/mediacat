import pickle
from konlpy.tag import Mecab
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence, text
from tensorflow.keras.models import load_model
from tensorflow.python.keras.backend import set_session
from preprocessing import clean_text

tagger = Mecab()

# import re
# def clean_text(sentence):
#     return re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》△▲\"\'◆■●■◇]', '', sentence.replace(' ',''))


tokenizer_path = "/mnt/d/workpython/workspace/keras/sentiment/tokenizer/tokenizer.pickle"
glove_path = "/mnt/d/workpython/workspace/keras/sentiment/embedding/glove/glove.6B.100d.txt"
max_len = 49
model_path = "/mnt/d/workpython/workspace/keras/sentiment/model/model.h5"



def load_tokenizer(path) :
    tokenizer = None
    try:
        with open(path, "rb") as f :
            tokenizer = pickle.load(f)
    except:
        tokenizer = None
    return tokenizer

    
class Sentiment:

    def __init__(self):
        self.sess = tf.Session()
        self.graph = tf.get_default_graph()
        set_session(self.sess)
        self.loaded_model = load_model(model_path)
        self.loaded_model._make_predict_function()
        self.tokenizer = load_tokenizer(tokenizer_path)
        print('load model success!')


    def run_predict(self, new_sentence):
        score = 0
        sentence = clean_text(new_sentence)
        tokens = [tagger.morphs(sentence)]
        
        encoded = self.tokenizer.texts_to_sequences(tokens)
        pad_new = sequence.pad_sequences(encoded, maxlen = max_len)

        try:
            with self.graph.as_default():
                set_session(self.sess)
                score = float(self.loaded_model.predict(pad_new, verbose=0)) 
        except Exception as e:
            print(e)
        if(score > 0.5):
            return {"result":"1", "score":str(score * 100)}
        else:
            return {"result":"0", "score":str((1 - score) * 100)}

if __name__=="__main__":
    res = Predict().run_predict("시간 때우기에 좋음")
    print(res)
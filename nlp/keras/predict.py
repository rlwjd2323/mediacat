from sentiment import Sentiment


def predict_sentiment(sentence):
    return Sentiment().run_predict(sentence) 


print(predict_sentiment("진짜 짜증남"))
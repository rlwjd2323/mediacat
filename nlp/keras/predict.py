from sentiment import Sentiment


def predict_sentiment(sentence):
    return Sentiment().run_predict(sentence) 


print(predict_sentiment("시간 때우기에 좋음"))
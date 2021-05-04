from flask import Flask, request
import json
from sentiment.predict import Predict

app = Flask(__name__)

predict = None


@app.route('/post', methods = ['POST'])
def post():

    try:
        # get JsonBody
        json_body = request.get_json(force=True)
        sentence = json_body["sentence"]
        result = predict.run_predict(sentence)
        return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    predict = Predict()
    app.run(host='0.0.0.0', debug = True)
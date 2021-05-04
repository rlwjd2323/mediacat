import numpy as np
import pandas as pd 
from konlpy.tag import Mecab
import pickle
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.python.keras.backend import set_session
from tensorflow.keras.preprocessing import sequence, text
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from preprocessing import clean_text
from modeling import build_model

sess = tf.Session()
set_session(sess)
tagger = Mecab()

max_len = 49

# tokenizer 생성 및 저장
def create_tokenizer(x_train, tokenizer_path):
    print(x_train)
    # tokenizer 생성
    tokenizer = text.Tokenizer(num_words=None)
    tokenizer.fit_on_texts(list(x_train))
    # tokenizer 저장
    with open(tokenizer_path, "wb") as f :
        pickle.dump(tokenizer, f, pickle.HIGHEST_PROTOCOL)

    return tokenizer


def below_threshold_len(max_len, nested_list):
    cnt = 0
    for s in nested_list:
        if(len(s) <= max_len):
            cnt = cnt + 1
    print('전체 샘플 중 길이가 %s 이하인 샘플의 비율: %s'%(max_len, (cnt / len(nested_list))*100))

def run_train(data_path, tokenizer_path, epoch, batch_size, model_path):

    # 데이터 업로드
    total_data = pd.read_csv(data_path)
    total_data['text'].nunique(), total_data['label'].nunique()
    total_data.drop_duplicates(subset=['text'], inplace=True) # reviews 열에서 중복인 내용이 있다면 중복 제거
    
    # 전처리
    stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게', '만', '게임', '겜', '되', '음', '면']
    total_data['text'] = total_data['text'].apply(clean_text)
    total_data['tokenized'] = total_data['text'].apply(tagger.morphs)
    total_data['tokenized'] = total_data['tokenized'].apply(lambda x: [item for item in x if item not in stopwords])

    x_train, x_test, y_train, y_test = train_test_split(total_data.tokenized.values, total_data.label.values, 
                                                  stratify=total_data.label.values, 
                                                  random_state=42, 
                                                  test_size=0.1, shuffle=True)

    # 단어 vocab 생성
    tokenizer = create_tokenizer(x_train, tokenizer_path)

    word_index = tokenizer.word_index


    # 토큰 seq index값으로 변경
    x_train_seq = tokenizer.texts_to_sequences(x_train)
    x_test_seq = tokenizer.texts_to_sequences(x_test)


    # mex_len으로 자르기
    x_train_pad = sequence.pad_sequences(x_train_seq, maxlen=max_len)
    x_test_pad = sequence.pad_sequences(x_test_seq, maxlen=max_len)


    # # embedding matix 생성
    # embedding_matrix = EmbedingGlove(glove_path).create_embedding_matrix(word_index)

    # 모델 빌드
    model = build_model(word_index, max_len)

    #모델 학습
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
    mc = ModelCheckpoint(model_path, monitor='val_acc', mode='max', verbose=1, save_best_only=True)
    model.fit(x_train_pad, y_train, epochs=int(epoch), callbacks=[es, mc], batch_size=int(batch_size), validation_split=0.1)

    #모델 평가
    print("테스트 정확도: %.4f" % (model.evaluate(x_test_pad, y_test)[1]))



if __name__=="__main__":
    run_train()



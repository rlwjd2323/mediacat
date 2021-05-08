#!/bin/sh

func=sentiment

python=/mnt/d/workpython/anaconda3/bin/python
data_path=/mnt/d/workpython/workspace/mediacat/nlp/keras/sentiment/data/sentiment_ko.csv
tokenizer_path=/mnt/d/workpython/workspace/mediacat/nlp/keras/sentiment/tokenizer/tokenizer.pickle
# glove_path=/mnt/d/workpython/workspace/keras/sentiment/embedding/glove/glove.6B.100d.txt
epoch=20
batch_size=64
model_path=/mnt/d/workpython/workspace/mediacat/nlp/keras/sentiment/model/model.h5

$python train.py --func $func --data_path $data_path --tokenizer_path $tokenizer_path --epoch $epoch --batch_size $batch_size --model_path $model_path
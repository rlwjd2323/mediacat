import argparse
from sentiment import run_train

# argument
parser = argparse.ArgumentParser(description="keras train model")
parser.add_argument("--func",required=False)
parser.add_argument("--data_path",required=False)
parser.add_argument("--tokenizer_path",required=False)
parser.add_argument("--epoch",required=False)
parser.add_argument("--batch_size",required=False)
parser.add_argument("--model_path",required=False)

args = parser.parse_args()

func = args.func
data_path = args.data_path
tokenizer_path = args.tokenizer_path
epoch = args.epoch
batch_size = args.batch_size
model_path = args.model_path

if func == "sentiment":
    from sentiment import run_train
    run_train(data_path, tokenizer_path, epoch, batch_size, model_path)


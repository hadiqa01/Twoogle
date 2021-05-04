from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
from transformers import pipeline, DistilBertForSequenceClassification, DistilBertTokenizerFast


parser = argparse.ArgumentParser(description='Sentiment Analysis')
parser.add_argument('text', help='tweet text')
args = parser.parse_args()

# Sentiment classes
LABELS = {'LABEL_0': 'NEGATIVE', 'LABEL_1': 'POSITIVE'}

model = pipeline('sentiment-analysis',
        model=DistilBertForSequenceClassification.from_pretrained("model"),
        tokenizer=DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased'))
result = model(args.text)
sentiment = LABELS[result[0].get('label')]
score = result[0].get('score')

if __name__ == "__main__":
    print('\n' + f'The sentiment for the text `{args.text}` is {sentiment} with a probaility of {round(score, 5)}.')

import pandas as pd
import numpy as np

# read the csv file
query_df = pd.read_csv("Tweetler.csv", error_bad_lines=False)
query_df = query_df.iloc[:82159]  # subset of dataframe
query_df['tweet'] = query_df['tweet'].astype(str)
print(query_df['tweet'])

#text processing(text verisini normalize etmek)
import re
import string
import nltk
from gensim import corpora, models, similarities
from nltk.corpus import stopwords
import gensim
import pyLDAvis.gensim

from gensim import corpora, models, similarities

tokenized = query_df['tweet']
print(tokenized)
dictionary = corpora.Dictionary(tokenized)
dictionary.filter_extremes(no_below=1, no_above=0.8)
corpus = [dictionary.doc2bow(tokens) for tokens in tokenized]
print(corpus[:1])

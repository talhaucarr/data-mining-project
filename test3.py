from gensim import corpora
from gensim.models.ldamodel import LdaModel

import nltk
nltk.download('punkt')

import pandas as pd
import numpy as np
#read the csv file
query_df = pd.read_csv("veri_vize.csv",error_bad_lines=False)
query_df = query_df.iloc[:95889]#subset of dataframe
query_df['0'] = query_df['0'].astype(str)
query_df['0'].head()

query_df['0'].head(10)

from gensim import corpora, models, similarities

from nltk.tokenize import word_tokenize, sent_tokenize

def tokenn(sentence):
    a=word_tokenize(sentence)
    return a

# clean texts and create new column "tokenized"
import time
t1 = time.time()
query_df['tokenized_texts'] = query_df['0'].apply(tokenn)
t2 = time.time()
print("Time to clean and tokenize", len(query_df), "texts:", (t2-t1)/60, "min") #Time to clean and tokenize 3209 reviews: 0.21254388093948365 min

import gensim
import pyLDAvis.gensim

#Create a Gensim dictionary from the tokenized data
tokenized = query_df['tokenized_texts']
#Creating term dictionary of corpus, where each unique term is assigned an index.
dictionary = corpora.Dictionary(tokenized)
#Filter terms which occurs in less than 1 query and more than 80% of the queries.
dictionary.filter_extremes(no_below=1, no_above=0.8)
#convert the dictionary to a bag of words corpus
corpus = [dictionary.doc2bow(tokens) for tokens in tokenized]
print(corpus[:1])

#LDA
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 5, id2word=dictionary, passes=15)
ldamodel.save('mOdel.gensim')#save model
topics = ldamodel.print_topics(num_words=30)#words in each topic group

#5 topic and topic groups
for topic in topics:
   print(topic)

   get_document_topics = ldamodel.get_document_topics(corpus[0])
   print(get_document_topics)


def dominant_topic(ldamodel, corpus, content):
    # Function to find the dominant topic in each query
    sent_topics_df = pd.DataFrame()
    # Get main topic in each query
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each query
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # =&gt; dominant topic
                wp = ldamodel.show_topic(topic_num, topn=30)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(
                    pd.Series([int(topic_num), round(prop_topic, 4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']
    contents = pd.Series(content)  # noisy data
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return (sent_topics_df)


df_dominant_topic = dominant_topic(ldamodel=ldamodel, corpus=corpus, content=query_df['0'])
df_dominant_topic.head(10)

df_dominant_topic.to_csv('vize_tekonize.csv')#save your results
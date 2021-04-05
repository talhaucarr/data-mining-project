"""import pandas as pd

df = pd.read_csv('tr_tekonize.csv')

print(df['tweet'])
print("####################################")
print("####################################")
print("####################################")

df = pd.read_csv('output.csv')

print(df['tweet'])
"""
import gensim
import pyLDAvis.gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel
lda_viz = gensim.models.ldamodel.LdaModel.load('mOdel.gensim')#load lda model
lda_display = pyLDAvis.gensim.prepare(lda_viz, corpus, dictionary, sort_topics=True)
pyLDAvis.display(lda_display)
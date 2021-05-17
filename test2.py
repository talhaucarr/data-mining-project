# Python program to generate word vectors using Word2Vec 
# importing all necessary modules 
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')
import gensim
from gensim.models import Word2Vec

stopWords = set(stopwords.words('turkish'))

"""sentence = ["Antalya Valisi Münir Karaloğlu, kırmızı kırmızı kırmızı kırmızı kodlu uyarının yapıldığı Antalya'da gece yarısında yağışın hızlanacağını belirterek",
            "Kriz merkezinin yönettiği bin 452 personel hazır durumda. 213 ekibimiz var, 252 iş makinesi ve 124 kamyonla olayı takip ediyoruz. dedi."]
"""

with open('enes.csv',encoding="utf8") as f:
    sentence = [line.rstrip() for line in f]


data = []
# iterate through each sentence in the file
for i in sentence:
    for w in sent_tokenize(i):
        temp = []

    # tokenize the sentence into words
for a in sentence:
    words = word_tokenize(a)
    for w in words:
        if w not in stopWords:
            temp.append(w)
    data.append(temp)
"""
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
text = []
for i in sentence:
    text.append(i)
text = ''.join(map(str, text))
wordcloud = WordCloud(width=6000, height=1000, max_font_size=300, background_color='white').generate(text)
plt.figure(figsize=(20,17))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()"""

# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count=1, vector_size=200, window=10, alpha=0.25)
gensim.models.Word2Vec.load("word2vec.wordvectors")
model1.save("word2vec.wordvectors")
# Print results
print("Cosine similarity between 'kodlu' " +
            "ve  'uyarının' - CBOW : ",
    model1.wv.similarity('çizik','bilek'))

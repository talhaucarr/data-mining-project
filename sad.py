from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')
import gensim
from gensim.models import Word2Vec
model1 = gensim.models.Word2Vec.load("word2vec.wordvectors")

print("Cosine similarity between 'kodlu' " +
            "ve  'uyarının' - CBOW : ",
    model1.wv.similarity('Pratik','güzel'))
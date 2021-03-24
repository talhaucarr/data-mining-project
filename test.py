import time
import logging
import re

def remove_emoji(string):

    return(' '.join(re.sub("[0-9]|(#[A-Za-z0-9ığşöçüİĞŞÖÇÜâÂÎî]+)|(@[A-Za-z0-9ığşöçüâÂÎîİĞŞÖÇÜ]+)|([^0-9A-Za-zığşöçüİâÂÎîĞŞÖÇÜ\t])|(\w+:\/\/\S+)"," ", string).split()))

from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)

logger = logging.getLogger(__name__)

examples = ["grmek için renklere mi ihtiyacımız var hayatı siyah beyaz sevenlere günaydın",]

morphology = TurkishMorphology.create_with_defaults()
cumleTemp = ""
exp = """Bir içimin alacakaranlığına dayanmak meselesi
Bir bu fena İstanbul akşamını yaşamak
Nice odaların kapanmış penceresi
Gene bana iniyor yalnızlığıma sığınmak"""

expList = exp.split()
for kelime in expList:

    results = morphology.analyze(kelime)
    sa = str(results)
    sa = sa.split(":")[0][1:]
    cumleTemp += sa + " "
print(cumleTemp.lower())



# SENTENCE NORMALIZATION
start = time.time()
normalizer = TurkishSentenceNormalizer(morphology)
logger.info(f"Normalization instance created in: {time.time() - start} s")

start = time.time()
for example in examples:
    print(example)
    test = remove_emoji(example)
    print(normalizer.normalize(test), "\n")

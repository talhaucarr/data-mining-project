import pymongo
import re


def remove_emoji(string):
    return (' '.join(re.sub(
        "[0-9]|(#[A-Za-z0-9ığşöçüİĞŞÖÇÜâÂÎî]+)|(@[A-Za-z0-9ığşöçüâÂÎîİĞŞÖÇÜ]+)|([^0-9A-Za-zığşöçüİâÂÎîĞŞÖÇÜ\t])|(\w+:\/\/\S+)"," ", string).split()))


from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['VeriMadenciligi']
mycol = mydb["Tweets"]

morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

for x in mycol.find():
    try:
        myquery = {"tweet": x["tweet"]}
        temp = remove_emoji(x["tweet"])
        new_values = {"$set": {"tweet": normalizer.normalize(temp)}}
        mycol.update_one(myquery, new_values)
        print(normalizer.normalize(temp))

    except:
        continue

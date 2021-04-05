import pymongo
import re
import threading
from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)


def remove_emoji(string):
    return (' '.join(re.sub(
        "[0-9]|(#[A-Za-z0-9ığşöçüİĞŞÖÇÜâÂÎî]+)|(@[A-Za-z0-9ığşöçüâÂÎîİĞŞÖÇÜ]+)|([^0-9A-Za-zığşöçüİâÂÎîĞŞÖÇÜ\t])|(\w+:\/\/\S+)",
        " ", string).split()))



def my_func():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['VMadenciligi']
    mycol = mydb["Tweetler"]
    sayac = 0

    morphology = TurkishMorphology.create_with_defaults()
    normalizer = TurkishSentenceNormalizer(morphology)

    cumleTemp = ""

    for x in mycol.find().skip(80259).limit(1900):
        cumleTemp = ""
        try:
            myquery = {"created_at": x["created_at"], "status_id": x["status_id"], "status_id_str": x["status_id_str"],
                       "source": x["source"],
                       "screen_name": x["screen_name"],
                       "source_url": x["source_url"],
                       "user_id": x["user_id"], "tweet": x["tweet"],
                       "location": x["location"], "lang": x["lang"]}
            temp = remove_emoji(x["tweet"])
            temp = normalizer.normalize(temp)
            expList = temp.split()

            for kelime in expList:
                results = morphology.analyze(kelime)
                sa = str(results)
                sa = sa.split(":")[0][1:]
                cumleTemp += sa + " "

            sayac += 1
            print(cumleTemp)

            new_values = {"$set": {"tweet": cumleTemp}}
            mycol.update_one(myquery, new_values)


        except:
            continue

my_func()
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
    print("sadas")
    mydb = myclient['Vize']
    mycol = mydb["veri"]
    sayac = 0

    morphology = TurkishMorphology.create_with_defaults()
    normalizer = TurkishSentenceNormalizer(morphology)


    for x in mycol.find():
        cumleTemp = ""
        try:
            myquery = {"0":x["0"],"1":x["1"]}
            temp = remove_emoji(x["0"])
            if(len(temp) < 125):
                print(temp)
                temp = normalizer.normalize(temp)

                expList = temp.split()

                for kelime in expList:
                    results = morphology.analyze(kelime)
                    sa = str(results)
                    sa = sa.split(":")[0][1:]
                    cumleTemp += sa + " "

                sayac += 1


                new_values = {"$set": {"0": cumleTemp}}
                mycol.update_one(myquery, new_values)

            else:
                mycol.delete_one(myquery)


        except:
            continue

my_func()
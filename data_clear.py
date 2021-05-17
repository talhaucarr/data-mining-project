import pymongo
import re
import pandas as pd
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


def read_data_from_csv():
    df = pd.read_csv('magaza_yorumlari_duygu_analizi.csv',header=0, encoding='utf16', engine='python')
    file = open("temizlenmis_veri_midterm.txt","a",encoding='utf-16')

    morphology = TurkishMorphology.create_with_defaults()
    normalizer = TurkishSentenceNormalizer(morphology)



    for ind in df.index:
        cumleTemp = ""
        temp = remove_emoji(df['Görüş'][ind])
        file.write(temp)
        temp = normalizer.normalize(temp)
        expList = temp.split()



        for kelime in expList:
            results = morphology.analyze(kelime)
            sa = str(results)
            sa = sa.split(":")[0][1:]
            cumleTemp += sa + " "
        print(cumleTemp)
        file.write(cumleTemp+"\n")






    file.close()
read_data_from_csv()
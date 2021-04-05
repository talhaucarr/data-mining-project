import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

#setting the directory and Downloading the dataset
#os.chdir('directory')
dataset = pd.read_csv('tr_tekonize.csv')

#Separating the Data Set into Dependent and Independent Attributes
X = dataset.iloc[:, [2]].values
y = dataset.iloc[:, 1].values

#Separating Data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)

"""
#Bagimsiz degiskenler ayni birimde olmadigi zaman kullanilir. Bu durumda tek bagimsiz degisken oldugu icin kapatilmistir.
#Normalization - Feature Scaling 

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

#Creating and Training the SVM Model
classifier = SVC(kernel='linear', random_state = 0)
classifier.fit(X_train, y_train)

#Estimating with a Test Set
y_pred = classifier.predict(X_test)

#Creating the Error Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#Result Analysis
s1 = 0
s2 = 0
for i in range(len(cm)):
    for j in range(len(cm[i])):
        s1 += cm[i][j]
        if i==j:
            s2 += cm[i][j]
            
print("Toplam Veri: ",s1)
print("Doğru Tahmin: ",s2)
print("Dogruluk oranı: ",round(s2/s1,5))
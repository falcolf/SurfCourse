import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
dataset = pd.read_csv('datafile.csv', delimiter = '\t', quoting = 3)
import re
import nltk

#nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 8995):
    keywords = re.sub('[^a-zA-Z]', ' ', dataset['Keywords'][i])
    keywords = keywords.lower()
    keywords = keywords.split()
    ps = PorterStemmer()
    keywords = [ps.stem(word) for word in keywords if not word in set(stopwords.words('english'))]
    keywords = ' '.join(keywords)
    corpus.append(keywords)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X_train = cv.fit_transform(corpus).toarray()
y_train = dataset.iloc[:, 1].values


from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
#ypred = classifier.predict(X_test.toarray())

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf')
classifier.fit(X_train , y_train)

from sklearn.neighbors import KNeighborsClassifier
cs = KNeighborsClassifier(n_neighbors= 5 , metric='minkowski' , p=2)
cs.fit(X_train , y_train)

from sklearn.ensemble import RandomForestClassifier
cs = RandomForestClassifier()
cs.fit(X_train , y_train)


with open('cntvect2.pkl','wb') as handle:
    pickle.dump(cv,handle)
    
with open('classifier2.pkl','wb') as handle:
    pickle.dump(cs,handle)



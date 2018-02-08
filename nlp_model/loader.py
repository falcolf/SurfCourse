# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


from sklearn.feature_extraction.text import CountVectorizer
with open('cntvect.pkl', 'rb') as fid:
    cv = CountVectorizer
    cv= pickle.load(fid)
from sklearn.naive_bayes import GaussianNB
with open('classifier.pkl', 'rb') as fid2:
    classifier = GaussianNB()
    classifier= pickle.load(fid2)

ps = PorterStemmer()
query = 'cats and dogs'
quer = query.lower()
query = query.split()
query = [ps.stem(word) for word in query if not word in set(stopwords.words('english'))]
query = ' '.join(query)
X_test = cv.transform([query])
ypred = classifier.predict(X_test.toarray())


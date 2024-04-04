# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 09:46:00 2023

@author: rac
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("Tweets.csv")

text_columns = ['B', 'D', 'F', 'K']  

themes_list = []  # Initialize an empty list to store themes

for index, row in data.iterrows():
    text_data = ' '.join(row[column] for column in text_columns)
    
    tfidf_vectorizer = TfidfVectorizer(max_features=1000)  
    tfidf_matrix = tfidf_vectorizer.fit_transform([text_data])
    
    sor_indices = tfidf_matrix.toarray().argsort()[0][-4:]  # Get indices of top 4 TF-IDF values
    themes_list.append(list(sor_indices))

data['Tfidf_theme'] = themes_list  # Add the list of indices as a new column

data.to_csv("Tweet_modified1.csv", index=False)
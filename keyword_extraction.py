# -*- coding: utf-8 -*-
"""Keyword extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wkKYlBxdRtbicHBjcl8hfYm12Y7E4tow
"""

import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')

nltk.download('stopwords')

def clean_text(text):
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

def extract_keywords(job_description, top_n=10):
    # Tokenize and clean the text
    job_description = clean_text(job_description)
    tokens = nltk.word_tokenize(job_description)

def extract_keywords(job_description, top_n=10):
    # Tokenize and clean the text
    job_description = clean_text(job_description)
    tokens = nltk.word_tokenize(job_description)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Calculate word frequencies
    word_freq = Counter(tokens)

    # Get the top N keywords based on word frequencies
    top_keywords = word_freq.most_common(top_n)

    return top_keywords

job_description = """
We are looking for a software engineer with experience in Python and machine learning.
The candidate should have strong problem-solving skills and a background in computer science.
Experience with natural language processing and data analysis is a plus.
"""

keywords = extract_keywords(job_description)
print("Keywords:", keywords)

data_analyst_job_description = """
We are seeking a data analyst with experience in SQL and statistical analysis.
The ideal candidate should have a strong background in data visualization and be proficient in tools like Tableau.
Experience in cleaning and analyzing large datasets is a plus.
"""

data_scientist_job_description = """
As a data scientist, you will be responsible for developing and implementing machine learning models.
The candidate should have expertise in Python, R, and data preprocessing techniques.
Experience with deep learning and natural language processing is highly desirable.
"""

data_analyst_keywords = extract_keywords(data_analyst_job_description)
print("Data Analyst Keywords:", data_analyst_keywords)

data_scientist_keywords = extract_keywords(data_scientist_job_description)
print("Data Scientist Keywords:", data_scientist_keywords)
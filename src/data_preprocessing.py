import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore",category=DeprecationWarning)
# Importing the usual utilities
import numpy as np
import pandas as pd
import re, random, os, string

from pprint import pprint  # pretty print
import matplotlib.pyplot as plt
import os
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from string import punctuation
from nltk.corpus import stopwords
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.models import ldamodel, LsiModel
from joblib import dump, load

def data_preprocessing(df: pd.DataFrame):
    # marking an array of sentences
    Normalize_rev_lower = [rev.lower() for rev in df.review.values]

    # Checking any links present in the review
    df[df["review"].apply(lambda x: x.find("http") > 0)]["review"].apply(
        lambda x: re.sub(r"http\S+", "", x)
    )

    # Making an array of sentences with lower values
    Normalize_rev_lower = [rev.lower() for rev in df.review.values]

    # tokenization of  words from normalize sentences
    reviews_word_token = [word_tokenize(sent) for sent in Normalize_rev_lower]

    # Converting all the tags in to pos tag tuple
    reviews_pos_tagged = [nltk.pos_tag(tokens) for tokens in reviews_word_token]

    # making an array of only for nouns
    reviews_noun = []
    for sent in reviews_pos_tagged:
        reviews_noun.append([token for token in sent if re.search("NN.*", token[1])])

    # Extracting the words
    only_nowns = []
    for sent in reviews_noun:
        nowns_row_wise = []
        for tup in sent:
            nowns_row_wise.append(tup[0])
        only_nowns.append(nowns_row_wise)
    # now lemmatize to get the root of the word
    lemm = WordNetLemmatizer()
    reviews_lemm = []
    for sent in only_nowns:
        reviews_lemm.append([lemm.lemmatize(word) for word in sent])
    stop_nltk = stopwords.words("english")

    stop_updated = stop_nltk + list(punctuation) + ["..."] + [".."]
    reviews_sw_removed = []
    for sent in reviews_lemm:
        reviews_sw_removed.append([term for term in sent if term not in stop_updated])
    dump(reviews_sw_removed,'model/reviews.pkl')


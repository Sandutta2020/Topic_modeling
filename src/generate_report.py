import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.models import ldamodel, LsiModel
from joblib import dump, load
from utilities import read_yaml
import pyLDAvis.gensim
import pandas as pd

param =read_yaml("conf/best_params.yaml","opt_topic")
print(param)
lda_model =load("model/lda_model.pkl")
reviews_sw_removed = load("model/reviews.pkl")
id2word = corpora.Dictionary(reviews_sw_removed)
texts = reviews_sw_removed
corpus = [id2word.doc2bow(text) for text in texts]
# print('\nCoherence Score: ', coherence_lda)
#print("\nPerplexity: ", lda_model.log_perplexity(corpus))
vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
pyLDAvis.save_html(vis, "report/lda.html")
# print(lda_model.print_topics())
x = lda_model.show_topics(formatted=False)
topics_words = [(tp[0], [wd[0] for wd in tp[1]]) for tp in x]
df_topics =pd.DataFrame(topics_words,columns =['Topic ID','Topics'])
df_topics.to_csv("report/topics.csv",index =False)


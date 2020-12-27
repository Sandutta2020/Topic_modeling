import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.models import ldamodel, LsiModel
from joblib import load,dump
from utilities import dump_yaml,read_yaml

def main(start,end):
    max_topic_no =start
    min_score =0
    reviews_sw_removed = load("model/reviews.pkl")
    id2word = corpora.Dictionary(reviews_sw_removed)
    texts = reviews_sw_removed
    corpus = [id2word.doc2bow(text) for text in texts]
    for i in range(start,end):
        lda_modeli = gensim.models.ldamodel.LdaModel(
            corpus=corpus,
            id2word=id2word,
            num_topics=i,
            random_state=42,
            passes=10,
            per_word_topics=True,
        )
        coherence_model_lda = CoherenceModel(
            model=lda_modeli,
            texts=reviews_sw_removed,
            dictionary=id2word,
            coherence="c_v",
        )
        coherence_lda = coherence_model_lda.get_coherence()
        print("topis no ", i, "Coherence Score: ", coherence_lda)
        if max_topic_no ==i:
            max_score =coherence_lda
            dump(lda_modeli,'model/lda_model.pkl')
        else:
            if coherence_lda > max_score :
                max_topic_no = i
                max_score =coherence_lda
                dump(lda_modeli,'model/lda_model.pkl')

    dump_yaml({"opt_topic" :max_topic_no},"conf/best_params.yaml" )
            



if __name__ == "__main__":
    start =read_yaml("params.yaml","startTopic")
    end =read_yaml("params.yaml","endTopic")
    main(start,end)

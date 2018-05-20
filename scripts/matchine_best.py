from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import operator
import numpy as np
class Similarity():
    def __init__(self,documents):
        self.tfidf_vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(documents)
        self.documents = documents

    def most_similar(self,doc):
        tfidmat = self.tfidf_vectorizer.transform(doc)
        similarvalues = list((cosine_similarity(tfidmat[0:1],self.tfidf_matrix))[0])
        similarvalues=[float(i) for i in similarvalues]
        similarvalues = dict(zip(self.documents, similarvalues))
        sorted_x = sorted(similarvalues.items(), key=operator.itemgetter(1),reverse=True)
        print(sorted_x)
        return sorted_x[0][0]


    def get_reviews(self,url_product):
        pass
if __name__=="__main__":
    obj  = Similarity(["lg washing machine","lg machine","lg washing","videocon washing"])
    print(obj.most_similar(["videocon 2014 machine"]))

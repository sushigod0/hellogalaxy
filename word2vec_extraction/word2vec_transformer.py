# create Word2vec transformer
from sklearn.base import BaseEstimator, TransformerMixin
from gensim.models import Word2Vec
from word2vec_extraction.combined_vectors import combined_vectors
import numpy as np

class Word2VecTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
      #initialising the model from the drive
        self.model = Word2Vec.load('word2vec_extraction/vec_model.model')

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):

        # Create mean vectors feature
        vec_features = combined_vectors(self.model,X)
        #reshape 1d array to 2d array for model input
        vec_features = np.reshape(vec_features,(1,100))
        return vec_features  # Return the processed data

# print("success")
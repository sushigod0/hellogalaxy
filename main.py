import json
import pandas as pd
import numpy as np
import gensim
import sklearn
from gensim.models import Word2Vec
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow import keras
from tensorflow.python.keras import layers
import scikeras
from scikeras.wrappers import KerasClassifier
from sklearn.pipeline import Pipeline
import joblib
from feature_extractor.custom_feature_extractor import CustomFeatureExtractor
from sklearn.preprocessing import StandardScaler
# from word2vec_extraction.combined_vectors import combined_vectors
from word2vec_extraction.word2vec_transformer import Word2VecTransformer
from nn_model.model_structure import model
from flask import Flask, request, jsonify



def load_model():
    
    # Initialize custom components
    feature_extractor = CustomFeatureExtractor()
    word2vec_transformer = Word2VecTransformer()
    scaler = StandardScaler()
   


    # Create a Scikit-learn pipeline
    pipeline = Pipeline([
        ("custom_features", feature_extractor),
        ("word2vec", word2vec_transformer),
        ("scaler", scaler),
        ("model", model)
    ])

    # Load your model using joblib
    model_path = 'model_for_bot_NN_v1.pkl'
    nn_model = joblib.load(model_path)
    


    # Example:predict the output
    # predict = nn_model.predict(input_data)
    # predict_proba = nn_model.predict_proba(input_data)
    # print (predict)
    # print (predict_proba)



if __name__ == "__main__":
    load_model()

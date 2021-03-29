import pickle
import os
from util import preprocess

# using the prefix path which will be used by sagemaker
prefix = "/opt/ml/"

class SimpleModel():
    # class variable used for model and other required object
    predictor = None
    vectorizer = None

    @classmethod
    def get_model(cls):
        "load model for the model files saved during the train process"

        # check if model is not already loaded 
        # if already loaded skip the the return statement
        if cls.predictor == None:
            # model path where the model will be located in the sagemaker container
            # generally it will be located at /opt/ml/model folder of the container
            model_path = os.path.join(prefix, 'model')
            with open("{}/logistic_model.pkl".format(model_path) , "rb") as fl:
                cls.predictor = pickle.load(fl)

            with open("{}/vectorizer.pkl".format(model_path) , "rb") as fl:
                cls.vectorizer = pickle.load(fl)
    
            print("Model initialized")

        # always return a model and a vectorizer
        return cls.predictor, cls.vectorizer
    
    @classmethod
    def predict(cls, input_text):
        # get the model and vectorizer.
        clf, vectorizer = cls.get_model() 

        # clean the text same a what we did while training.
        preprocessed_text = preprocess(input_text)

        # converted the cleaned text into vector
        vector = vectorizer.transform([preprocessed_text])

        # use the sklearn logistic regression predict function to make predicitions
        return clf.predict(vector)[0], clf.predict_proba(vector)[0]
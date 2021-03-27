import pickle
import os
from util import preprocess

prefix = "/home/parth/sagemaker_deployment/"
# prefix = "/opt/ml/"

class SimpleModel():
    predictor = None
    vectorizer = None

    @classmethod
    def get_model(cls):
        "load model for the model files saved during the train process"
        if cls.predictor == None:
            print("Initialised Model")
            model_path = os.path.join(prefix, 'model')
            with open("{}/logistic_model.pkl".format(model_path) , "rb") as fl:
                cls.predictor = pickle.load(fl)

            with open("{}/vectorizer.pkl".format(model_path) , "rb") as fl:
                cls.vectorizer = pickle.load(fl)
        print("return model")
        return cls.predictor, cls.vectorizer
    
    @classmethod
    def predict(cls, input_text):
        clf, vectorizer = cls.get_model() 
        preprocessed_text = preprocess(input_text)
        vector = vectorizer.transform([preprocessed_text])
        return clf.predict(vector)

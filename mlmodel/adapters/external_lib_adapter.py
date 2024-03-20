import pandas  as pd
import pickle
import numpy as np
import os
import logging

NAME_MODEL="ml_iris_classifier_02_03_24.pickle"

class singleton_load_model:
    """
    This Python class ensures only one instance exists,
    enhancing efficiency and data consistency. Well-implemented Singleton pattern.
    """
    _instance = None

    def __new__(cls):
        """
        class to load model by singleton
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            file_path = os.path.join(os.path.dirname(__file__), NAME_MODEL)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as archivo:
                    cls._instance.model = pickle.load(archivo)
            else:
                raise FileNotFoundError(f"El archivo '{file_path}' no existe.")
        return cls._instance

class lib_adapter:
    """
    Class for connecting to a pre-trained and compiled machine learning model.

    Iris_classifier.pickle

    This class loads a pre-trained machine learning model from a file and provides
    methods to interact with the model such as making predictions.
    """
    def __init__(self) -> None:
        """
        init load adapter
        """
        self.singleton_instance=singleton_load_model()

    def prediccions(self,value_inputs:list):
        """
        value_inputs: lista de listas
        debe de ser una lista de 4 valores flotantes, que representen 
        ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'] = [6.2, 3.4, 5.4, 2.3]
        """
        logging.info("start predicctions in lib adapters")
        
        _model = self.singleton_instance
        print("el model")
        print(_model.__dict_)
        print(_model.__dir_)

        inputs = pd.DataFrame(value_inputs, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])

        pred = _model.model.predict(inputs)

        predicciones = pd.DataFrame(pred, columns=['pivot_Iris-setosa', 'pivot_Iris-versicolor', 'pivot_Iris-virginica'])

        response = predicciones.to_dict(orient='records')
        
        return response
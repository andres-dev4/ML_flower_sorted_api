from django.test import TestCase
from mlmodel.adapters.external_lib_adapter import lib_adapter

class LibAdapterTestCase(TestCase):
    """
    class to testing adapter and mlmodel

    To exec only run project locally and run follo comand

        python manage.py test mlmodel
    """
    def test_prediccions_one_by_one(self):
        """
        This test function verifies the functionality of the model when processing arrays individually
        """
        adapter = lib_adapter()
        print("Test with this input adapter : [[1.3, 1.5, 1.5, 1.1]] ")
        input_values = [[1.3, 1.5, 1.5, 1.1]]
        response = adapter.prediccions(input_values)
        assert isinstance(response, list), "La respuesta no es una lista."
        print("La respuesta es una lista")
        print(response)

    def test_prediccions_by_batch(self):
        """
        This test function verifies the functionality of the model when processing arrays in batches 
        """
        adapter = lib_adapter()
        print("check with multi list : [[5.3 ,1.5 ,9.5 ,1.1], [1.3 ,1.5 ,1.5 ,1.1]] dict")
        input_values=[[5.3 ,1.5 ,9.5 ,1.1], [1.3 ,1.5 ,1.5 ,1.1]]
        response = adapter.prediccions(input_values)
        assert isinstance(response, list), "La respuesta no es una lista."
        print("La respuesta es una lista")
        print(response)
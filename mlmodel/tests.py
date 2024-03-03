from django.test import TestCase
from mlmodel.adapters.external_lib_adapter import lib_adapter

class LibAdapterTestCase(TestCase):
    def test_prediccions_one_by_one(self):
        """
        This test function verifies the functionality of the model when processing arrays individually
        """
        adapter = lib_adapter()
        input_values = [[1.3, 1.5, 1.5, 1.1]]
        response = adapter.prediccions(input_values)
        print(response)

    def test_prediccions_by_batch(self):
        """
        This test function verifies the functionality of the model when processing arrays in batches 
        """
        adapter = lib_adapter()
        input_values=[[5.3 ,1.5 ,9.5 ,1.1], [1.3 ,1.5 ,1.5 ,1.1]]
        adapter.prediccions(input_values)
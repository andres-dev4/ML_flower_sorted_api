from logging import exception
from django.http import JsonResponse
from django.shortcuts import render
from mlmodel.core.history_data_interactor import HistoryDataInteractor
import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework import views
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from mlmodel.serializers.mlmodel import FlowerSerializer


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework import status

from mlmodel.core.mlmodelflower import mlflower

class mlflowers(views.APIView):
    """
    This class provides an API interface for interacting with a machine learning model for flower analysis.

    Methods:

        - get: Retrieves the execution history of the model grouped by username.
        - post: Performs a prediction using the machine learning model and returns the result.
    Parameters:

        sdfsdf
    """


    
    def get(self,request,format=None):
        """
        Endpoint function that returns all calculated estimates, grouped by username

        Only service endpoint **GET** to read all data calculate 

        
        
        Example data structure return

            {
                "msg": "all data register",
                "data_history_by_user": {
                "manuel": [
                    {
                    "id": 9,
                    "user_name": "manuel",
                    "pivot_Iris_setosa": 1.0,
                    "pivot_Iris_versicolor": 0.0,
                    "pivot_Iris_virginica": 0.0,
                    "date": "2024-03-03T01:29:41.181Z"
                    },
                    {
                    "id": 32,
                    "user_name": "manuel",
                    "pivot_Iris_setosa": 0.0,
                    "pivot_Iris_versicolor": 0.0,
                    "pivot_Iris_virginica": 1.0,
                    "date": "2024-03-03T17:47:21.978Z"
                    }
                ],
                "miguel": [
                    {
                        "id": 3,
                        "user_name": "miguel",
                        "pivot_Iris_setosa": 0.0,
                        "pivot_Iris_versicolor": 0.0,
                        "pivot_Iris_virginica": 1.0,
                        "date": "2024-03-03T01:27:06.995Z"
                },
                       {
                "id": 8,
                "user_name": "miguel",
                "pivot_Iris_setosa": 0.0,
                "pivot_Iris_versicolor": 0.0,
                "pivot_Iris_virginica": 1.0,
                "date": "2024-03-03T01:29:31.004Z"
                    }
                ]
            }
        }
        """
        
        _history = HistoryDataInteractor()
        
        queryset = _history.reed_register()


        df = pd.DataFrame(queryset.values())
        group_by_user = df.groupby('user_name')
        data_history = group_by_user.apply(lambda x: x.to_dict(orient='records')).to_dict()

        
        response={
            "msg":"all data register",
            "data_history_by_user" : data_history
            }
        
        return JsonResponse(data=response)

    

  
    @swagger_auto_schema(request_body=FlowerSerializer())
    def post(self, request, format=None):
        """
        Endpoint to calculate clasified base in values input
        
        This API receives a list of lists where each list must contain 4 float values
        These values represent the features of the flowers to be classified
        by the pre-trained machine learning model 'iris_classifier'

        values ​​define the representation the parameters

            'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

        example response [200]:

            {
                "msg": "the model was execute succesfull",
                "prediction": [
                {
                    "pivot_Iris-setosa": 1.0,
                    "pivot_Iris-versicolor": 0.0,
                    "pivot_Iris-virginica": 0.0
                },
                {
                    "pivot_Iris-setosa": 1.0,
                    "pivot_Iris-versicolor": 0.0,
                    "pivot_Iris-virginica": 0.0
                },
                {
                    "pivot_Iris-setosa": 0.0,
                    "pivot_Iris-versicolor": 0.0,
                    "pivot_Iris-virginica": 1.0
                }
        ]

        }

        example payload:
        
            {
                "save_data":true,
                "name":"manuel",
                "inputs_values": [
                    [5.3, 0.5, 1.5, 1],
                    [5.3, 9.5, 0.9, 5],
                    [1.3, 5.5, 9.9, 3]
                ]
            }

        """
        serializer_class = FlowerSerializer
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                data =  serializer.validated_data

                list_data = data["inputs_values"]
                name=data["name"]
                save_data=data["save_data"]

                _mlflower = mlflower(list_data,name,save_data)

                predicctions = _mlflower.exec_predictions()

                response={
                    'msg':'the model was execute succesfull',
                    'prediction':predicctions
                    }

                return JsonResponse(response)

            except Exception  as e:
                print("one error was occurred",e)
                message=f" {str(e)}"
                return JsonResponse({"msg":message},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            

        error = serializer.errors
        return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)

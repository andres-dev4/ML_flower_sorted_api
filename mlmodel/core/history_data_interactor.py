from mlmodel.models import history_predictions
from datetime import datetime

class HistoryDataInteractor:
    def __init__(self):
        """
        methods init
        """
        pass

    def add_register(self, data:list,name:str):
        """
        principal function to save data interactive direcly with model
        """

        for item in data:
            prediction = history_predictions(
                user_name=name,
                pivot_Iris_setosa=item['pivot_Iris-setosa'],
                pivot_Iris_versicolor=item['pivot_Iris-versicolor'],
                pivot_Iris_virginica=item['pivot_Iris-virginica'],
                date=datetime.now()
            )
        
            prediction.save()

    def reed_register(self):
        data = history_predictions.objects.all()
        return data

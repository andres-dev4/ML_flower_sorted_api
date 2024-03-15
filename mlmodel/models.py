from django.db import models
from datetime import datetime


class history_predictions(models.Model):
    """
    history predictions model to migrate
    and generate objecst typr table in db
    Mensajes history
    """
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    pivot_Iris_setosa = models.FloatField()
    pivot_Iris_versicolor = models.FloatField()
    pivot_Iris_virginica = models.FloatField()
    date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        """
        method str to  get data
        """
        return f"Iris ({self.pivot_Iris_setosa}, {self.pivot_Iris_versicolor}, {self.pivot_Iris_virginica})"

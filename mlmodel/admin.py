from django.contrib import admin
from .models import history_predictions

# Register your models here.

@admin.register(history_predictions)
class HistoryPredictionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'pivot_Iris_setosa', 'pivot_Iris_versicolor', 'pivot_Iris_virginica', 'date')
    list_filter = ('user_name', 'date')
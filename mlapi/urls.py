"""
URL configuration for mlapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from mlmodel.views  import MlFlowersView


schema_view = get_schema_view(
   openapi.Info(
      title="ML flowers classifier APIs",
      default_version='v0.2.0',
      description="""
      This endpoint classifies a flower using a pre-trained machine learning model.
      It accepts a list of input values representing the characteristics of the flower and 
      returns the predicted classification for that flower.

      The model was trained  with this values

      	    Id	SepalLengthCm	SepalWidthCm	PetalLengthCm	PetalWidthCm	Species	            pivot_Iris-setosa	pivot_Iris-versicolor	pivot_Iris-virginica
                1	  5.1	            3.5	            1.4	            0.2	            Iris-setosa	        1	                0	                    0
                2	  4.9	            3.0	            1.4         	0.2	            Iris-setosa	        1	                0	                    0
                3	  4.7	            3.2	            1.3	            0.2	            Iris-setosa	        1	                0	                    0
                4     4.6	            3.1	            1.5             0.2	            Iris-setosa	        1	                0	                    0
                5	  5.0	            3.6	            1.4	            0.2	            Iris-setosa	        1	                0	                    0
      
      The values ​​must represent the following parameters
      
            'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

    If you want know more about this machine learning model in the project be one folder
    with name **mllab** with the notebooks and file to training model

    if you prefer searching data in a view, You can use admin page django with 
            user : **mluser**
            pass : **mlpass**

    in the next url

            http://localhost:8000/admin/

    for more information you can visit the follow link kaggle exercies **Iris classificator**

            https://www.kaggle.com/code/caesarmario/petal-profiling-classification-clustering?scriptVersionId=159330644


      
      """
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mlflowers',MlFlowersView.as_view(),name='mlflowers'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

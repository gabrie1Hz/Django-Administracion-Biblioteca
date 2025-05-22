from django.urls import path
from . import views
from .views import (

	     ChartData,
   get_data,




	 )



urlpatterns = [    

  
   path('dashboard/',views.dashboard, name ="dashboard"),
  # path('logout/',views.logout,name="logout")
  path('api/chart/data/', ChartData.as_view()),
  path('api/data/', get_data, name='api-data'),


  
 
  
]


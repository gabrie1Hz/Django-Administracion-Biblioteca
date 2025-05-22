from django.urls import path
from . import views 

urlpatterns = [  

		path('',views.getroutes,name="api"),
		path('books/',views.getbooks),
		path('author/',views.getauthor),
		path('book/<str:pk>',views.getbook),
		path('category/',views.getcategory)



]
from django.urls import path , register_converter
from .views import (

	 booksView , 
	 add_category ,
	 UpdateCategoryView ,
	 ListCategoryView ,
	 DeleteCategoryView,
	 CategoryDetailView,
   UpdateBookView,
   BookDetailView,
   deleteBookview,
   issuebooksview,
   search_historyview,




	 )

from . import views 




urlpatterns = [    

    #path('category/test/',testview.as_view(), name= "testview")
    #path('category/test/',views.test,name="testview"),
    #path('',views.books,name="books") ,
    #path('homepage/',PostListView.as_view(), name ="homepage"),
    #path('hardcopybooks/',views.hardcopybooks,name="hardcopybooks"),
  	path('',booksView.as_view() , name="books") ,
    path('addbooks/',views.addbooks,name="addbooks"),
    path('issuebook/<booksid>/',views.issuebook,name="issue-book"),
    path('get_issue_books/',views.getissuebook,name="get-issue-book"),

    path('get_reserve_book/',views.get_reserve_book,name="get-reserve-book"),
    
    path('update/<int:pk>',UpdateBookView.as_view(),name="Update-book"),
    path('delete/<int:pk>',deleteBookview.as_view(),name="delete-book"),
    path('bookdetail/<int:pk>/',BookDetailView.as_view(),name="book-detail"),
    path('issuebooks',issuebooksview.as_view(),name="issued-books-view"),
    path('userissuedbook/<userid>', views.UserIssuedBooks,name="user-issued-books"),

    path('returnbook/<issuebooksid>',views.returnbook,name="returnbook"),
    path('returnissuedbook/<issuebooksid>',views.returnissuedbook,name="return-issued-book"),
    path('reserve_book/<booksid>',views.reserve_book,name="reserve-book"),

    path('export_csv/',views.export_csv,name="export-csv"),
    path('export_pdf/',views.export_pdf,name="export-pdf"),


  	path('category/<int:pk>/',CategoryDetailView.as_view(), name ="category-detail"),
  	path('addcategory/',add_category.as_view(),name="addcategory"),
  	path('category/',ListCategoryView.as_view(),name ="Viewcategory"),
  	path('category/update/<int:pk>/',UpdateCategoryView.as_view(),name="UpdateCategory"),
  	path('category/delete/<int:pk>/',DeleteCategoryView.as_view(),name="DeleteCategory"),
    path('category/<categoryid>',views.viewCategory,name="viewCategory"),

  	

    path('searched_books/',views.searched_books,name="searched-books"),
    path('searched_user_issued_books/',views.searched_user_issued_books,name="searched-user-issued-books"),
    path('search_history/<userid>',search_historyview.as_view(),name='search-history'),
    
  	

  	



  	 
  
]


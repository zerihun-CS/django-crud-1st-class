
from django.urls import path
from .views import index,about,add_hobby
app_name = 'app1'
urlpatterns = [
    
    
    # *******************************************
   
    path('',index,name="index_url" ),
    path('add/', add_hobby, name='add_hobby_url')
    # *******************************************
    
]

from django.urls import path 
from . import views 
'''. ==> mean from the current dir we in'''

urlpatterns = [
    path('', views.posts_list),
    
]

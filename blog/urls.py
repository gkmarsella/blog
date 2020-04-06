from django.urls import path
from . import views
 
#When we go to blog first it looks through our admin urls.py, then here because we directed it

urlpatterns = [
     path('', views.home, name='blog-home'),
     path('about/', views.about, name='blog-about'),
]

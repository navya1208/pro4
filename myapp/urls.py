from myapp import views
from django.urls import path 
app_name="myapp"

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
]

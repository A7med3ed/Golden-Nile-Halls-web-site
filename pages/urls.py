from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home,name="home"),
    path('lotus/', lotus,name="lotus"),
    path('horus/', horus,name="horus"),
    path('goldn/', goldn, name="goldn"),
    path('book/', book, name="book"),
    path('gdn-admin/', dashboard, name="dashboard"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
    path('approve/<str:pk>/', approveReserv, name="approve"),
    path('delete/<str:pk>/', delReserv, name="delete"),
]

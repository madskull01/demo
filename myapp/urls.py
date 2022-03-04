from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('insert/',views.MyTestClass.as_view(),name="insert"),
    path('show/',views.show,name="show"),
    path('delete_data/<int:id>',views.delete_data,name="delete_data"),
    path('update_data/<int:pk>',views.update_data,name="update_data"),
    path('viewplayer/<int:id>',views.viewplayer,name="viewplayer"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
]
from django.urls import path

from .views import *
urlpatterns=[
path('',home_view,name='home'),
path('register',registerview,name='register'),
path('login',login_view,name='login'),
path('create',create_view,name='create'),
path('logout_url',logout_view,name='logout_url'),
path('delete_d/<int:id>',delete_data,name='delete_d'),
path('<int:id>',update_view,name='update'),
]
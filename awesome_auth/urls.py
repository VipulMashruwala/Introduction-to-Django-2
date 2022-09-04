from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('check_credentials',views.check_credentials, name = 'check_credentials'),
    path('signup',views.signup, name = 'signup'),
    path('addData',views.addData, name = 'addData'),
    path('updateData',views.updateData, name = 'updateData'),
    path('deleteData',views.deleteData, name = 'deleteData'),
    path('addNewAdmin',views.addNewAdmin, name = 'addNewAdmin')
]
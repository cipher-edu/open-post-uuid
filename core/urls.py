from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add/',add, name="add"  ),
    path('delete/<uuid:id>', delete, name='post'),
    path('edit/<uuid:id>', edit, name='post'),
    path('edit/editrecord/<uuid:id>', editrecord, name='post')
]

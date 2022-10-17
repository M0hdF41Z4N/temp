from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'home'),
    path('<str:slug>',views.ViewPost,name = 'view'),
    path('search',views.SearchPost,name = 'search'),
    path('create',views.CreatePost,name = 'create')
]

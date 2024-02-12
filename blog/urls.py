from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_index, name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<category>/', views.post_category, name='post_category')
]

from django.urls import path

from . import views

app_name= 'feeds'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('new_post/', views.CreateNewPost.as_view(), name='new_post'),
]
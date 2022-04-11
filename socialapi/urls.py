from django.db import router
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

app_name ='socialapi'

urlpatterns = [
    path('', include(router.urls)),
    path('api-posts/', include('rest_framework.urls', namespace='rest_framework'))
]
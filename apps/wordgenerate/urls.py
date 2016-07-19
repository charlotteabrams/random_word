from django.conf.urls import url
from . import views
#VIEWS

urlpatterns = [
    url(r'^$', views.index),
    url(r'^word$', views.generate)
]
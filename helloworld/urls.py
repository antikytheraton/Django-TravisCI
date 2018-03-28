from django.conf.urls import url

from .views import HelloWorld

urlpatterns = [
    url(r'^$', HelloWorld.as_view()),
]
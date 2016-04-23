from django.conf.urls import url

from .views import base_view

urlpatterns = [
    url(r'^$', base_view)
]

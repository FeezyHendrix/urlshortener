from django.urls import path, re_path
from .views import UrlShortener, viewUrl, createUrl
urlpatterns = [
    path('',  UrlShortener.as_view(), name="index"),
    path('l/<slug:generated_link>', viewUrl, name="url-view" ),
    path('create_link',  createUrl.as_view(), name="create_url")
]

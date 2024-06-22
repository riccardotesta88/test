from django.contrib import admin
from django.urls import path,include

'''Url resolver principale'''

urlpatterns = [
    path("admin/", admin.site.urls),
      # API RESTFRamework
    path("api/",include('EndpointAPI.urls')),
    # API BASE Light
    path("apix/",include('EndpointAPI.urls1')),
]

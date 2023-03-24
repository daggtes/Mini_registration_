from django.contrib import admin
from django.urls import include, path
from .router import router
from registration import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
]

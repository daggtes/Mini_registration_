from django.contrib import admin
from django.urls import include, path
from .router import router




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('rest_framework.urls', namespace='rest_framework')),
    path('api', include(router.urls)),
]

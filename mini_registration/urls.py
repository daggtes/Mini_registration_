from django.contrib import admin
from django.urls import include, path
from .router import router
from registration import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
    path('Member/Post', views.MemberLevelViewSetPost),
    path('Member/Get', views.MemberLevelViewSetGet),
    path('Member/Create', views.MemberLevelViewSetCreate),
    path('Member/Update', views.MemberLevelViewSetUpdate),
    path('Member/Delete', views.MemberLevelViewSetDelete)
]

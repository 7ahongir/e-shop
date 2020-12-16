from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('geo/', include('geo.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('geo/', include('geo.urls')),
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

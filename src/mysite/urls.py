from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cart/', include('order_product.urls')),
	path('geo/', include('geo.urls')),
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
]

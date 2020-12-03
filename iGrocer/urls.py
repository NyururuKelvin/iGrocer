from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('istore.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
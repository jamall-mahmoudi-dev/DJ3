
from django.contrib import admin
from django.urls import include, path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("website.urls")),
    path('', include("blog.urls")),
    

]

#Bahram explaine
# --- اضافه کردن static و media فقط در زمان توسعه (DEBUG=True) --- مهم : 
if settings.DEBUG:
    # files static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # files media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
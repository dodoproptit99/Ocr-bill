from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.upload_image, name='home'),
    # path('image_upload/', views.upload_image, name = 'image_upload'),
    # path('image_display', views.display_images, name = 'image_display'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 

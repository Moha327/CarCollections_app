from django.urls import path
from . import views # the . indicates that the views file can be found in the same directory as this file
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path('', views.index),
 path('profile', views.index2),
 path('profile/create', views.createpage),
 path('profile/details', views.index5),
 path('car/add', views.index4),
 path('catalogue', views.success),
 path('profile/edit', views.updateprofile),
 path('profile/edit/<int:profileid>', views.index6),
 path('update/<int:profileid>', views.index7),
 path('delete', views.deleteprofile),  
 path('profile/delete', views.deleteprofile),  
 path('car2/create2', views.createcar),
 path('car/<int:carid>/details', views.index8),
 path('car/<int:carid>/edit', views.index9),
 path('car2/<int:carid>/edit2', views.updatecar),
 path('car/<int:carid>/delete', views.index10)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# myapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('connectgroup/', views.connectgroup, name='connectgroup'),
    path('event/', views.eventsingle, name='eventsingle'),
    path('events/', views.events, name='events'),
    path('style/', views.style, name='style'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('contact/', views.contact, name='contact'),
    path('image/', views.image, name='image'),

    # FIXED — correct function name
    path('Media/', views.Media, name='Media'),

    path('testimony_success/', views.testimony_success, name='testimony_success'),
    path('testimonies/', views.testimony_page, name='testimony_page'),

    path("nav/", views.nav, name="nav"),
    path("styles/", views.styles, name="styles"),

    # delete testimony
    path('delete/<int:id>/', views.delete_testimony, name='delete_testimony'),
]

# Serve media files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

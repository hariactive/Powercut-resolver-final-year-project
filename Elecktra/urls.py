
from django.contrib import admin
from django.urls import path
from electricity import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('login/',views.loginuser,name="login"),
    path('register/',views.registeruser,name="register"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('map/',views.map,name="map"),
    path('announcements/',views.annnouncements,name="announcements"),
    path('feedback/',views.feedback,name="feedback"),
    path('logout/',views.logoutuser,name="logout"),
    path('coordinates/',views.getmapcoordinates,name="coordinates"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

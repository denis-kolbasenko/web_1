"""
from django.contrib import admin
from django.urls import path
# Импортируем нашу функцию из приложения gallery
from gallery.views import home
#from gallery.views import about
urlpatterns = [
path('admin/', admin.site.urls),

# Пустая строка '' означает главную страницу сайта (http://localhost:8000/)
path('', home, name='home'),
#path('about/', about, name='about'),
]


from gallery.views import home, about  ### Самостоятельная добавьте about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),  # добавьте эту строку
]
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


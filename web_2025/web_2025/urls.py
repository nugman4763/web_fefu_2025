from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fefu_lab.urls')),  # Подключаем маршруты приложения
]

# Обработчик для 404 ошибок
handler404 = 'fefu_lab.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),  # <-- Убрали слово polls/ вот тут
    path('admin/', admin.site.urls),
]
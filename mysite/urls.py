from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Теперь админка будет открываться сразу на главной странице (127.0.0.1:8000/)
    path('', admin.site.urls),

    # А приложение с опросами будет доступно по адресу 127.0.0.1:8000/polls/
    path('polls/', include('polls.urls')),
]
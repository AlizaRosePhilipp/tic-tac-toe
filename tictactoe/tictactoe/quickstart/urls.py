from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tictactoe.urls')),  # Include tictactoe app URLs
]
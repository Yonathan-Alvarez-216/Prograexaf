from django.urls import path
from .views import wenos


urlpatterns = {
    path('', wenos, name='wenos'),
}

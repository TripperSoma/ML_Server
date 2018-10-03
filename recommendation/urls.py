from django.urls.conf import path
from django.http import HttpResponse

from .views import recommend_view


urlpatterns = [
    path('', recommend_view),
]
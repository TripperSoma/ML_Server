from django.urls.conf import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse('hello')),
]
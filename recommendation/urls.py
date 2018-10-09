from django.urls.conf import path
from django.http import HttpResponse

from .views import recommend_view
from . import views

urlpatterns = [
    path('<int:user_id>/', recommend_view, name='recommend_view'),
    path('',views.IndexView.as_view(),name='index'),
]
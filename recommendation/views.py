from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from .ml import main_project


@require_GET
@csrf_exempt
def recommend_view(user_id):
    return main_project(user_id)

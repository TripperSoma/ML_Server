from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from .ml import main_project
from .models import ReviewModel


@require_GET
@csrf_exempt
def recommend_view(request, user_id):
    # return main_project(user_id)
    # return {'result', list(ReviewModel.objects.values())}
    return {'result': [377, 203, 42, 154, 904, 1064, 1405]}


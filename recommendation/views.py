from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.views import View
from .ml import main_project
from .models import ReviewModel, RecommendModel


@require_GET
@csrf_exempt
def recommend_view(request, user_id):
    # return main_project(user_id)
    # return {'result', list(ReviewModel.objects.values())}
    query_set = RecommendModel.objects.filter(user_id=user_id).values()

    return {'result': list(query_set)}

class IndexView(View):
    def get(self,request):
        return HttpResponse('<h1>EB Django Project<h1>')
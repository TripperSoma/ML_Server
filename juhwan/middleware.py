import json

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, JsonResponse


class JsonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and request.body:
            content_type = request.META.get('content_type', '')
            if 'application/json' in content_type:
                request.JSON = json.loads(request.body)

    def process_response(self, request, response):
        if isinstance(response, str):
            if response[0] in ('[', '{',):
                return HttpResponse(response, content_type='application/json')
            return HttpResponse(response)
        elif isinstance(response, (list, tuple, dict,)):
            return JsonResponse(response)
        else:
            # Queryset, ... 처리 해주자
            return HttpResponse(response)

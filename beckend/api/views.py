import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    # reguest -> HttpRequest -> Django
    print(request.GET) #url query params
    print(request.POST)
    body = request.body #byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.POST)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)
from django.http import JsonResponse


def index(request):
    data = {"test": "test"}
    return JsonResponse(data)

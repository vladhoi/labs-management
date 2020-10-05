from django.http import JsonResponse


def index(request):
    data = {"test": "testing"}
    return JsonResponse(data)

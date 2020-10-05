from django.http import JsonResponse


def index(request):
    data = {"test": "just a test"}
    return JsonResponse(data)

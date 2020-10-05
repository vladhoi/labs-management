from django.http import JsonResponse


def index(request):
    data = {"test_ci": "testing"}
    return JsonResponse(data)

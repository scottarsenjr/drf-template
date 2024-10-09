from django.http import JsonResponse


def custom404(request, exception=None):
    return JsonResponse(
        {'error': 'Endpoint not found', 'detail': f'Endpoint not found for requested resource: {request.path}'},
        status=404,
    )

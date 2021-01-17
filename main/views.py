from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'sign-up': reverse('sign-up', request=request, format=format),
        'email-verify': reverse('email-verify', request=request, format=format),
        'profile': reverse('profile', request=request, format=format),
        'active-profiles-list': reverse('active-profiles-list', request=request, format=format),
        'login': reverse('login', request=request, format=format),

    })
    return response

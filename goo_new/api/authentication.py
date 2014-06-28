from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        if token != 'aqb7YPH5zRkpza3oLG2irwFRd6fArHVq':
            return None

        user = User.objects.get(username='dbadmin')
        return (user, None)

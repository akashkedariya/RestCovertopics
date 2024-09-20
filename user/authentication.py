# from rest_framework.authentication import BaseAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from django.contrib.auth.models import User

# class CustomAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         token = request.headers.get('X-Custom-Token')
#         if not token:
#             return None

#         try:
#             user = User.objects.get(auth_token=token)
#         except User.DoesNotExist:
#             raise AuthenticationFailed('No such user')

#         return (user, None)
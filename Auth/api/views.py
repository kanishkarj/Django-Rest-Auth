from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

@login_required
def return_token(request):
    token, _ = Token.objects.get_or_create(user=request.user)
    #return Response({"token": token.key})
    return JsonResponse(token.key, safe=False)

'''
class ExampleView(APIView):
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
# Create your views here.
'''
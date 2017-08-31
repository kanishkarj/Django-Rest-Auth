from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.generic import View
from django.contrib import auth
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView


class LogOut(View):
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        Token.objects.filter(user_id=request.user.id).delete()
        auth.logout(request)
        return JsonResponse({"token": request.user.id})

class LogIn(GenericAPIView):
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

@login_required
def return_token(request):
    token, _ = Token.objects.get_or_create(user=request.user)
    #return Response({"token": token.key})
    return JsonResponse(token.key, safe=False)
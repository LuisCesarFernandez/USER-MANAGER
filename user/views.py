from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from .serializer import *
from .models import *
import secrets

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])

        #generar un token único
        token_str = secrets.token_hex(16)

        token, created = Token.objects.get_or_create(id_user=user, defaults={'token': token_str})
        return Response({'token': token.token, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def user_id(request, id):
    try:
        user_instance = User.objects.get(id_user = id)
    except User.DoesNotExist:
        raise Http404('Usuario no existe')
    
    serializer = UserSerializer(user_instance)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def profile(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def profile_id(request, id):
    try:
        profile_instance = Profile.objects.get(id_profile = id)
    except Profile.DoesNotExist:
        raise Http404('Perfíl no existe')
    
    serializer = ProfileSerializer(profile_instance)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def login(request):
    return Response({'Hola como estan espero que bien'})

@api_view(['PUT'])
def profile(request):
    return Response({'Todo bien y actualizado'})
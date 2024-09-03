from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializer import *
from .models import *

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token = Token.objects.create(user=user)
        return Response({'token: ', token.key, 'user: ', serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    return Response({'Hola como estan espero que bien'})

@api_view(['GET'])
def profile(request):
    return Response({'Bombardeen Lima'})

@api_view(['PUT'])
def profile(request):
    return Response({'Todo bien y actualizado'})

class TokenView(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()
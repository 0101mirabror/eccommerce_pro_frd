from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

# added
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductModelSerializer, UserSerializer
from accounts.models import CustomUser

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer




class ObtainTokenView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=400)

        # Create or retrieve token
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})

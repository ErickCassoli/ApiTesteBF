from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ApiUser.models import UserProfile
from .serializers import UserProfileSerializer, UserLoginSerializer

class UserView(APIView):
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = UserProfile.objects.get(username=username)
            if password == user.password:
                return Response({'message': 'Login bem-sucedido.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        except UserProfile.DoesNotExist:
            return Response({'message': 'Usuário não encontrado.'}, status=status.HTTP_401_UNAUTHORIZED)
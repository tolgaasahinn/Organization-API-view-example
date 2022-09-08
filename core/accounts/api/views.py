from accounts.models import UserModel
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserListApiView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserModel.objects.all().order_by("id")
    serializer_class = UserSerializer


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


class UserProfileCreateApiView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerWithToken

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            user = UserModel.objects.create(
                first_name=data["username"],
                username=data["email"],
                email=data["email"],
                password=make_password(data["password"]),
            )
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            message = {"detail": "User already exists"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

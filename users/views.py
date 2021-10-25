from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
# from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
# from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username", None)
        email = serializer.validated_data.get("email", None)
        password = serializer.validated_data.get("password", None)
        User.objects._create_user(
            username=username, email=email, password=password)
        return Response(
            {
                'success': f"{username} your account has been created",
                'details': serializer.data
            }, status=201)


class SignInView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'])

        if not user:
            return Response({"error": "Invalid username or password"}, status="400")
        login(self.request, user)
        return Response(serializer.data, status=200)


class LogoutView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        try:
            logout(request)
            return Response({"success": "Logout success"})
        except:
            return Response({"error": "Something went wrong, Try again"})

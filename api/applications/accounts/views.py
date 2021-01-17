import jwt

from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.utils import jwt_payload_handler


from .serializers import (
    UserSerializer,
    VerifyEmailSerializer,
    ProfileSerializer,
    ProfilesListSerializer,
)

from .models import Profile
from .permissions import IsOwner

from main.settings import SECRET_KEY

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                response_data = user.send_activation_email(request.get_host())
                return Response((serializer.data, response_data), status=status.HTTP_201_CREATED)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmailVerificationView(APIView):
    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        if serializer.is_valid():
            decoded_jwt = jwt.decode(serializer.validated_data['key'], SECRET_KEY, algorithm='HS256')
            if 'id' in decoded_jwt:
                user = User.objects.filter(id=decoded_jwt['id']).first()
                if user:
                    user.is_active = True
                    user.save()
                    serializer = UserSerializer(instance=user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'key': 'given code is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=self.request.user.pk)
        profile_serializer = self.get_serializer(user.profile, context={'request': request})
        return Response(profile_serializer.data, status=status.HTTP_200_OK)


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.email = request.data.get('email', instance.user.email)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActiveProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfilesListSerializer

    def get_queryset(self):
        return Profile.objects.filter(user__is_active=True)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)
        if user:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            user_details = {'id': user.id, 'email': user.email, 'token': token}
            user_logged_in.send(sender=user.__class__,
                                request=request, user=user)
            return Response(user_details, status=status.HTTP_200_OK)
        else:
            response_data = {
                'error': 'Can not authenticate with the given credentials or the account has been deactivated'}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)



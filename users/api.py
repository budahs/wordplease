from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404, ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer, InsertUserSerializer, ListBlogSerializer


class UserAPI(GenericAPIView):
    permission_classes = [UserPermission]

    def get(self, request):
        users = User.objects.all()
        paginated_users = self.paginate_queryset(users)
        serializer = UserListSerializer(paginated_users, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = InsertUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            user_serializer = UserSerializer(new_user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):
    permission_classes = [UserPermission]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = InsertUserSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            user_serializer = UserSerializer(updated_user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListBlogs(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ListBlogSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username']
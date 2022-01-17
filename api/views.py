from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import TodoModel
from .permissions import IsSuperUser, IsOwnerOrReadOnly, IsSuperUserOrStaffReadOnly
from .serializers import TodoSerializer, UserSerializer


class GetTodoList(APIView):
    def get(self, request):
        todo = TodoModel.objects.all()
        serialized = TodoSerializer(todo, many=True)
        '''todo_lst = []
        for item in serialized.data:
            todo_lst.append(item['status'])'''
        return Response(serialized.data)


class TodoDetail(RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

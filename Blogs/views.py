from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .serilaizers import UserSerializer

from rest_framework.response import Response
from .models import UserModelBlog


class Registration(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Xabar': 'Siz ro`yxatdan o`tdingiz'})
        else:
            return Response(serializer.errors)


class LoginAPI(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = UserModelBlog.objects.all().filter(username=username, password=password)

        if user:
            return Response({'Xabar': "Siz akkauntga kirdizngiz"})
        else:
            return Response({'Xabar': "Bunday login mavjud emas"})


class AllUsers(APIView):
    def get(self, request):
        users = UserModelBlog.objects.all()  # [::3]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

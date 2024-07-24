from django.shortcuts import render
from rest_framework import status

# Create your views here.

from rest_framework.views import APIView
from .serilaizers import UserSerializer, DeleterSerializer

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
        users = UserModelBlog.objects.all()  # [:1:-1]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class DeleteUsers(APIView):
    serializer_class = DeleterSerializer

    def delete(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            deleted_count, _ = UserModelBlog.objects.filter(username=username).delete()
            if deleted_count:
                return Response({'Xabar': f'{username} bazadan o`chirildi'}, status=status.HTTP_200_OK)
            else:
                return Response({'Xabar': f'{username} bazada mavjud emas'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

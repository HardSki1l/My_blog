from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .serilaizers import UserSerializer

from rest_framework.response import Response
from .models import UserModelBlog


class Registration(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        # username = request.data.get('username')
        # password = request.data.get('password')
        # try:
        #     UserModelBlog.objects.create(username=username, password=password)
        #     return Response({'Xabar': 'Siz ro`yxatdan o`tdingiz'})
        # except:
        #     return Response({'Xabar': 'Tizimda qandaydir nosozlik tez orada to`g`rilaymiz'})

        # print(username,'\n',password)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Xabar': 'Siz ro`yxatdan o`tdingiz'})
        else:
            return Response(serializer.errors)

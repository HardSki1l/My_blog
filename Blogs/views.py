from django.shortcuts import render
from rest_framework import status

# Create your views here.

from rest_framework.views import APIView
from .serilaizers import *

from rest_framework.response import Response
from .models import UserModelBlog, TaskList


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


class UpdatePassword(APIView):
    def patch(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        user = UserModelBlog.objects.all().filter(username=username, password=password)
        if user:
            UserModelBlog.objects.all().filter(username=username, password=password).update(password=new_password)
            return Response({'Xabar': f'{username} userni paroli o`zgartrildi'})
        else:
            return Response({'Xabar': f'{username} bazada mavjud emas'}, status=status.HTTP_404_NOT_FOUND)


class SearchUserTask(APIView):
    def post(self, request):
        username = request.data.get('username')
        try:
            user = UserModelBlog.objects.get(username=username)
            tasks = TaskList.objects.filter(who=user)
            serializer = TaskListSerializer(tasks, many=True)

            serialized_data = list(serializer.data)

            for task in serialized_data:
                usernames = []
                for user_id in task['who']:
                    user = UserModelBlog.objects.get(id=user_id)
                    usernames.append(user.username)
                task['who'] = usernames

            return Response(serialized_data, status="200")
        except:
            return Response({"msg": "User Not Found"}, status="404")


class UpdateComment(APIView):
    serializer_class = CommentUpdateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            comment_id = serializer.validated_data['comment_id']
            new_comment = serializer.validated_data['comment']

            try:
                task = TaskList.objects.get(id=comment_id)
                task.comment = new_comment
                task.save()
                return Response({'Xabar': 'Comment muvaffaqiyatli yangilandi'}, status="400")
            except TaskList.DoesNotExist:
                return Response({'Xabar': 'Comment topilmadi'}, status="400")
        return Response(serializer.errors, status="400")

# class UserFinder(APIView):
#     serializer_class = TaskFinder
#
#     def post(self, request):
#         comment = request.data.get('comment')
#         filtr1 = TaskList.objects.all().filter(comment=comment)
#         connected_users = UserModelBlog.objects.filter(tasklist__in=filtr1).distinct()
#         print(connected_users)
#         users_list = []
#         for i in connected_users:
#             users_list.append(i.username)
#             print(i)
#         return Response({'Userlar': f"{users_list}"})

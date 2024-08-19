from django.urls import path
from .views import *

urlpatterns = [
    path('v1/user/register/', Registration.as_view()),
    path('v1/user/login/', LoginAPI.as_view()),
    path('v1/user/all/', AllUsers.as_view()),
    path('user/delete/', DeleteUsers.as_view()),
    path('v1/user/update_password/', UpdatePassword.as_view()),
    path('v1/searchtasks/', SearchUserTask.as_view()),
    path('v1/comment/update/', UpdateComment.as_view()),
    path('v1/users_update/', AdduserToTask.as_view()),
    path('v1/user/delete/', DeleteuserToTask.as_view()),
]

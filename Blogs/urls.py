from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Registration.as_view(), name='Registratsiya qilish uchun API'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('all_user/', AllUsers.as_view(), name='all_user'),
    path('delete/', DeleteUsers.as_view(), name='delete_user'),
    path('update_password/', UpdatePassword.as_view()),
    path('searchtasks/',SearchUserTask.as_view(),name='searchtasks'),
]

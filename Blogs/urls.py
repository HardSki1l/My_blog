from django.urls import path
from .views import Registration,LoginAPI,AllUsers

urlpatterns = [
    path('register/', Registration.as_view(), name='Registratsiya qilish uchun API'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('all_user/', AllUsers.as_view(), name='all_user'),
]

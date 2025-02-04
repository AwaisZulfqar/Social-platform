from django.urls import path
from .views import UserCreateView,LoginUserView

urlpatterns = [
    path("Registerusers/", UserCreateView.as_view(), name="user-create"),
    path("Loginusers/", LoginUserView.as_view(), name="user-login"),

]



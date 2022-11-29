from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('profile-setup/',views.profile,name="profile"),
    path("register/",views.register,name="register"),
    path("login/",views.loginPage,name="login"),
    path('logout/', LogoutView.as_view(next_page="/user/login/"), name='logout'),
]
urlpatterns += staticfiles_urlpatterns()

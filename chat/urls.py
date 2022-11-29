from django.urls import path
from . import views
urlpatterns = [
    path("",views.inbox,name="inbox"),
    path("chat/<str:id>/",views.chat,name="chat"),
    path('search/',views.searchUsers,name="search"),
    path('createRoom/',views.createRoom,name="createRoom"),
]

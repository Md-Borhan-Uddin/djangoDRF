from django.urls import path
from blog.views import (
    home, PostAPIView, 
    PostCreate, PostDelete, 
    PostList, PostUpdate, SinglePost, 
    ListAndCreate, UpdateDeleteRetrive
    )

urlpatterns = [
    path('',home),
    path('<int:id>/',home),
    path('classview/<int:id>/',PostAPIView.as_view()),
    path('classview/',PostAPIView.as_view()),

    path('gview/list/',PostList.as_view()),
    path('gview/create/',PostCreate.as_view()),
    path('gview/delete/<int:pk>/',PostDelete.as_view()),
    path('gview/update/<int:pk>/',PostUpdate.as_view()),
    path('gview/post/<int:pk>/',SinglePost.as_view()),


    path('gview/lc/',ListAndCreate.as_view()),
    path('gview/udr/<int:pk>/',UpdateDeleteRetrive.as_view()),
]
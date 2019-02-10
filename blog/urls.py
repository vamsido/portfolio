
from django.urls import path
import blog.views

urlpatterns = [
    path('',blog.views.allblogs,name="allblogs"),
    path('<int:blogId>/',blog.views.getBlog,name="getBlog"),
]

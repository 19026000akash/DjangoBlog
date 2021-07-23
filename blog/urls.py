from django.urls import path
from . import views
from .views import (
    Postlistview,
    Postdetailview,
    Postcreateview,
    Postupdateview,
    Postdeleteview,
)

urlpatterns = [
    path("", Postlistview.as_view(), name="blog-home"),
    path("post/<int:pk>/", Postdetailview.as_view(), name="post-detail"),
    path("post/new/", Postcreateview.as_view(), name="post-create"),
    path("post/<int:pk>/update", Postupdateview.as_view(), name="post-update"),
    path("post/<int:pk>/delete", Postdeleteview.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),
]

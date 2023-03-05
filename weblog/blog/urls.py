from django.urls import path
from . import views

urlpatterns = [
    path("post_list/", views.post_list, name="post_list"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.post_detail, name="post_detail"),
    path('', views.home, name='home'),
]

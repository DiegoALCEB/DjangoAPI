from django.urls import path
from . import views
urlpatterns = [
    path("articles", views.articles, name ="articles"),
    path("articles/<int:article_id>", views.article, name="article")
]
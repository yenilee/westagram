from django.urls import path

from .views import CommentView, CommentfilterView

urlpatterns = [
        path('', CommentView.as_view()),
        path('/list', CommentfilterView.as_view()),
]

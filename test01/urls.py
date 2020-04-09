from django.urls import include, path
    
urlpatterns = [
    path('user', include('user.urls')),
    path('comment', include('comment.urls')),
]

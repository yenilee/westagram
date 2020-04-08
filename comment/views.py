import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Comment

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
                user = data['user'],
                comment = data['comment']
        ).save()
        return HttpResponse(status=200)

    def get(self, request):
        comment = Comment.objects.values()
        return JsonResponse({'comment_list':list(comment)}, status=200)




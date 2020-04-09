import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Comment

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            Comment(
                  user = data['user'],
                  comment = data['comment']
            ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=401)
    def get(self, request):
        comment = Comment.objects.values()
        return JsonResponse({'comments':list(comment)}, status=200)

class CommentfilterView(View):
    def post(self, request):
        data = json.loads(request.body)
        comment_user = data.get('user', None)

        if Comment.objects.filter(user=comment_user):
            user_comment_list = Comment.objects.filter(user=comment_user).values('comment')
            return JsonResponse({'user_comment_list':list(user_comment_list)}, status=200)
        return JsonResponse({'message':"INVALID_KEY"}, status=400)




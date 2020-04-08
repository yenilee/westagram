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
        return JsonResponse({'comments':list(comment)}, status=200)

class CommentfilterView(View):
    def get(self, request):
        data = json.loads(request.body)
        comment_user = data.get('user', None)
        try:
            if Comment.objects.filter(user=comment_id):
               user_data = Comment.objects.filter(user=comment_id)
               user_data_length = len(user_data)
               my_list={}
               for num in range(user_data_length):
                   my_list[num] = user_data[num].comment
            return JsonResponse({'comment_list':my_list}, status=200)

        except TypeError:
            return JsonResponse({'message': 'INVALID_USER'}, status = 401)



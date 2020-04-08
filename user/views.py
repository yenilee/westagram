import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import User 


class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            new_user = data.get('user_id', None)

            if User.objects.filter(user_id=new_user):
                return JsonResponse({'message':'DUPLICATE_USER'}, status=401)
            User(
                 user_id  = new_user,
                 password = data['password']
            ).save()
            return HttpResponse(status=200)
        except TypeError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)

class UserView(View):
    def get(self, request):
        user = User.objects.values()
        return JsonResponse({'user_info':list(user)}, status=200)

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        login_id = data.get('user_id', None)
        login_password = data.get('password', None)

        try:
            if User.objects.filter(user_id=login_id):
                user=User.objects.get(user_id=login_id)
                if User.objects.filter(password=login_password):
                    return JsonResponse({'message':'LOGIN_SUCCESS'}, status=200)
                return JsonResponse({'message':'INVALID_PASSWORD'}, status = 401)
            return JsonResponse({'message': 'INVALID_USER'}, status = 401)
        except TypeError:
            return JsonResponse({'message': 'INVALID_KEY'}, status = 401)


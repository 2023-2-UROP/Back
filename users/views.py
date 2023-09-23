from django.shortcuts import render
import json, re, traceback, bcrypt, jwt, my_settings
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Account
# Create your views here.

minimum_password_length = 8


def valid_email(email):
    pattern = re.compile('^.+@+.+\.+.+$')
    if not pattern.match(email):
        return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)
def valid_password(password):
    if len(password) < minimum_password_length:
        return JsonResponse({'message':'SHORT_PASSWORD'}, status=400)

def vaild_phone(phone):
    pattern = re.compile('^[0]\d{9, 10}$')
    if not pattern.match(phone):
        return JsonResponse({'message':'USER_ALREADY_EXISTS'}, status=409)

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            email = data.get('email',None)
            password = data.get('password', None)
            name = data.get('name', None)
            nickname = data.get('nickname', None)
            phone = data.get('phone', None)

            if not (password and email and name and phone and nickname):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            valid_email(email)
            valid_password(password)

            user = Account.objects.filter(Q(email=email) | Q(name=name) | Q(phone=phone))
            if not user:
                Account.objects.create(
                    email=email,
                    name=name,
                    phone=phone,
                    nickname=nickname,
                    password= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                )
                return JsonResponse({'message': 'SUCCESS'}, status=200)

            return JsonResponse({'message': 'USER_ALREADY_EXISTS'}, status=409)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email = data.get('email')
            phone = data.get('phone')
            password = data.get('password')

            if Account.objects.filter(Q(email=email) | Q(phone=phone)).exists():
                account = Account.objects.get(Q(email=email) | Q(phone=phone))
                if bcrypt.checkpw(password.encode('utf-8'), account.password.encode('utf-8')):
                    token = jwt.encode({'email' : email}, my_settings.SECRET['secret'], algorithm='HS256')
                    return JsonResponse({'message' : 'SUCCESS'}, status=200)
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)
            return JsonResponse({"message": "INVALID_USER"}, status=401)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
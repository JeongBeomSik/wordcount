from django.shortcuts import render
from .models import Login
# Create your views here.

def login (request) :
    text='login'
    context={'text':text}
    return render(request, "login/test.html",context)

def check (request) :
    user_id = request.GET.get('uid')
    user_pwd = request.GET.get('pwd')
    print(user_id)
    print(user_pwd)
    user_infos = Login.objects.all()
    for user_info in user_infos :
        if(user_info.id == user_id and user_info.PassWord == user_pwd):
            text = "로그인 성공"
            break
        else :
            text = "로그인 실패"
        
    context={'text':text}
    return render(request, "login/check.html",context)
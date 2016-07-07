#-*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from bbs.forms import RegistForm,LoginForm
from bbs.models import MyUser

def md5(value):
    """
    md5加密函数
    """
    import hashlib
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()

def check_login(main):
    """
    控制是否需要登陆权限的装饰器
    """
    def check(request,*args,**kwargs):
        if request.session.get('user'):
            return main(request,*args,**kwargs)
        else:
            return redirect('/bbs/login/')
    return check

def Index(request):
    name = request.session.get('user')
    if name:
        return render_to_response(
            'bbs/index.html',
            {'name':name}
        )
    else:
        return render_to_response(
            'bbs/index.html'
        )

def Regist(request):
    """
    注册视图
    """
    #判断请求方式
    if request.method == 'POST':
        form = RegistForm(request.POST)
        #检查表单提交的数据是否合法
        if form.is_valid():
            #取出表单提交过来的数据
            name = form.cleaned_data['username']
            mail = form.cleaned_data['email']
            pwd1 = form.cleaned_data['password1']
            pwd2 = form.cleaned_data['password2']
            #数据库查询
            result_uname = MyUser.objects.filter(username = name).count()
            result_email = MyUser.objects.filter(email = mail).count()
            #检查邮箱、用户名是否已存在
            if result_email == 1:
                return render_to_response(
                    'bbs/regist.html',
                    {'form':form, 'error_msgs':'该邮箱已注册'}
                )
            else:
                if result_uname == 1:
                    return render_to_response(
                        'bbs/regist.html',
                        {'form':form, 'error_msgs':'该用户名已注册'}
                    )
                else:
                    #检查两次输入的密码是否一样
                    if pwd1 != pwd2:
                        return render_to_response(
                            'bbs/regist.html',
                            {'form':form, 'error_msgs':'两次输入的密码不一致'}
                        )
                    else:
                        MyUser.objects.create(
                            username = name,
                            email = mail,
                            password = md5(pwd1)
                        )
                        return render_to_response(
                            'bbs/registsuccess.html',
                            {'username':name}
                        )
    else:
        form = RegistForm()
    return render_to_response('bbs/regist.html',{'form':form})

def Login(request):
    """
    登录视图
    """
    #判断请求方式
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #检查表单提交的数据是否合法
        if form.is_valid():
            #取出表单提交过来的数据
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            pwd = md5(password)
            result = MyUser.objects.filter(email = email, password = pwd).count()
            #检查用户名密码是否正确
            if result == 1:
                user = MyUser.objects.get(email=email)
                request.session['user'] = user.username
                return redirect('/bbs/index/')
            else:
                return render_to_response(
                    'bbs/login.html',
                    {'form':form,'error_msgs':'用户名或密码错误'}
                )
    else:
        form = LoginForm()
    return render_to_response(
        'bbs/login.html',
        {'form':form}
    )

@check_login
def Logout(request):
    del request.session['user']
    return redirect('/bbs/index/')

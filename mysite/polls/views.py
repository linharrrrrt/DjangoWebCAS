from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
# Create your views here.
from django.template import loader
from .models import Question,Choice,User,QiangDaItem
from . import forms

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):     
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()       
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def logindex(request):
    
    return render(request, 'login/login.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/polls/qiangda/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = User.objects.get(username=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                request.session['group_name'] = user.groupname
                qiangda_form = forms.QaingdaForm(request.POST)
                qiangda_form.username = request.session['user_name'] 
                qiangda_form.groupname = request.session['group_name']
                return render(request, 'login/qiangda.html', locals())
                
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect('/polls/qiangda/')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            groupname = register_form.cleaned_data.get('groupname')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                new_user = User()
                new_user.username = username
                new_user.groupname = groupname
                new_user.password = password1
                new_user.save()
                message = '注册成功，请登录！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    request.session['is_login'] = False
    request.session['user_id'] = ""
    request.session['user_name'] = "user.username"
    return redirect("/polls/index/")

def qiangda(request):
    if request.session.get('is_login', None):
        pass
    else:
        return render(request, 'login/login.html', locals())
    if request.method == 'POST':
        qiangda_form = forms.QaingdaForm(request.POST)
        if qiangda_form.is_valid():
            username = qiangda_form.cleaned_data.get('username')
            groupname = qiangda_form.cleaned_data.get('groupname')
            qiangdaitem = QiangDaItem()
            qiangdaitem.groupname = groupname
            qiangdaitem.username = username
            qiangdaitem.username = username
            qiangdaitem.save()
        qiangdaitemadmin = QiangDaItem.objects.filter(username = "admin").order_by('-pub_date')[0]
        qiangda_form = forms.QaingdaForm(request.POST)
        qiangda_form.username = request.session['user_name'] 
        qiangda_form.groupname = request.session['group_name']
        
        # qiangdalist = QiangDaItem.objects.order_by('-pub_date')[:30]
        qiangdalist = QiangDaItem.objects.filter(pub_date__gt=qiangdaitemadmin.pub_date).order_by('pub_date')
        return render(request, 'login/qiangda.html', locals())
    else:
        qiangda_form = forms.QaingdaForm(request.POST)
        qiangda_form.username = request.session['user_name'] 
        qiangda_form.groupname = request.session['group_name']
        qiangdaitemadmin = QiangDaItem.objects.filter(username = "admin").order_by('-pub_date')[0]
        qiangdalist = QiangDaItem.objects.filter(pub_date__gt=qiangdaitemadmin.pub_date).order_by('pub_date')
        # qiangdalist = QiangDaItem.objects.order_by('-pub_date')[:30]

        return render(request, 'login/qiangda.html', locals())

from django.shortcuts import render, redirect
from .models import UsersAccount
from submission.models import StudentEssay
from .forms import LoginForm, RegisterForm, AddEssayform


def login(request):
    if request.session.get('email'):
        return redirect('dashboard')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email1 = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password')

        u = UsersAccount.objects.filter(email=email1, password=password1)

        if u:
            request.session['email'] = email1
            return redirect('dashboard')
        else:
            print('not match')

    context = {
        'form': form
    }
    return render(request, 'student/login.html', context)


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'student/home.html', context)


def dashboard(request):
    if not request.session.get('email'):
        return redirect('login', )
    se_email = request.session.get('email')

    login_user = UsersAccount.objects.get(email=se_email)

    form = AddEssayform(request.POST or None, request.FILES or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        body = form.cleaned_data.get('body')

        p = StudentEssay(user=login_user, title=title, body=body)
        p.save()

    context = {
        'form': form,
        'login_user': login_user,

    }
    return render(request, 'student/dashboard.html', context)


def logout_views(request):
    del request.session['email']
    return redirect('login')

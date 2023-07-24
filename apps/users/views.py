from django.shortcuts import render, redirect
from apps.users.forms import LoginForm, CadatroForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            usermail = form['user_login'].value()
            user_password = form['user_password'].value()
            
            user = auth.authenticate(
                request,
                username= usermail,
                password= user_password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Usuário logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login!')
                return redirect('login')

    return render(request, 'users/login.html', {'form': form})

def cadastro(request):
    form = CadatroForm()

    if request.method == 'POST':
        form = CadatroForm(request.POST)

        if form.is_valid():
            
            name = form['user_name'].value()
            e_mail = form['user_email'].value()
            password = form['user_password'].value()

            if User.objects.filter(email=e_mail).exists():
                messages.error(request, 'Usuário já existe!')
                return redirect('cadastro')
            
            user = User.objects.create_user(
                username=name,
                password=password,
                email=e_mail
            )
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

    return render(request, 'users/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
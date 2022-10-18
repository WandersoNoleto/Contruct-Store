from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator

from users.models import Users


@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == "GET":
        return render(request, 'users/register_seller.html')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar Messages do Django
            return HttpResponse("Email já existe")

        user = Users.objects.create_user(username=email, email=email, password=password, position="V")

        #TODO: Redirecionar com uma mensagem
        return HttpResponse('Conta criada')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'users/login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido')

        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

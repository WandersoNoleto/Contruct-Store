from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator

from users.models import Users


@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == "GET":
        sellers = Users.objects.filter(position="V")

        context = {
            'seller': sellers,
        }

        return render(request, 'users/register_seller.html', context)


    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last-name')
        email     = request.POST.get('email')
        password  = request.POST.get('password')

        user = Users.objects.filter(email = email)

        if user.exists():
            # TODO: Utilizar Messages do Django
            return HttpResponse("Email já existe")

        user = Users.objects.create_user(
            first_name = name, 
            last_name = last_name, 
            username  = email, 
            email     = email, 
            password  = password, 
            position  = "V"
            )

        #TODO: Redirecionar com uma mensagem
        return HttpResponse('Conta criada')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))

        return render(request, 'users/login.html')
    
    elif request.method == "POST":
        email    = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(
            username = email, 
            password = password
            )

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido')

        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')

def logout(request):
    request.session.flush()

    return redirect(reverse('login'))

@has_permission_decorator('excluir_vendedor')
def remove_user(request, id):
    seller = get_object_or_404(Users, id=id)
    seller.delete()
    
    messages.add_message(request, messages.SUCCESS, 'Vendedor excluído com sucesso')

    return redirect(reverse('cadastrar_vendedor'))

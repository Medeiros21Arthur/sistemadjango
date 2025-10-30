from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
#BIBLIOTECA DE AUTOMENSAGENS
from django.contrib.messages import constants
from django.contrib import messages
#BIBLIOTECA DE AUTETICACAO 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
#IMPORTACAO DA MODEL
from .models import motoristas
#TONAR PAGINA PRIVADA

def cadastro(request):

    if request.method =='GET':     
        return render(request, 'cadastro.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha=  request.POST.get('confirmar_senha')
        if senha != confirmar_senha:
            messages.add_message(request,constants.ERROR,'Senha e Confirma senha não conferem')
            return redirect ('cadastro')
        User.objects.create_user( 
            username= username,
            password= senha,
        )
        return redirect('login')
    

    #FUNCAO DE LOGIN
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username,  password=senha)

        if user:
            auth_login(request, user)
            return redirect('motor')
        
        messages.add_message(request, constants.ERROR, 'Username ou senha inválidos.')
        return redirect('login')

def motor(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            listamotorista = motoristas.objects.all()
            return render(request, 'motor.html', {'motoristas': listamotorista})
        elif request.method == "POST":
            foto = request.FILES.get('foto')
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')

            motorista = motoristas(
            foto=foto,
            nome=nome,
            idade=idade,
        )

        motorista.save()

        return redirect('motor')
    else:
        return redirect('login') 

def sair(request):
     return render(request,'login')  # redireciona para a página de login

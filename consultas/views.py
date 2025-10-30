from django.shortcuts import render, get_object_or_404, redirect
from usuarios.models import motoristas
from .models import Gravacoes

def consultas(request, id):
    motorista = get_object_or_404(motoristas, id=id)

    if request.method == 'POST':
        gravacao_arquivo = request.FILES.get('gravacao')
        data = request.POST.get('data')
        transcript = request.POST.get('transcript') == 'on'

        Gravacoes.objects.create(
            motoristas=motorista,
            video=gravacao_arquivo,
            data=data,
            transcrever=transcript,
        )

    # buscar todas as gravações desse motorista
     
    gravacoes = Gravacoes.objects.filter(motoristas=motorista)
    return render(request, 'consultas.html', {
        'motorista': motorista,
        'gravacoes': gravacoes
    })
     
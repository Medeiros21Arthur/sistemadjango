from django.shortcuts import render, get_object_or_404, redirect
from usuarios.models import motoristas
from .models import Gravacoes

def consultas(request, id):
    motorista = get_object_or_404(motoristas, id=id)
    if request.method == 'GET':
        return render(request, 'consultas.html', {'motorista': motorista})
    elif request.method == 'POST':
        gravacao = request.FILES.get('gravacao')
        data = request.POST.get('data')
        transcript = request.POST.get('transcript') == 'on'

        gravacao = Gravacoes(
            video=gravacao,
            data=data,  
            transcrever=transcript,
            motoristas=motorista,
        )

        gravacao.save()

        return redirect('motor',)
    
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from usuarios.models import motoristas
from .models import Gravacoes

def consultas(request, id):
    paciente = get_object_or_404(motoristas, id=id)
    if request.method == 'GET':
        return render(request, 'consultas.html', {'motorista': motoristas})
    elif request.method == 'POST':
        gravacao = request.FILES.get('gravacao')
        data = request.POST.get('data')
        transcript = request.POST.get('transcript') == 'on'

        gravacao = Gravacoes(
            video=gravacao,
            data=data,  
            transcrever=transcript,
            paciente=paciente,
        )

        gravacao.save()

        return redirect(reverse('consultas', kwargs={'id': id}))
    
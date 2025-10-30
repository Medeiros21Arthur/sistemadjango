from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Redireciona automaticamente para login se o usuário não estiver autenticado
    e tentar acessar uma página privada.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs que não precisam de login
        public_urls = [
            reverse('login'),
            reverse('cadastro'),
            '/admin/',  # se você usa admin
        ]

        # Se a URL não estiver na lista pública e o usuário não estiver logado
        if not request.user.is_authenticated and not any(request.path.startswith(url) for url in public_urls):
            return redirect('login')

        response = self.get_response(request)
        return response

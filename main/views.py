from django.shortcuts import render, get_object_or_404
from .models import Projeto

def home(request):
    projetos = Projeto.objects.all()
    return render(request, "main/home.html", {"projetos": projetos})

def projeto_detalhe(request, slug):
    projeto = get_object_or_404(Projeto, slug=slug)
    return render(request, "main/project_detail.html", {"projeto": projeto})
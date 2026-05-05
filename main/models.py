from django.db import models
from django.utils.text import slugify


class Projeto(models.Model):
    titulo = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    resumo = models.CharField(max_length=200)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    imagem = models.ImageField(upload_to="projetos/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

# Create your models here.

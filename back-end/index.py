from django.contrib import admin
from django.db import models
from django.shortcuts import render
from django.urls import path


# Models
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


# Admin configuration
admin.site.register(Article)


# URLs configuration
from . import views

urlpatterns = [
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),
]


# Views
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)


# Template: news/year_archive.html
"""
{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}
"""


# Base template: base.html
"""
{% load static %}
<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <img src="{% static 'images/sitelogo.png' %}" alt="Logo">
    {% block content %}{% endblock %}
</body>
</html>
"""


from pysus.online_data.SIM import download
import pandas as pd

# 1. Definir os parâmetros de busca
# Exemplo: Estado de São Paulo (SP), ano de 2022
estado = 'SP'
ano = 2022

print(f"Iniciando o download dos dados de mortalidade ({estado} - {ano})...")

# 2. Baixar os dados (o PySUS busca direto do FTP e converte para DataFrame)
# Nota: O retorno padrão do PySUS é um objeto que pode ser convertido em DataFrame
dados_brutos = download(estado, ano)
df = pd.DataFrame(dados_brutos)

# 3. Visualizar as primeiras linhas do seu projeto
print("\nDados carregados com sucesso!")
print(df.head())

# 4. Salvar em formato CSV para usar depois
df.to_csv(f"mortalidade_{estado}_{ano}.csv", index=False)
print(f"\nArquivo salvo como: mortalidade_{estado}_{ano}.csv")

from pysus.preprocessing.decoders import decodificar_idade

# Exemplo: O SUS codifica a idade de forma complexa (ex: 420 significa 20 anos). 
# Essa função limpa e padroniza a idade em anos no seu DataFrame:
df['idade_anos'] = decodificar_idade(df['IDADE'])


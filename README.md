# FacilitaSaúde - Programe com Propósito

Este projeto é uma aplicação web desenvolvida com Django para oferecer uma experiência mais organizada e acolhedora ao usuário, com páginas de login, perfil, rotina, consultas, dúvidas e informações de saúde.

## Estrutura das pastas

- **back_end/**  
  Contém a aplicação principal do Django. Aqui ficam os modelos, formulários, views, URLs, templates e a lógica de negócio relacionada ao cadastro de usuários, glossário, perfil e páginas internas.

- **config/**  
  Armazena a configuração do projeto Django, incluindo as definições do settings, URLs globais e a configuração de execução da aplicação.

- **CSS/**  
  Pasta com os arquivos de estilo do site, responsáveis por definir a aparência visual das páginas HTML.

- **DataBase/**  
  Guarda arquivos relacionados ao banco de dados ou cópias de dados locais do projeto.

- **HTML/**  
  Contém os arquivos HTML das páginas do sistema, como login, perfil, rotina, atendimento, serviços e outras telas públicas/privadas.

- **Imagens/**  
  Armazena imagens e recursos visuais usados no projeto, como logos, ícones ou fotos.

- **JavaScript/**  
  Pasta para scripts front-end, comportamentos interativos e funcionalidades do lado do cliente.

- **python_modules/**  
  Contém módulos Python com lógica auxiliar do projeto, como gráficos, consultas médicas e gerenciamento da rotina do usuário.

## Arquivos principais

- **manage.py**  
  Arquivo responsável por iniciar e gerenciar o projeto Django.

- **db.sqlite3**  
  Banco de dados SQLite usado pela aplicação localmente.

## Como executar o projeto

1. Entre na pasta do projeto.
2. Ative o ambiente virtual, se houver.
3. Execute:

```bash
python manage.py runserver
```

4. Acesse no navegador:

```text
http://127.0.0.1:8000/
```

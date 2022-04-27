# Website para trabalhos freelance desenvolvido com o framework Django 

## ![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![image](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white) ![image](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)

## Baseado na PSW3.0 do Pythonando / Ainda em desenvolvimento / Work in progress

### Objetivos
Página voltada para cadastro de trabalhos freelance onde os usuários podem solicitar trabalhos ou se oferecerem para trabalhar.

### Conceitos aplicados
* Criação e autenticação de usuários
* ORM (Manipulação de banco de dados)
* Navegação fluída entre as páginas
* Estilização com CSS
* Boas práticas de programação Python e Django
  + Encapsulamento de apps
  + Abstração

### Configurações iniciais para executar o projeto
* Escolher um diretório para colocar os arquivos
* Criar um ambiente virtual Python
* Dentro do ambiente virtual:
  + Instalar as bibliotecas Django e Pillow

  > pip install django pillow

  + Executar os comandos para configurar o Banco de Dados e rodar o servidor

  > python manage.py makemigrations  
  > python manage.py migrate  
  > python manage.py runserver
  
* Com o servidor em execução aceder a porta http://127.0.0.1:8000/auth/login

As informações serão armazenadas em um banco de dados local (SQLite).

Pronto! Basta navegar e testar as funcionalidades.


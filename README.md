# pesquisa_QA
Repositório com testes da pagina de pesquisa QA

# Steps para Executar

# Linux(Ubuntu)

Executar os comandos abaixo no terminal:

pip install virtualenv
virtualenv env
source ./env/bin/activate
sudo pip install -r requirements.txt

# Executar os testes

behave -f 'behave_html_formatter:HTMLFormatter' -o 'cucumber.html'
ao executar os testes o arquivo cucumber.html será gerado com o resultado dos testes



# Executar os Testes via pipeline

pip3.8 install -r requirements.txt --user && /usr/bin/python3.8 main.py"


# Adicionar cucumber reports a pipeline

cucumber fileIncludePattern: 'reports/cucumber*.json'

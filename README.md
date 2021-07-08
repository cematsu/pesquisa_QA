# Pesquisa_QA
Repositório com testes da pagina de pesquisa QA

# Steps para Executar
# Windows

Executar os comandos abaixo no terminal:

Clonar o repositório:
```sh
git clone https://github.com/cematsu/pesquisa_QA.git
cd pesquisa_QA
```
Instalar o python
```sh
python
```
```sh
pip install -r requirements.txt
```

# Linux(Ubuntu)

Executar os comandos abaixo no terminal:

Clonar o repositório:
```sh
git clone https://github.com/cematsu/pesquisa_QA.git
cd pesquisa_QA
pip install virtualenv
virtualenv env
source ./env/bin/activate
sudo pip install -r requirements.txt
```

# Executar os testes
```sh
cd pesquisa_QA
python main.py
```
ao executar os testes o arquivo cucumber.html será gerado com o resultado dos testes na pasta /reports



# Executar os Testes via pipeline

pip3.8 install -r requirements.txt --user && /usr/bin/python3.8 main.py"


# Adicionar cucumber reports a pipeline
Para gerar o relatório no formato cucumber reports, habilitar a linha de comando abaixo no arquivo main.py
```sh
# code = behave_main(["features/", "-t~@ignore", '-k', '-o', 'reports/cucumber-behave.html', '-f', 'json'])
```
cucumber fileIncludePattern: 'reports/cucumber*.json'

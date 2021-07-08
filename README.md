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
Obs. No windows o usuário deverá permitir a execução do Python
Obs2. em caso de erro na execução informar a versão do python na execução:
```sh
python3.9 main.py
```

# Report de execução dos Testes
Ao executar os testes 2 reports são gerados na pasta /reports (json e html). O arquivo .json está no formato cucumber para ser utilizado ao adicionar os testes a pipeline (cucumber-reports)


# Executar os Testes via pipeline

pip3.8 install -r requirements.txt --user && /usr/bin/python3.8 main.py"


# Adicionar cucumber reports a pipeline

cucumber fileIncludePattern: 'reports/cucumber*.json'

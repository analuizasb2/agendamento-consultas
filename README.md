# Agendamento de Consultas

## Descrição
API para a persistência de agendamentos de consultas médicas.
Permite as seguintes operações:
- Listar agendamentos
- Gerar um novo agendamento
- Deletar um agendamento
- Atualizar um agendamento

## Execução com Docker

### Requisitos

1. Ter o [Docker](https://docs.docker.com/engine/install/) instalado

### Execução
1. A partir da pasta raiz em um terminal como administrador, executar o comando abaixo para criar a imagem do Docker:

   `docker build -t agendamento-consultas .`
2. No mesmo terminal, executar o comando abaixo para executar o container:

   `docker run -p 3000:3000 agendamento-consultas`

## Execução sem Docker

### Requisitos

1. Ter o Python 3 instalado na máquina
2. Executar o comando abaixo para instalar as dependências:

   `pip install -r requirements.txt`

3. Executar o comando abaixo para inicializar o banco de dados:

   `python init_db.py`

### Execução

Para executar a API, execute o comando abaixo a partir desta pasta:

`python -m flask run --port 3000`


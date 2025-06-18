# Python API

API REST para gerenciamento de tarefas (Tasks) construída com [FastAPI](https://fastapi.tiangolo.com/), [Beanie ODM](https://roman-right.github.io/beanie/) e MongoDB.

## Funcionalidades

- Criar, listar, buscar, atualizar e deletar tarefas.
- Persistência de dados em MongoDB usando Beanie ODM.

## Requisitos

- Python 3.10+
- MongoDB em execução (local ou remoto)

## Instalação

1. Clone o repositório:
   ```sh
   git clone <url-do-repo>
   cd Python-API
   ```

2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure a variável de ambiente `MONGO_URI` com a string de conexão do seu MongoDB:
   ```sh
   export MONGO_URI="mongodb://localhost:27017"
   ```

## Execução

Inicie a API com o comando:
```sh
./start.sh
```
A aplicação estará disponível em [http://localhost:10000](http://localhost:10000).

## Endpoints

### Criar uma task

`POST /tasks`

```json
{
  "title": "Estudar FastAPI",
  "content": "Ler a documentação oficial e fazer um CRUD"
}
```

### Listar todas as tasks

`GET /tasks`

### Buscar uma task por ID

`GET /tasks/{task_id}`

### Atualizar uma task

`PUT /tasks/{task_id}`

```json
{
  "title": "Novo título",
  "content": "Novo conteúdo"
}
```

### Deletar uma task

`DELETE /tasks/{task_id}`

## Exemplos de requisições

Veja exemplos prontos no arquivo [`requests.http`](requests.http).

## Estrutura do Projeto

- [`main.py`](main.py): Arquivo principal da aplicação e definição das rotas.
- [`models.py`](models.py): Definição do modelo de dados `Task`.
- [`requirements.txt`](requirements.txt): Dependências do projeto.
- [`start.sh`](start.sh): Script para iniciar o servidor FastAPI.


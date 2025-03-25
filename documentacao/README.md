# IS-MultiTech_WebServer

Este projeto implementa um sistema **cliente-servidor** que integra **SOAP, REST, GraphQL e gRPC** para a gestão de tarefas (**Task Manager**).

## 📌 Requisitos

Antes de começar, certifica-te de que tens instalados:

- **Ubuntu**
- **Python** (`python --version`)
- **Pip** (`pip --version`)

## 📂 Estrutura do Projeto

```
/servidor
    /services
        soap.py
        rest.py
        graphql.py
        grpc.py
    tasks.json
    config.py
    server.py
/cliente
    client.py
/documentacao
    README.md
.gitignore
requirements.txt
```

## ⚙️ Instalação

As dependências devem ser instaladas **tanto no servidor como no cliente**. Para isso, executa:

```sh
pip install -r requirements.txt
```

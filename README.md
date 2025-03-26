# IS-MultiTech_WebServer

Este projeto implementa um sistema **cliente-servidor** que integra **SOAP, REST, GraphQL e gRPC** para a gestão de tarefas (**Task Manager**).

## 📌 Requisitos

Antes de começar, certifica-te de que tens instalados:

- **Ubuntu**
- **Python** (`python --version`)
- **Pip** (`pip --version`)

## 📂 Estrutura do Projeto

```
/cliente
    /requests
        graphql_client.py
        grpc_client.py
        rest_client.py
        grpc_client.py
    client.py
/documentacao
/servidor
    /services
        graphql_service.py
        grpc_client.py
        rest_client.py
        soap_service.py
    config.py
    server.py
    tasks.json
.gitignore
README.md
requirements.txt
```

## ⚙️ Instalação

As dependências devem ser instaladas **tanto no servidor como no cliente**. Para isso, executa:

1. **Clonar o repositório**  
   Primeiro, clona o repositório para a tua máquina:

   ```sh
   git clone <URL_DO_REPOSITORIO>
   ```

2. **Instalar as dependências**  
   Depois de clonar o repositório, navega até à pasta do projeto e instala as dependências com:

   ```sh
   cd <nome-do-repositorio>
   pip install -r requirements.txt
   ```

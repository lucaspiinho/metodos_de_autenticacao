# Projeto Flask de Autenticação

Este projeto é uma API simples em Flask que implementa autenticação e autorização básica usando HTTP Basic Auth.

## Funcionalidades

- Controle de acesso por perfis de usuários (`admin` e `usuario`)
- Rotas protegidas e públicas
- Mensagens de erro claras para autenticação e autorização

## Como usar

### Requisitos

- Python 3.7+
- Virtualenv (recomendado)

### Setup

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio

2. Crie e ative o ambiente virtual:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4. Rode o servidor Flask:
    ```bash
    python app.py

## Endpoints
    
    /dados - acesso restrito a usuários com perfil admin

    /publico - acesso para usuários com perfil admin ou usuario

## Testando a autenticação

    Use um cliente HTTP como `curl`, `Postman` ou `Insomnia`.
    
    Exemplo com Postman:

        Abra o Postman e crie uma nova requisição do tipo GET.

        No campo URL, digite: http://127.0.0.1:5000/dados

        Vá para a aba Authorization.

        No tipo (Type), selecione Basic Auth.

        Preencha:

        Username: joao

        Password: 123

        Clique em Send para enviar a requisição.

        Você deve receber a resposta JSON com a mensagem de boas-vindas para o admin.

        Para testar a rota pública /publico, troque a URL e o usuário para:

        URL: http://127.0.0.1:5000/publico

        Username: maria

        Password: abc

---
Desenvolvido por Lucas Pinho


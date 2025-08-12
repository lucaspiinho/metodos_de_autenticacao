from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Dados de usuários
usuarios = {
    "joao": {"senha": "123", "perfil": "admin"},
    "maria": {"senha": "abc", "perfil": "usuario"}
}

# Autenticação e autorização
def checar_autenticacao(perfis_permitidos):
    def decorator(func):
        @wraps(func)  # <- ESSA LINHA É IMPORTANTE
        def wrapper(*args, **kwargs):
            auth = request.authorization
            if not auth or auth.username not in usuarios:
                return jsonify({"erro": "Não autorizado"}), 401

            usuario = usuarios[auth.username]
            if usuario["senha"] != auth.password:
                return jsonify({"erro": "Senha incorreta"}), 403

            if usuario["perfil"] not in perfis_permitidos:
                return jsonify({"erro": "Acesso negado para este perfil"}), 403

            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route("/dados")
@checar_autenticacao(["admin"])
def dados_privados():
    return jsonify({"mensagem": "Bem-vindo, administrador!"})

@app.route("/publico")
@checar_autenticacao(["admin", "usuario"])
def dados_publicos():
    return jsonify({"mensagem": "Bem-vindo! Acesso permitido."})

if __name__ == '__main__':
    app.run(debug=True)

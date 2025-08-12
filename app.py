from flask import Flask, request, jsonify
from functools import wraps # Pra preservar nome e info da função quando usar decorator

app = Flask(__name__) # Crio a aplicação Flask

# Usuários fixos, cada um com senha e perfil (admin ou usuário)
usuarios = {
    "joao": {"senha": "123", "perfil": "admin"},
    "maria": {"senha": "abc", "perfil": "usuario"}
}

# Decorator que vai checar se o usuário está autenticado e autorizado
def checar_autenticacao(perfis_permitidos):
    def decorator(func):
        @wraps(func)  # Mantém nome original da função para o Flask não confundir
        def wrapper(*args, **kwargs):
            auth = request.authorization # Pega usuário e senha da requisição

             # Se não enviou autenticação ou usuário não existe, rejeita com 401
            if not auth or auth.username not in usuarios:
                return jsonify({"erro": "Não autorizado"}), 401

            # Se a senha estiver errada, rejeita com 403 (proibido)
            usuario = usuarios[auth.username]
            if usuario["senha"] != auth.password:
                return jsonify({"erro": "Senha incorreta"}), 403
            
            # Se o perfil do usuário não estiver permitido, rejeita com 403
            if usuario["perfil"] not in perfis_permitidos:
                return jsonify({"erro": "Acesso negado para este perfil"}), 403
            
            # Se tudo ok, chama a função da rota normalmente
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Rota /dados só pra admin
@app.route("/dados")
@checar_autenticacao(["admin"])
def dados_privados():
    return jsonify({"mensagem": "Bem-vindo, administrador!"})

# Rota /publico pra admin e usuário
@app.route("/publico")
@checar_autenticacao(["admin", "usuario"])
def dados_publicos():
    return jsonify({"mensagem": "Bem-vindo! Acesso permitido."})

# Rodar o servidor em modo debug pra facilitar o desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)

import streamlit_authenticator as stauth
import yaml

# Informações dos usuários
credentials = {
    "usernames": {
        "usuario1": {
            "email": "usuario1@example.com",
            "name": "Usuario Um",
            "password": "senha_usuario1"
        },
        "usuario2": {
            "email": "usuario2@example.com",
            "name": "Usuario Dois",
            "password": "senha_usuario2"
        }
    }
}

# Gerar hashes para as senhas
usernames = list(credentials["usernames"].keys())
passwords = [credentials["usernames"][user]["password"] for user in usernames]
hashed_passwords = stauth.Hasher(passwords).generate()

# Atualizar o dicionário com os hashes
for i, user in enumerate(usernames):
    credentials["usernames"][user]["password"] = hashed_passwords[i]

# Configurações de cookies
cookie_config = {
    "cookie": {
        "expiry_days": 30,
        "key": "SUA_CHAVE_DE_COOKIE_SECRETA_AQUI",  # Substitua por uma chave segura
        "name": "servmar_cookie"
    }
}

# Combinar credenciais e configuração de cookies
config = {**credentials, **cookie_config}

# Salvar no arquivo config.yaml
with open('config.yaml', 'w') as file:
    yaml.dump(config, file)

print("Arquivo config.yaml gerado com sucesso!")

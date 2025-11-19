import bcrypt

# --- CADASTRO ---
senha_usuario = "minha_senha_secreta"

# Gera o "sal" (salt) aleatório
salt = bcrypt.gensalt()

print(salt)

# Cria o hash (transforma a senha numa sopa de letrinhas)
# O encode() é necessário pois o bcrypt trabalha com bytes
senha_hash = bcrypt.hashpw(senha_usuario.encode('utf-8'), salt)

print(senha_hash)

print(f"O que vai para o banco: {senha_hash}")
# Vai imprimir algo como: b'$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/M...'


# --- LOGIN ---

senha_digitada = input("senha: ")

if bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_hash):
    print("Login Aprovado!")
else:
    print("Senha Incorreta.")
# file = "test.txt"

# try:
#     with open(file, 'r', encoding='utf-8') as f:
#         conteudo = f.readlines()
#         conteudo = [palavra.strip() for palavra in conteudo]
#         print(conteudo)
# except UnicodeDecodeError:
#     print("Erro: O ficheiro não está em UTF-8.")
# except FileNotFoundError:
#     print(f"Erro: O ficheiro '{file}' não foi encontrado.")


import re
import os

entrada = "poligonos.txt"
saida = "poligonos.txt"

def limpar_linhas(entrada, saida):
    if not os.path.exists(entrada):
        raise FileNotFoundError(f"Arquivo não encontrado: {os.path.abspath(entrada)}")

    # Tenta UTF-8; se falhar, lê substituindo caracteres problemáticos
    try:
        with open(entrada, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except UnicodeDecodeError:
        with open(entrada, "r", encoding="utf-8", errors="replace") as f:
            linhas = f.readlines()

    # Remove dígitos em cada linha e tira espaços das extremidades
    linhas_limpo = [re.sub(r"\d+", "", linha).strip() for linha in linhas]

    # Opcional: remove linhas vazias resultantes
    linhas_limpo = [linha for linha in linhas_limpo if linha]

    with open(saida, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas_limpo))

    print(f"OK: gerado {os.path.abspath(saida)} com {len(linhas_limpo)} linhas limpas.")

if __name__ == "__main__":
    try:
        limpar_linhas(entrada, saida)
    except FileNotFoundError as e:
        print("Erro de arquivo:", e)
    except PermissionError as e:
        print("Permissão negada. Feche o arquivo se estiver aberto em outro programa e tente de novo.")
        print(e)
    except Exception as e:
        print("Erro inesperado:", type(e).__name__, "-", e)

import os

pasta = "Outros/rockyou/arquivos/rockyou-25.txt"
destino = "outros/rockyou/arquivos/rockyou"

nomes = os.listdir(pasta)

ultimo = nomes[-1]
with open(f"{destino}.txt", "w", encoding="UTF-8") as f:

    for nome in nomes:
        if nome == ultimo:
            f.write(f'{nome}')
#            f.write(f"\ngm04032013")
        else:
            f.write(f'{nome}\n')
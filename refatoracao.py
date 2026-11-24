
# Constantes
PRIORIDADE_ALTA = 1
PRIORIDADE_MEDIA = 2

PRIORIDADES = ["Alta", "Média", "Baixa"]

# Variáveis
nome = "Carlos"
prioridade = PRIORIDADE_MEDIA
status_demanda = "Pendente"


def mostrar_dados():
    """Exibe os dados da demanda."""
    print("Nome:", nome)
    print("Prioridade:", prioridade)
    print("Status:", status_demanda)


if prioridade == PRIORIDADE_ALTA:
    print("Alta")
elif prioridade == PRIORIDADE_MEDIA:
    print("Média")
else:
    print("Baixa")


mostrar_dados()

for item in PRIORIDADES:
    print("Prioridade disponível:", item)

contador = 1

while contador <= 3:
    print("Demanda número:", contador)
    contador += 1

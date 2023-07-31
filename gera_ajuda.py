def gera_ajuda(questao):
    opcoes = questao['opcoes']
    correta = questao['correta']
    incorretas = []

    for letra in opcoes.keys():
        if letra != correta:
            incorretas.append(letra)

    random.shuffle(incorretas)
    quantidade_opcoes = random.randint(1, 2)
    opcoes_incorretas_selecionadas = incorretas[:quantidade_opcoes]

    mensagem_ajuda = "DICA:\nOpções certamente erradas: " + " | ".join(opcoes_incorretas_selecionadas)

    return mensagem_ajuda
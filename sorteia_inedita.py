def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questao_sorteada = None

    if questoes_sorteadas:
        questoes_nivel = questoes[nivel]
        titulos_sorteados = [questao['titulo'] for questao in questoes_sorteadas]
        questoes_nao_sorteadas = [questao for questao in questoes_nivel if questao['titulo'] not in titulos_sorteados]

        if questoes_nao_sorteadas:
            questao_sorteada = random.choice(questoes_nao_sorteadas)
            questoes_sorteadas.append(questao_sorteada)
    else:
        questao_sorteada = sorteia_questao(questoes, nivel)
        if questao_sorteada:
            questoes_sorteadas.append(questao_sorteada)

    return questao_sorteada
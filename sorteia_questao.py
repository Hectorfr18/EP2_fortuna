def sorteia_questao(questoes, nivel):
    
    if nivel in questoes:
        questoes_nivel = questoes[nivel]
        questao_sorteada = random.choice(questoes_nivel)
        return questao_sorteada
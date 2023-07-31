def questao_para_texto(questao, id):
    
    titulo = questao['titulo']
    nivel = questao['nivel']
    opcoes = questao['opcoes']

    texto_questao = f"{'-' * 40}\n"
    texto_questao += f"QUESTAO {id}\n\n"
    texto_questao += f"{titulo}\n\n"
    texto_questao += "RESPOSTAS:\n"
    
    for letra, resposta in opcoes.items():
        texto_questao += f"{letra}: {resposta}\n"

    texto_questao += f"\nNível: {nivel.capitalize()}\n"
    texto_questao += '-' * 40

    return texto_questao

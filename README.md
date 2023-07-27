# EP2_fortuna

def transforma_base(questoes):
    base = {}

    for questao in questoes:
        nivel = questao['nivel']

        if nivel in base:
            base[nivel].append(questao)
        else:
            base[nivel] = [questao]

    return base
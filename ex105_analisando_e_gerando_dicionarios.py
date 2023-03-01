def notas(*num, sit=False):
    """Função para analisar notas e situações de vários alunos.

    Args:
        sit (bool, optional): Valor opcional, que válida a média da turma. Defaults to False.

    Returns:
        _type_:Dicionario com varias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
def fatorial(n, show=False):
    """Calcula o fatorial de um numero.

    Args:
        n (int): O numero a ser calculado.
        show (optional): Mostrar ou não a conta. Defaults to False.

    Returns:
        _type_: O valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f
    
    
print(fatorial(5, show=True))
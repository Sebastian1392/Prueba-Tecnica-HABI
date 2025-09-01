def solve_blocks(my_array):
    """
    Procesa un arreglo de bloques de números separados por ceros.

    Args:
        my_array (list): Una lista de enteros entre 1-9 y 0 como separador.

    Returns:
        str: Un string con los bloques ordenados y separados por espacios.
             Los bloques vacíos se representan con 'X'.
    """
    blocks = ''.join(map(str, my_array)).split('0')
    for i in range(len(blocks)):
        if blocks[i] == '':
            blocks[i] = 'X'
        else:
            sorted_group = ''.join(sorted(blocks[i]))
            blocks[i] = sorted_group
    resultString = ' '.join(blocks)
    return resultString
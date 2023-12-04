def agregar_asterisco(texto, patrones):
    for patron in patrones:
        if patron in texto:
            return '*'+texto
    return texto

import wikipedia

wikipedia.set_lang("pt")

def pesquisar(nome):

    return wikipedia.summary(nome, sentences=3)
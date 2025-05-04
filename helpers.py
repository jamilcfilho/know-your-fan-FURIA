def validar_documento(nome_arquivo):
    return nome_arquivo.lower().endswith(".pdf")


def validar_link(link):
    return link.startswith("http://") or link.startswith("https://")

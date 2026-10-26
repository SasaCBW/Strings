import re
from collections import Counter

STOPWORDS = {
    "a", "o", "as", "os", "um", "uma", "de", "do", "da",
    "dos", "das", "em", "no", "na", "por", "para", "com",
    "e", "ou", "que", "se", "ao", "é", "foi", "são",
    "como", "mais", "mas", "não", "sua", "seu", "uma",
    "este", "esta", "esse", "essa", "ele", "ela"
}


def extrair_palavras_chave(texto, quantidade=10):
    texto = texto.lower()
    palavras = re.findall(r"\b[a-zA-ZÀ-ÿ]+\b", texto)

    palavras_filtradas = [
        palavra for palavra in palavras
        if palavra not in STOPWORDS and len(palavra) > 2
    ]

    frequencias = Counter(palavras_filtradas)
    return frequencias.most_common(quantidade)


def main():
    print("=== EXTRATOR DE PALAVRAS-CHAVE ===")
    texto = input("Digite ou cole um texto:\n")

    if not texto.strip():
        print("Erro: digite um texto.")
        return

    resultado = extrair_palavras_chave(texto)

    if not resultado:
        print("Nenhuma palavra-chave encontrada.")
        return

    print("\nPalavras-chave encontradas:")
    for palavra, frequencia in resultado:
        print(f"{palavra}: {frequencia} ocorrência(s)")


if __name__ == "__main__":
    main()

import json

README_PATH = "README.md"
BOARD_PATH = "board.json"

# Gera um tabuleiro simples de exemplo
def gerar_tabuleiro():
    return [
        ["⬜", "💣", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["💣", "⬜", "⬜"]
    ]

def atualizar_readme(tabuleiro):
    with open(README_PATH, "r", encoding="utf-8") as f:
        conteudo = f.read()

    tabuleiro_md = "\n".join("".join(linha) for linha in tabuleiro)

    # Substitui apenas a parte do campo minado no README
    novo_conteudo = conteudo.split("<!-- minesweeper-start -->")[0] + \
        "<!-- minesweeper-start -->\n" + tabuleiro_md + "\n<!-- minesweeper-end -->" + \
        conteudo.split("<!-- minesweeper-end -->")[1]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(novo_conteudo)

if __name__ == "__main__":
    tabuleiro = gerar_tabuleiro()
    atualizar_readme(tabuleiro)

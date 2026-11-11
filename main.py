#-----------------------------🌊-Mudanças--Climáticas--ÁGUA E O CONSUMO-🌎------------------------------------

from pathlib import Path
from flask import Flask, render_template
import shutil
import sys

# Caminho principal do projeto
BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

HTML_DESTINO = TEMPLATES_DIR / "index.html"
CSS_DESTINO = STATIC_DIR / "styles.css"

app = Flask(__name__)


def preparar_site():
    # Criar pastas necessárias
    TEMPLATES_DIR.mkdir(exist_ok=True)
    STATIC_DIR.mkdir(exist_ok=True)

    # Procurar HTML original
    if not HTML_DESTINO.exists():
        arquivos_html = [
            BASE_DIR / "index.html",
            BASE_DIR / "Texto colado (2).txt"
        ]

        origem = next(
            (arquivo for arquivo in arquivos_html if arquivo.is_file()),
            None
        )

        if origem is None:
            raise FileNotFoundError("Arquivo HTML não encontrado!")

        shutil.copy2(origem, HTML_DESTINO)

    # Procurar CSS original
    if not CSS_DESTINO.exists():
        arquivos_css = [
            BASE_DIR / "styles.css",
            BASE_DIR / "Texto colado.txt"
        ]

        origem = next(
            (arquivo for arquivo in arquivos_css if arquivo.is_file()),
            None
        )

        if origem is None:
            raise FileNotFoundError("Arquivo CSS não encontrado!")

        shutil.copy2(origem, CSS_DESTINO)


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Verificar funcionamento
@app.route("/status")
def status():
    return {
        "status": "online",
        "site": "Gota a Gota"
    }


# Inicialização
if __name__ == "__main__":
    try:
        preparar_site()

        print("==============================")
        print("🌊 GOTA A GOTA")
        print("==============================")
        print("Site iniciado com sucesso!")
        print("Acesse: http://127.0.0.1:5000")
        print("==============================")

        app.run(
            host="127.0.0.1",
            port=5000,
            debug=False
        )

    except Exception as erro:
        print(f"ERRO AO INICIAR: {erro}")
        sys.exit(1)

import csv
import os
import requests
from io import BytesIO
from PIL import Image

# CONFIGURAÇÕES
CSV_FILE = 'imagens.csv'
OUTPUT_DIR = 'imagens_webp'
WEBP_QUALITY = 85
TIMEOUT = 15

os.makedirs(OUTPUT_DIR, exist_ok=True)

def otimizar_para_webp(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; ImageOptimizer/1.0)"
        }

        response = requests.get(url.strip(), headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        nome_original = os.path.basename(url.split("?")[0])
        nome_base = os.path.splitext(nome_original)[0]
        nome_webp = f"{nome_base}.webp"

        caminho_saida = os.path.join(OUTPUT_DIR, nome_webp)

        imagem = Image.open(BytesIO(response.content))

        if imagem.mode in ("RGBA", "LA", "P"):
            imagem = imagem.convert("RGBA")
        else:
            imagem = imagem.convert("RGB")

        imagem.save(
            caminho_saida,
            "WEBP",
            quality=WEBP_QUALITY,
            method=6
        )

        print(f"✔ Convertida: {nome_webp}")

    except Exception as e:
        print(f"✖ Erro ao processar {url}: {e}")

def processar_csv():
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row and row[0].strip():
                otimizar_para_webp(row[0])

if __name__ == "__main__":
    processar_csv()

📁 Estrutura correta dos arquivos

Coloque tudo na mesma pasta:

/projeto-imagens/
│
├── script.py
├── imagens.csv
└── imagens_webp/        ← criada automaticamente

📄 Nome do arquivo CSV (OBRIGATÓRIO)

🔹 Nome:

imagens.csv


🔹 Conteúdo obrigatório:

url

https://site.com/wp-content/uploads/2023/01/imagem1.jpg
https://site.com/wp-content/uploads/2023/01/banner.png

🐍 Nome do script Python
🔹 Nome do arquivo: script.py

Você pode mudar o nome se quiser, desde que altere esta linha no código:
CSV_FILE = 'imagens.csv'


Exemplo:

CSV_FILE = 'minhas-imagens.csv'

📂 Pasta de saída (automática)

🔹 Nome da pasta criada automaticamente pelo script:

imagens_webp


Se quiser mudar:

OUTPUT_DIR = 'webp_otimizadas'

▶️ Como rodar o script (passo a passo)

No terminal, dentro da pasta do projeto:

python script.py


Pronto ✅
As imagens WebP aparecerão em:

/imagens_webp/

🔁 O que acontece com o nome das imagens?

Exemplo prático:

URL original	Arquivo gerado
imagem-produto-01.jpg	imagem-produto-01.webp
banner-home.png	banner-home.webp
foto.webp	foto.webp

✔ Mesmo nome
✔ Apenas troca da extensão
✔ SEO-safe

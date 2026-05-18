import json
import os
import glob
import numpy as np
from sentence_transformers import SentenceTransformer

def gerar_banco_vetorial(pasta_chunks, caminho_banco_saida):
    """
    Lê todos os arquivos _chunks.json de uma pasta,
    gera embeddings em lote (batch) e salva o banco vetorial.
    """
    print("⏳ Carregando o modelo neural...")
    modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

    # Coleta todos os arquivos de chunks da pasta
    arquivos = glob.glob(os.path.join(pasta_chunks, "*_chunks.json"))
    if not arquivos:
        print("❌ Nenhum arquivo _chunks.json encontrado na pasta.")
        return

    print(f"📂 {len(arquivos)} arquivo(s) de chunks encontrado(s).")

    todos_textos = []
    todas_origens = []

    for arquivo in arquivos:
        with open(arquivo, 'r', encoding='utf-8') as f:
            chunks = json.load(f)
        for chunk in chunks:
            todos_textos.append(chunk['chunk_text'])
            todas_origens.append(chunk['source_path'])

    total = len(todos_textos)
    print(f"🧠 Gerando embeddings para {total} chunks em lote...")

    # CORREÇÃO PRINCIPAL: encode em batch (muito mais rápido que um por vez)
    vetores = modelo.encode(
        todos_textos,
        batch_size=32,          # processa 32 chunks por vez na GPU/CPU
        show_progress_bar=True, # barra de progresso automática
        convert_to_numpy=True   # retorna numpy array direto
    )

    # Monta o banco vetorial
    banco_vetorial = [
        {
            "origem": todas_origens[i],
            "texto": todos_textos[i],
            "vector": vetores[i].tolist()
        }
        for i in range(total)
    ]

    # Salva o JSON do banco
    os.makedirs(os.path.dirname(caminho_banco_saida), exist_ok=True)
    with open(caminho_banco_saida, 'w', encoding='utf-8') as f:
        json.dump(banco_vetorial, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Banco vetorial JSON salvo em: {caminho_banco_saida}")
    print(f"   Total de vetores: {total} | Dimensão: {vetores.shape[1]}")
    print("O JARVIS agora tem memória matemática!")

# ==========================================
# ÁREA DE EXECUÇÃO
# ==========================================

# Pasta onde estão todos os _chunks.json gerados pelo chunks.py
PASTA_CHUNKS = r"C:\Programas\facul\IA\Documents\Chunks"

# Onde o banco de dados JSON final será salvo
BANCO_FINAL = r"C:\Programas\facul\IA\Documents\embeddings"

gerar_banco_vetorial(PASTA_CHUNKS, BANCO_FINAL)
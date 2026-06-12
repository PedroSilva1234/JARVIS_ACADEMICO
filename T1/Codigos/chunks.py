import os
import json
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_md(md_path):
    """Lê o conteúdo de um arquivo Markdown."""
    with open(md_path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_text(text, chunk_size=800, overlap=150):
    """
    Divide o texto em blocos 
    """
    chunks = []
    start = 0
    length = len(text)
    
    while start < length:
        # Define onde o bloco idealmente deveria terminar
        end = min(start + chunk_size, length)
        
        # Só tenta recuar se não estivermos no fim do texto
        if end < length:
            original_end = end
            
            # Limite máximo que o algoritmo pode recuar (para garantir que ele sempre avance)
            limite_recuo = start + overlap
            
            # Recua até achar um espaço, MAS para se bater no limite
            while end > limite_recuo and text[end] not in [' ', '\n', '\t']:
                end -= 1
                
            # Se bateu no limite e não achou espaço (ex: um link de site gigante),
            # nós cancelamos o recuo e fazemos um corte seco. A segurança vem primeiro!
            if end == limite_recuo:
                end = original_end
                
        # Adiciona o bloco na lista
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
            
        # Se chegou no fim, quebra o laço na hora
        if end == length:
            break
            
        # Cálculo matemático do próximo passo
        start = end - overlap
        
    return chunks

def process_md_to_chunks(md_path, save_folder):
    """Processa um arquivo MD específico e salva seus chunks em JSON."""
    text = extract_text_from_md(md_path)
    chunks = chunk_text(text)
    
    base_name = os.path.splitext(os.path.basename(md_path))[0]
    file_name = base_name + '.md'
    save_path = os.path.join(save_folder, base_name + '_chunks.json')
    
    chunk_data = [{'source_path': file_name, 'chunk_text': c} for c in chunks]
    
    os.makedirs(save_folder, exist_ok=True)
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(chunk_data, f, ensure_ascii=False, indent=2)
    
    print(f'✅ Processado {file_name} em {len(chunks)} chunks.')
    print(f'   Salvo em: {save_path}')
    return chunk_data

def processar_pasta_completa(input_folder, save_folder):
    """Varre uma pasta e processa todos os arquivos .md encontrados."""
    print(f"Iniciando processamento da pasta: {input_folder}")
    todos_chunks = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.md'):
            md_path = os.path.join(input_folder, filename)
            chunks_do_arquivo = process_md_to_chunks(md_path, save_folder)
            todos_chunks.extend(chunks_do_arquivo)

# ==========================================
# ÁREA DE EXECUÇÃO
# ==========================================

# 1. Caminho para a pasta dos estão os arquivos .md 
pasta_entrada = os.getenv(r'PASTA_MD') 

# 2. Caminho para onde os JSONs devem ser salvos 
pasta_saida = os.getenv(r'PASTA_CHUNKS')

# Executa o processamento para a pasta toda
processar_pasta_completa(pasta_entrada, pasta_saida)
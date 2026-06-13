import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_md(md_path):
    """Lê o conteúdo de um arquivo Markdown."""
    with open(md_path, 'r', encoding='utf-8') as f:
        return f.read()
import re

# Mude a assinatura da função para receber o nome_doc
def chunk_by_headers(text, nome_doc):
    """
    Divide o texto com base em cabeçalhos Markdown (#),
    injetando a origem em TODOS os chunks e filtrando blocos inúteis.
    """
    chunks = []
    current_content = []
    
    # 1. CORREÇÃO DE ERRO FATAL: Define um título padrão caso o texto comece sem '# '
    current_header = "Início do Documento" 
    
    for line in text.split('\n'):
        if re.match(r'^#+ ', line):
            # Junta o conteúdo acumulado até agora
            texto_acumulado = '\n'.join(current_content).strip()
            
            # 2. O FILTRO DE QUALIDADE (< 50 caracteres)
            if texto_acumulado and len(texto_acumulado) >= 50:
                chunk_final = f"[Documento: {nome_doc}] | Seção: {current_header}\n\n{texto_acumulado}"
                chunks.append(chunk_final)
            elif texto_acumulado:
                print(f"🗑️ Chunk lixo ignorado na seção: '{current_header}'")
            # Atualiza o cabeçalho para o novo bloco
            current_header = re.sub(r'^#+ ', '', line).strip()
            # Salva a linha do cabeçalho como a primeira linha do novo conteúdo
            current_content = [line] 
            
        else:
            current_content.append(line)
            
    # Processa o último bloco que sobrou no final do arquivo
    texto_acumulado = '\n'.join(current_content).strip()
    if texto_acumulado and len(texto_acumulado) >= 50:
         chunk_final = f"[Documento: {nome_doc}] | Seção: {current_header}\n\n{texto_acumulado}"
         chunks.append(chunk_final)
         
    return chunks

def process_md_to_chunks(md_path, save_folder):
    text = extract_text_from_md(md_path)
    
    base_name = os.path.splitext(os.path.basename(md_path))[0] # Pega o nome "PPC-ENG-COMP-Completo"
    
    # Passa o base_name para a função!
    chunks = chunk_by_headers(text, nome_doc=base_name) 
    
    base_name = os.path.splitext(os.path.basename(md_path))[0]
    file_name = base_name + '.md'
    save_path = os.path.join(save_folder, base_name + '_chunks.json')
    
    chunk_data = [{'source_path': file_name, 'chunk_text': c} for c in chunks]
    
    os.makedirs(save_folder, exist_ok=True)
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(chunk_data, f, ensure_ascii=False, indent=2)
    
    print(f'✅ Processado {file_name} em {len(chunks)} chunks enriquecidos.')
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
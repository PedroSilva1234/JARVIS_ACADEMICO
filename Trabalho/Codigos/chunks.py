import os
import json

def extract_text_from_md(md_path):
    """Lê o conteúdo de um arquivo Markdown."""
    with open(md_path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_text(text, chunk_size=800, overlap=150):
    """
    Divide o texto em blocos de forma inteligente.
    Garante o avanço matemático absoluto para evitar loops infinitos.
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
            
        # Cálculo matemático 100% seguro do próximo passo
        start = end - overlap
        
    return chunks

def process_md_to_chunks(md_path, save_folder):
    """Processa um arquivo MD específico e salva seus chunks em JSON."""
    text = extract_text_from_md(md_path)
    chunks = chunk_text(text)
    
    base_name = os.path.splitext(os.path.basename(md_path))[0]
    file_name = base_name + '.md'
    save_path = os.path.join(save_folder, base_name + '_chunks.json')
    
    # Usando 'origem' e 'texto' para bater com nosso sistema RAG
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
            
    # Opcional: Salvar um arquivo "master" com todos os chunks de todos os arquivos
   # master_path = os.path.join(save_folder, 'todos_chunks_master.json')
    #with open(master_path, 'w', encoding='utf-8') as f:
     #   json.dump(todos_chunks, f, ensure_ascii=False, indent=2)
    #print(f"\n🚀 Arquivo master criado com {len(todos_chunks)} chunks totais: {master_path}")

# ==========================================
# ÁREA DE EXECUÇÃO
# ==========================================

# 1. Caminho para a pasta onde estão seus arquivos .md (Sua pasta 'data')
pasta_entrada = r'C:\Programas\facul\IA\Trabalho\Documents\Markdows'

# 2. Caminho para onde os JSONs devem ser salvos (Sua pasta 'rag' ou 'data')
pasta_saida = r'C:\Programas\facul\IA\Trabalho\Documents\Chunks'

# Executa o processamento para a pasta toda
# (Lembre-se de criar alguns arquivos .md de teste na pasta de entrada antes de rodar)
processar_pasta_completa(pasta_entrada, pasta_saida)


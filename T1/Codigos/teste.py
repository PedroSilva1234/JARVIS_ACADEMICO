import os
from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# Importa os motores de busca que criamos
from retrieval import IndicesRAG, buscar_hibrido
from dotenv import load_dotenv

load_dotenv()
# ==========================================
# 1. CONFIGURAÇÕES INICIAIS
# ==========================================
load_dotenv()

PASTA_INDICES = os.getenv(r'PASTA_EMBEDDINGS') 

print("🧠 Acordando o JARVIS...")
print("⏳ Carregando modelos de matemática (Aguarde)...")

modelo_embedding = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
indices_rag = IndicesRAG(PASTA_INDICES)

client = OpenAI(
    base_url='https://llm.liaufms.org/v1/gemma-3-12b-it', # MANTENHA O NOME AQUI!
    api_key=os.getenv('LIA_API_KEY')
)
# ==========================================
# 2. SISTEMA DE BUSCA PROATIVA
# ==========================================
def executar_busca_rag(pergunta):
    """Executa a busca híbrida antes de chamar a LLM."""
    print(f"\n[JARVIS varrendo banco de dados acadêmico...]")
    
    resultados = buscar_hibrido(
        query=pergunta,
        modelo=modelo_embedding,
        indices=indices_rag,
        top_k=3,
        peso_semantico=0.6
    )
    
    contexto_formatado = ""
    for r in resultados:
        contexto_formatado += f"--- [Fonte: {r['origem']}] ---\n{r['texto']}\n\n"
        
    return contexto_formatado

# ==========================================
# 3. COMPORTAMENTO DA IA
# ==========================================
SYSTEM_PROMPT = """Você é o JARVIS Acadêmico, um tutor de IA brilhante e didático.
Sua missão é ajudar o aluno respondendo dúvidas baseadas EXCLUSIVAMENTE nos materiais de contexto fornecidos na mensagem.

REGRAS:
1. Use formatação Markdown para deixar a explicação bonita e didática.
2. Use LaTeX para fórmulas matemáticas usando o formato $formula$ ou $$formula$$.
3. SEMPRE cite o nome do arquivo de origem da informação (ex: "Segundo o material *aula13.md*...").
4. Se o usuário fizer apenas uma saudação (ex: "Olá"), responda educadamente oferecendo ajuda nos estudos.
5. Se a resposta para a pergunta não estiver no contexto fornecido, diga honestamente que não encontrou a informação nos materiais atuais."""


# ==========================================
# 4. LOOP PRINCIPAL DE CONVERSA
# ==========================================
def main():
    print("\n" + "="*50)
    print("🤖 JARVIS Online e pronto para ajudar nos estudos.")
    print("Digite 'sair' para encerrar os sistemas.")
    print("="*50 + "\n")
    
    historico = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("JARVIS: Desligando. Bons estudos, senhor!")
            break
        if not user_input.strip(): continue

        try:
            # 1. Busca os documentos no seu banco vetorial/híbrido ANTES de chamar a IA
            textos_recuperados = executar_busca_rag(user_input)
            
            # 2. Monta o super-prompt combinando a dúvida e os PDFs lidos
            prompt_enriquecido = f"""
CONTEXTOS RECUPERADOS DO BANCO DE DADOS:
{textos_recuperados}

PERGUNTA DO ALUNO:
{user_input}
"""
            # Adiciona apenas no histórico temporário da requisição para não poluir a tela
            mensagens_para_llm = historico.copy()
            mensagens_para_llm.append({"role": "user", "content": prompt_enriquecido})

            # 3. Faz a chamada simples para a IA
            resposta = client.chat.completions.create(
                model='google/gemma-3-12b-it', # MANTENHA O 'google/' AQUI!
                messages=mensagens_para_llm,
                temperature=0.2
            )
            
            conteudo_resposta = resposta.choices[0].message.content
            print(f"\nJARVIS:\n{conteudo_resposta}\n")
            
            # Salva no histórico real apenas o que foi conversado
            historico.append({"role": "user", "content": user_input})
            historico.append({"role": "assistant", "content": conteudo_resposta})

        except Exception as e:
            print(f"\n⚠️ Falha no sistema de comunicação: {e}\n")

if __name__ == "__main__":
    main()
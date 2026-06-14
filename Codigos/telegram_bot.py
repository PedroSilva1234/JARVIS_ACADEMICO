import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from sentence_transformers import SentenceTransformer
from retrieval import IndicesRAG
from gerar_respostas import gerar_resposta, montar_system_prompt, SESSAO_ACTIVE_RECALL

# Importa as peças do seu JARVIS (Garanta que a pasta está correta)
from retrieval import IndicesRAG
from gerar_respostas import gerar_resposta, montar_system_prompt

# Carrega as chaves
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    print("🚨 ERRO: TELEGRAM_TOKEN não encontrado no arquivo .env!")
    exit()

print("⏳ Iniciando motores e carregando banco de dados RAG...")
# Inicializa os modelos uma única vez (Globais)
modelo_emb = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
indices = IndicesRAG(os.getenv('PASTA_EMBEDDINGS'))
print("✅ Sistemas RAG carregados e prontos!")

# Memória do Bot: Guarda o histórico de conversa separado para cada usuário
memorias_usuarios = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde ao comando /start"""
    chat_id = update.message.chat_id
    
    # Inicia a memória deste chat com o Prompt de Sistema
    memorias_usuarios[chat_id] = [{"role": "system", "content": montar_system_prompt()}]
    
    await update.message.reply_text(
        "🤖 Sistemas operacionais online.\n\n"
        "Olá! Sou o JARVIS Acadêmico. Estou conectado aos seus materiais didáticos.\n"
        "O que vamos estudar hoje?"
    )

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde ao comando /end, limpando a memória do usuário"""
    chat_id = update.message.chat_id
    if chat_id in memorias_usuarios:
        del memorias_usuarios[chat_id]
    await update.message.reply_text("👋 Memória limpa. Até a próxima! Use /start para recomeçar.")

async def processar_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Recebe a mensagem de texto, envia pro RAG e devolve a resposta"""
    chat_id = update.message.chat_id
    texto_usuario = update.message.text
    
    # Se o bot reiniciou, recria a memória do usuário
    if chat_id not in memorias_usuarios:
        memorias_usuarios[chat_id] = [{"role": "system", "content": montar_system_prompt()}]
        
    historico = memorias_usuarios[chat_id]

    if "atual" in SESSAO_ACTIVE_RECALL and not SESSAO_ACTIVE_RECALL["atual"].encerrada:
        sessao_ativa = SESSAO_ACTIVE_RECALL["atual"]
        
        # Manda o feedback visual pro celular
        mensagem_espera = await update.message.reply_text("⏳ *Avaliando resposta...*", parse_mode="Markdown")
        
        try:
            # Envia a resposta direto para a classe de aprendizado (sem IA do Jarvis interferir)
            feedback = sessao_ativa.avaliar_resposta(texto_usuario)
            
            # Atualiza o histórico para o JARVIS não ficar confuso depois do teste
            historico.append({"role": "user", "content": texto_usuario})
            historico.append({"role": "assistant", "content": feedback})
            
            # Se a palavra 'parar' encerrou a sessão, limpamos o dicionário
            if sessao_ativa.encerrada:
                del SESSAO_ACTIVE_RECALL["atual"]
                
            # Entrega a nota pro usuário
            await mensagem_espera.edit_text(feedback)
            
            # 🛑 ENCERRA A FUNÇÃO AQUI! O 'return' impede que o código continue 
            # e chame a função gerar_resposta lá embaixo.
            return 
            
        except Exception as e:
            await mensagem_espera.edit_text(f"⚠️ Erro ao avaliar a resposta: {e}")
            return
    # =========================================================

    # Se não houver Active Recall rodando, segue o fluxo normal de conversa
    historico.append({"role": "user", "content": texto_usuario})
    mensagem_espera = await update.message.reply_text("⏳ *Consultando...*", parse_mode="Markdown")

    try:
        # A MÁGICA ACONTECE AQUI: Chama a sua função RAG original
        resposta_jarvis = gerar_resposta(historico, modelo_emb, indices)
        
        # Salva no histórico
        historico.append({"role": "assistant", "content": resposta_jarvis})
        
        # Substitui o "Consultando..." pela resposta final
        await mensagem_espera.edit_text(resposta_jarvis)
        
    except Exception as e:
        await mensagem_espera.edit_text(f"⚠️ Falha no sistema de comunicação: {e}")

def main():
    """Liga o servidor do bot"""
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Adiciona os comandos que o bot entende
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("end", end))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, processar_mensagem))
    
    print("🚀 JARVIS Online no Telegram! Abra o app e mande um /start.")
    print("Pressione Ctrl+C no terminal para desligar.")
    
    # Deixa o bot rodando para sempre ouvindo mensagens
    app.run_polling()

if __name__ == '__main__':
    main()


import logging
import random
import smtplib
import asyncio
from email.message import EmailMessage
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURAÇÕES DE AMBIENTE ---
# Substitua estas strings pelas suas credenciais reais em seu ambiente local.
TOKEN_TELEGRAM = "SEU_TOKEN_AQUI"
EMAIL_REMETENTE = "SEU_EMAIL_AQUI"
SENHA_EMAIL = "SUA_SENHA_DE_APP_AQUI"
LINK_WHATSAPP = "SEU_LINK_DO_GRUPO_AQUI"

# Dicionário para controle de estado dos usuários (RU e Código gerado)
dados_validacao = {}

def enviar_codigo(email_destino, codigo):
    """ Gerencia a conexão SMTP e dispara o e-mail de validação """
    msg = EmailMessage()
    msg.set_content(f"Seu código de acesso ao grupo de Engenharia de Software é: {codigo}")
    msg['Subject'] = 'Validação de Acesso - UNINTER'
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = email_destino

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_REMETENTE, SENHA_EMAIL)
        smtp.send_message(msg)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Comando inicial para novos usuários """
    await update.message.reply_text("Olá! Digite seu RU para iniciar a validação:")

async def processar_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ 
    Lógica principal: identifica se a entrada é um RU (início) ou um Código (finalização).
    Possui filtro para aceitar apenas dígitos numéricos.
    """
    user_id = update.effective_user.id
    texto = update.message.text.strip()

    # Sanitização: Bloqueia caracteres não numéricos
    if not texto.isdigit():
        await update.message.reply_text("⚠️ Erro: Entrada deve conter apenas números.")
        return

    # Se o texto tiver padrão de RU (5 a 10 dígitos)
    if 5 <= len(texto) <= 10:
        # Reseta o processo caso o usuário já estivesse tentando validar
        if user_id in dados_validacao:
            del dados_validacao[user_id] 
        
        ru = texto
        codigo = str(random.randint(100000, 999999))
        email_aluno = f"{ru}@alunouninter.com"
        
        await update.message.reply_text(f"Enviando código para: {email_aluno}...")
        
        try:
            # Envio assíncrono para não travar a operação do Bot
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, enviar_codigo, email_aluno, codigo)
            
            dados_validacao[user_id] = {"ru": ru, "codigo": codigo}
            await update.message.reply_text("Código enviado! Verifique seu e-mail acadêmico e digite os 6 dígitos abaixo:")
        except Exception:
            await update.message.reply_text("Erro ao enviar e-mail. Tente novamente em instantes.")
        return

    # Validação do Token enviado pelo usuário
    if user_id in dados_validacao:
        if texto == dados_validacao[user_id]["codigo"]:
            await update.message.reply_text(f"✅ Sucesso! Link do grupo: {LINK_WHATSAPP}")
            del dados_validacao[user_id] # Limpa a memória após validação concluída
        else:
            await update.message.reply_text("❌ Código incorreto. Envie o RU novamente para resetar.")
    else:
        await update.message.reply_text("Por favor, envie um RU válido primeiro.")

if __name__ == '__main__':
    print("Servidor de Validação Online...")
    app = Application.builder().token(TOKEN_TELEGRAM).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, processar_texto))
    app.run_polling(drop_pending_updates=True)

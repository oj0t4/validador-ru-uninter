# 🛡️ Bot Validador de Acesso Acadêmico

Sistema de segurança desenvolvido em Python para automatizar a entrada de estudantes em comunidades digitais. O bot utiliza uma camada de autenticação via e-mail institucional (2FA) para garantir a integridade do grupo.

## 📋 Como o sistema funciona
1. **Solicitação de Identidade:** O bot recebe o RU (Registro Universitário) do aluno.
2. **Geração de Token:** Um código aleatório de 6 dígitos é gerado e armazenado temporariamente em memória.
3. **Validação por E-mail:** O sistema dispara o código para o e-mail oficial `@alunouninter.com`.
4. **Liberação de Acesso:** Após a inserção correta do código no Telegram, o link de convite do grupo é enviado.

## 🛠️ Detalhes Técnicos e Segurança
- **Sanitização de Input:** Implementação de filtro rígido que aceita apenas caracteres numéricos, prevenindo entradas inválidas ou maliciosas.
- **Processamento Assíncrono:** Uso da biblioteca `asyncio` para garantir que o envio de e-mails não bloqueie o atendimento de outros usuários.
- **Gestão de Estado:** Lógica de reinicialização automática — se o usuário enviar um novo RU no meio do processo, o sistema limpa o buffer anterior e recomeça o fluxo.

## ⚙️ Configuração (Variáveis Plaintext)
Para rodar este serviço localmente, é necessário configurar as seguintes variáveis no cabeçalho do código:
- `TOKEN_TELEGRAM`: Chave da API do bot.
- `EMAIL_REMETENTE`: Endereço de e-mail para disparo dos códigos.
- `SENHA_EMAIL`: Senha de App configurada no provedor de e-mail.
- `LINK_WHATSAPP`: Destino final do usuário após validação.

---
*Desenvolvido como projeto prático para o curso de Engenharia de Software.*

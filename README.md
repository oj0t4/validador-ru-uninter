# 🛡️ Bot Validador de Acesso Acadêmico

### 🔗 [Acesse o Bot aqui!](https://t.me/portariaavauninterbot)
*(Substitua o link acima pelo link real do seu bot)*

Sistema de segurança desenvolvido em Python para automatizar a entrada de estudantes em comunidades digitais. O bot utiliza uma camada de autenticação via e-mail institucional (2FA) para garantir a integridade do grupo.

## 📋 Como o sistema funciona
1. **Solicitação de Identidade:** O bot recebe o RU (Registro Universitário) do aluno.
2. **Geração de Token:** Um código aleatório de 6 dígitos é gerado e armazenado temporariamente em memória.
3. **Validação por E-mail:** O sistema dispara o código para o e-mail oficial `@alunouninter.com`.
4. **Liberação de Acesso:** Após a inserção correta do código no Telegram, o link de convite do grupo é enviado.

## 🛠️ Detalhes Técnicos e Segurança
- **Sanitização de Input:** Filtro rígido que aceita apenas dígitos numéricos, prevenindo erros de processamento.
- **Processamento Assíncrono:** Uso de `asyncio` para garantir que o envio de e-mails não bloqueie o atendimento de outros usuários.
- **Gestão de Estado:** Lógica de reinicialização automática (Idempotência) ao reenviar um RU.

## ⚙️ Configuração (Variáveis Plaintext)
Para rodar este serviço localmente, configure:
- `TOKEN_TELEGRAM`: Chave da API do bot.
- `EMAIL_REMETENTE`: E-mail para disparo dos códigos.
- `SENHA_EMAIL`: Senha de App do provedor.
- `LINK_WHATSAPP`: Destino final após validação.

---
*Projeto desenvolvido para fins acadêmicos e portfólio de Engenharia de Software.*

# PortalRPA - Primeiro teste de automação

Este é um exemplo mínimo de automação para testar o monitoramento do PortalRPA.

## Objetivo

- Simular uma automação simples em Python
- Expor endpoints de saúde e execução
- Gerar logs em arquivo para facilitar o monitoramento
- Ser facilmente hospedado em GitHub e executado em qualquer ambiente

## Estrutura

- `app.py` - aplicação principal
- `requirements.txt` - dependências
- `Dockerfile` - opcional para deploy em servidor/container
- `.gitignore` - arquivos locais do ambiente

## Como executar localmente

```bash
cd portalrpa-primeiro-teste
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

A aplicação irá subir em:

## Endpoints

### GET /health
Retorna o status da automação.

### GET /run
Executa uma simulação simples:
- lê uma tarefa
- processa algumas etapas
- registra mensagens de log
- retorna status final

### GET /status
Retorna o estado atual da automação.

## Como hospedar no GitHub

1. Crie um repositório vazio no GitHub.
2. Envie esta pasta para o repositório:

```bash
git init
git add .
git commit -m "Primeiro teste de automação PortalRPA"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git push -u origin main
```

3. Depois, você pode usar esse projeto como o primeiro teste no PortalRPA, apontando para o serviço hospedado ou para uma instância local de teste.

## Exemplo de uso no PortalRPA

Use esse projeto como uma automação de teste com:
- nome: `demo-portalrpa`
- descrição: `Automação de teste inicial`
- endpoint de checagem: `/health`
- status esperado: `RUNNING` quando a aplicação estiver ativa

## Observação

Esta automação é intencionalmente simples e foi pensada para servir como base para versões mais reais depois.

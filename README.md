# Projeto Agente IA com RAG e OpenAI

Este projeto cria um backend em FastAPI que utiliza uma abordagem RAG (Retrieval Augmented Generation) para responder perguntas sobre o meu portfólio. A API recupera dados do Supabase e, em seguida, utiliza a LLM da OpenAI (GPT‑3.5‑turbo) para gerar respostas.

## Pré-requisitos

- Python 3.8 ou superior
- Conta no Supabase com uma tabela `portfolio_data` contendo, pelo menos, os campos `title` e `content`
- Chave de API da OpenAI

## Configuração

1. Clone o repositório.
2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
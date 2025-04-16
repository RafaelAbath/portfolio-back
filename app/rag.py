import os
import openai
from app.supabase_client import supabase
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise Exception("A variável OPENAI_API_KEY deve estar definida no .env.")

def retrieve_documents(question: str):
    """
    Recupera os documentos da tabela 'projetos' do Supabase.
    Essa implementação inicial retorna todos os registros.
    """
    response = supabase.table("projetos").select("*").execute()
    documents = response.data or []
    return documents

def generate_answer(question: str) -> str:
    """
    Combina os dados recuperados do Supabase e a pergunta do usuário para
    construir um prompt e envia à LLM da OpenAI para gerar a resposta.
    """
    documents = retrieve_documents(question)

    
    context = ""
    for doc in documents:
        title = doc.get("title", "Sem título")
        content = doc.get("content", "Sem conteúdo")
        context += f"{title}: {content}\n"

    
    prompt = (
        "Você agirá como meu assistente particular, quero que responda apenas perguntas relacionadas ao Rafael Abath, utilize sempre como base os dados dos documentos que forem entregues a você. Será meu agente de IA particular para responder dúvidas do meu portfolio:\n\n"
        f"Dados do portfólio:\n{context}\n"
        f"Pergunta: {question}\n\n"
        "Resposta:"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente IA que responde perguntas sobre o portfólio, utilizando os dados fornecidos."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.7,
        )
        answer = response.choices[0].message['content'].strip()
    except Exception as e:
        answer = f"Erro ao gerar resposta: {str(e)}"

    return answer
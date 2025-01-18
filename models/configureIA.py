import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path


pdfs_pendentes = os.listdir(Path(r'..\src\pending'))
conteudo_pdf = ''

os.environ['GROQ_API_KEY'] = os.getenv('API_KEY')

chat = ChatGroq(model='llama-3.3-70b-versatile')

for arquivo in pdfs_pendentes:
  pdf = Path(rf"{pdfs_pendentes}\{arquivo}")
  loader = PyPDFLoader(pdf)
  dados_pdf = loader.load()

  for doc in dados_pdf:
    conteudo_pdf += doc.page_content


template = ChatPromptTemplate.from_messages([
    (
        "system",
        "Voce é um assistente chamado J-bote, e a partir de agora tem acesso ao {conteudo_pdf}"
    ),
    ('user', '{input}'),
])

chain = template | chat

resposta = chain.invoke({'documento_site': conteudo_pdf, 'input': 'Informe dados do documento disponibilizado, quero informações como docigo de barras, codigo da instalação/unidade consumidora/conta contrato, valor a pagar, vencimento, emissao, numero da nota fiscal e mes refencia'})

print(resposta.content)



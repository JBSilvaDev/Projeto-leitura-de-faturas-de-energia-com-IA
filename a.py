from langchain.prompts import ChatPromptTemplate
from models import configureIA as config

for arquivo in config.pdfs_pendentes:
    pdf = config.Path(rf"{config.caminho}/{arquivo}")
    loader = config.PyPDFLoader(pdf)
    dados_pdf = loader.load()
    for doc in dados_pdf:
        config.conteudo_pdf += doc.page_content
    template = ChatPromptTemplate.from_messages([
        (
            "system",
            "Voce é um assistente chamado J-bote, e a partir de agora tem acesso ao {conteudo_pdf}"
        ),
        ('user', '{input}'),
    ])

    chain = template | config.chat

    resposta = chain.invoke({'conteudo_pdf': config.conteudo_pdf, 'input': 'Informe dados do documento disponibilizado, quero informações como distribuida, codigo de barras, codigo da instalação/unidade consumidora/conta contrato, valor a pagar, vencimento, emissao, numero da nota fiscal e mes refencia, traga estas informações em formato de tabela'})

    print(resposta.content)
    break
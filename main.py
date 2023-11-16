from fastapi import FastAPI
from langchain.llms import OpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import ChatOpenAI
from prompt import getTemplate, getPrompt

app = FastAPI()

@app.get("/api")
def root(conversation_id: int, question: str):

    template = getTemplate()
    prompt = getPrompt(template)

    llm = ChatOpenAI(openai_api_key = "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")
    print("Id ", conversation_id, " ", question)
    chain = prompt | llm
    capital =  chain.invoke({"input": "what is the capital of bangladesh?"})
    return {"hello": capital}

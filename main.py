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
    chain = prompt | llm
    ans =  chain.invoke({"input": question})
    return {conversation_id: ans.content}

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import ChatGPTAPI
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title= "Langchain Server",
    version= "0.1.0",
    description= "A simple API server using Langchain"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"

)
model=ChatGPTAPI()
llm = ChatOpenAI(model_name="openai")

prompt1 = ChatPromptTemplate.from_template("Write a short story about {topic}.")
prompt2 = ChatPromptTemplate.from_template("Write a poem about {topic}.")

add_routes(
    app,
    prompt1|model,
    path = "/essay"
)

add_routes(
    app,
    prompt2|llm,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)





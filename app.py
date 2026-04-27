import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groq_llm import GroqLLLM

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

@app.post("/blogs")
async def generate_blog(request: Request):
    data=await request.json()
    topic = data.get("topic", "")

    # get llm onject
    groqllm = GroqLLLM()
    llm = groqllm.get_llm()

    # get graph builder object
    graph_builder = GraphBuilder(llm)
    if topic:
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.run({"topic": topic})

        return {"data": state}
    

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
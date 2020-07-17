from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from qa.qa_pipeline import QAPipeline

qa = QAPipeline()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index(request: Request):
    return {'status': 'up'}


@app.post("/remote")
async def remote_data(data_url: str):
    return qa.add_to_datastore_from_remote(data_url)


@app.get("/arxiv")
async def seed_arxiv_data(request: Request):
    return qa.add_to_datastore_local('./arxivData.json')


@app.post("/qa")
async def get_answer(question: str):
    res = qa.answer(question)
    return {'question': question, 'answers': res}

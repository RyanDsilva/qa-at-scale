from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from qa.qa_pipeline import QAPipeline

pipeline = QAPipeline()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.get("/")
async def index():
    return {'status': 'up'}


@app.post("/remote")
async def remote_data(data_url: str):
    return pipeline.add_to_datastore_from_remote(data_url)


@app.get("/arxiv")
async def seed_arxiv_data():
    return pipeline.add_to_datastore_local('./qa/arxivData.json')


@app.post("/qa")
async def get_answer(question: Question):
    res = pipeline.answer(question.question)
    return {'question': question, 'answers': res}

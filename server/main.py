from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

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


@app.post("/data")
async def upload_data(file: UploadFile = File(...)):
    return {'file': file.filename}


@app.post("/qa")
async def qa(question: str):
    return {'question': question}

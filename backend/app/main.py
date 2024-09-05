from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
import os
import pdfminer
from elasticsearch import Elasticsearch
from langchain import LangChain
from .utils import extract_text_from_pdf, chunk_text, process_question

app = FastAPI()
es = Elasticsearch()
lc = LangChain()

class Question(BaseModel):
    question: str

@app.post("/upload/")
async def upload_files(files: List[UploadFile]):
    try:
        texts = []
        for file in files:
            text = extract_text_from_pdf(file.file)
            chunks = chunk_text(text)
            # Store text chunks and metadata in PostgreSQL here
            # Example: save_text_chunks_to_db(chunks)
        return {"message": "Files processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask/")
async def ask_question(question: Question):
    try:
        response = process_question(question.question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

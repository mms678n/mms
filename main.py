
# main.py
from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ذكاء اصطناعي محمود جاهز"}

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    return {"filename": file.filename, "content_type": file.content_type}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

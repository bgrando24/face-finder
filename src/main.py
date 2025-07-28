from fastapi import FastAPI

# init app
app = FastAPI()

# basic test
@app.get("/")
async def get_root():
    return {"message": "Hello world!"}
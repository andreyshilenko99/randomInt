import random
from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/random")
async def generate_random_number():
    data = {"random_number": random.randint(0, 100)}
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=data, headers=headers)


@app.get("/")
async def root():
    return FileResponse('templates/index.html')

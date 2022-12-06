import random

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.responses import JSONResponse
from starlette.responses import FileResponse

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/random")
async def generate_random_number():
    data = {"random_number": random.randint(0, 100)}
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=data, headers=headers)


@app.get("/")
async def root():
    return FileResponse('templates/index.html')


if __name__ == '__main__':
    uvicorn.run("main:app", port=443, host='0.0.0.0', reload = True, ssl_keyfile="~/openssl/server.key",
                ssl_certfile="~/openssl/server.crt")


import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from message_model import MessageModel
from message_service import create_message, load_messages

from model import FamilyModel
from service import confirm_family, get_list

app = FastAPI()
load_dotenv() 

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/list")
async def req_get_list():
    return get_list()


@app.post("/confirmation")
async def req_confirmation(family: FamilyModel):
    confirm_family(family)
    return True


@app.post("/message")
async def save_message(message: MessageModel):
    create_message(message)


@app.get("/messages")
async def get_messages():
    return load_messages()


if __name__ == '__main__':
    if (os.environ["ENV"] == 'prod'):
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True,
                    ssl_keyfile="privkey.pem",
                    ssl_certfile="cert.pem"
                    )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True
                    )

from datetime import datetime
from os import environ
import os
import uuid
from firebase_admin import firestore
from message_model import MessageModel
from firebase_admin import credentials
from firebase_admin import initialize_app


cred = credentials.Certificate("auth.json")
initialize_app(cred)

# cred = credentials.ApplicationDefault()
# initialize_app(cred, {
#     'projectId': "coralina",
# })

db = firestore.client()


def create_message(message: MessageModel):
    doc_ref = db.collection(u'messages').document(str(uuid.uuid4()))

    doc_ref.set({
        u'author': message.author,
        u'text': message.text,
    })

    return True


def load_messages():
    doc_ref = db.collection(u'messages').get()
    messages = []
    for message in doc_ref:
        messages.append(message.to_dict())
    return messages

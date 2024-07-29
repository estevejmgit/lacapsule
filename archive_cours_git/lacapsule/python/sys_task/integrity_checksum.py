import hashlib
import os

survey = "./survey/encrypt.me"
empreintes = {}

def get_empreintes(path):
    initial_hash = hashlib.sha256(path.encode())
    final_hash = initial_hash.hexdigest()
    empreintes.append(final_hash) 


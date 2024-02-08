import time 
import hashlib 

def create_hash():
    return hashlib.sha256(str(time.time()).encode()).hexdigest()
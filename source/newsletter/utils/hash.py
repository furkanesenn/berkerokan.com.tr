import time 
import hashlib 

def create_hash(key: str = time.time):
    return hashlib.sha256(str(key).encode()).hexdigest()
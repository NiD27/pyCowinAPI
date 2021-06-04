import hashlib

def get_sha256(message):
    result = hashlib.sha256()
    result.update(str(message).encode('utf-8'))
    return result.hexdigest()
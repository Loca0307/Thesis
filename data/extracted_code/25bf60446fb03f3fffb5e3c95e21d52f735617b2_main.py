    return {'token': string}


class Text(BaseModel):
    text: str

# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called "text" and returns a checksum of the text.
# The checksum should be a SHA-256 hash of the text encoded in base64.
# The endpoint should return a JSON response with a single field called "checksum" containing the base64-encoded checksum.
@app.post('/checksum')
def checksum(text: Text):
    import hashlib
    checksum = hashlib.sha256(text.text.encode()).digest()
    return {'checksum': base64.b64encode(checksum).decode()}

@app.get("/")
def home():
    return {
        "message": "Welcome to Library API"
    }

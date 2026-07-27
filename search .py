#GET /title
@app.get("/search")
def search_book(title: str):
    result = []

    for book in books:
        if title.lower() in book["title"].lower():
            result.append(book)

    return result

@app.post("/books")
def add_book(book: Book):
    books.append(book.model_dump())
    return {
        "message": "Book Added Successfully",
        "book": book
    }

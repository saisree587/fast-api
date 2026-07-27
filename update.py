@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: int):

    for book in books:

        if book["id"] == book_id:

            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["publish_date"] = updated_book.publish_date

            return {
                "message": "Book Updated Successfully",
                "book": book
            }

    return {"message": "Book not found"}

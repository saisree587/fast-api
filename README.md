fast-api
bash
uvicorn main:app --reload

API: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc


GET    http://127.0.0.1:8000/
GET    http://127.0.0.1:8000/books
GET    http://127.0.0.1:8000/books/1
GET    http://127.0.0.1:8000/search?title=Python
POST   http://127.0.0.1:8000/books
PUT    http://127.0.0.1:8000/books/1
DELETE http://127.0.0.1:8000/books/1



req body 
{
  "id": 3,
  "title": "Deep Learning",
  "author": "Andrew Ng",
  "publish_date": "2026"
}

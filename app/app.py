from flask import Flask, jsonify, request
from google.cloud import firestore
import os
#from model.book import Book
import uuid
# Initialize Flask application
app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
collection = app.config['COLLECTION']
# Initialize Firestore Client
db = firestore.Client()
#app.testing = True
class Book:
    def __init__(self, isbn, title, description, authors, categories, publisher):
        """
        """
        if isinstance(authors, str):
            self.authors = [authors]
        else:
            self.authors = authors
        if isinstance(categories, str):
            self.categories = [categories]
        else:
            self.categories = categories
        self.isbn = isbn
        self.title = title
        self.description = description
        self.publisher = publisher


    def __repr__(self):
        return f"Book(ISBN={self.isbn}, Title={self.title})"
    
    @staticmethod
    def from_dict(data):
        if not isinstance(data, dict):
            raise Exception("Invalid book data")
        book = Book(data['isbn'], data['title'], data['description'],
                    data['authors'], data['categories'], data['publisher'])
        
        return book
    
    def to_dict(self):
        data = {
            "isbn": self.isbn, "title": self.title, "description": self.description, 
            "authors": self.authors, "categories": self.categories, "publisher": self.publisher
        }
        return data
    

 


# Define a route for testing purposes
@app.route('/')
def info():
    return 'Hello! This is a Flask application running on Google Cloud Run.'

@app.route('/add-book', methods=['POST'])
def add_book():
    new_book = request.json
    try:
        book = Book.from_dict(new_book)
    except:
        return jsonify({"message": "Invalid book details"}), 400
    
    books_ref = db.collection(collection)
    ## generate uuid for document id
    doc_id = str(uuid.uuid1())

    result = books_ref.document(doc_id).set(new_book)

    return jsonify({"book_id": doc_id}), 201

@app.route('/get-books', methods=['GET'])
def get_books():
    books_ref = db.collection(collection)
    books = [doc.to_dict() for doc in books_ref.stream()]
    return jsonify(books), 200

@app.route('/update-book/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    update_data = request.json
    if not update_data:
        return jsonify({"message": "Missing book data"}), 400

    book_ref = db.collection(collection).document(book_id)
    book = book_ref.get()
    if not book.exists:
        return jsonify({"message": "Book not found"}), 400
    

    result = book_ref.update(update_data)
    updated_details = book_ref.get()
    return jsonify(updated_details.to_dict()), 200


@app.route('/get-book/<string:book_id>', methods=['GET'])
def get_book(book_id):

    book_ref = db.collection(collection).document(book_id)
    book = book_ref.get()
    if not book.exists:
        return jsonify({"message": "Book not found"}), 400
    
    return jsonify(book.to_dict()), 200

@app.route('/delete-book/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_ref = db.collection(collection).document(book_id)
    result = book_ref.delete()
    return jsonify({"message": "Book deleted successfully"}), 200



@app.route('/books/search', methods=['GET'])
def search_books():
    return jsonify({"message": "This feature is not implemented yet!"}), 200
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
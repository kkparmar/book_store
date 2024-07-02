# Book Store Backend App
Repo to host a simple flask based bookstore backend app
This application is intended to run in GCP cloud run environment with firestore database backend.

### How is the repo structured
```

├───app         // main app folder
│   ├───app.py  // flask application
|
├───infrastructure  // code for infrastructure resources
|   |
│   └───terraform
|
├───tests     // Directory where all the unit tests are present
|   |
│   └───test_data.josn    // some test data

```

## APIs

### Print welcome message

Endpoint: /

Method: GET

Response: Welcome message

### Add a book
Endpoint: /add-book

Method: POST

Request Body:  JSON payload of book to be added
Sample request:
```
{
            "isbn": "9781593279509",
            "title": "Eloquent JavaScript, Third Edition",
            "authors": "Marijn Haverbeke",
            "publisher": "No Starch Press",
            "categories": [
                "Non-Fiction",
                "Technology"
            ],
            "description": "JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications."
}
```
Response: UUID of the book added 

Sample Response: `{'book_id': '6bad884f-367d-11ef-8cdd-2c3358935ef3'}`

### Get all books

Endpoint: /get-books

Method: GET

Response: list of all the books

Sample Response:
```[{
            "isbn": "9781593279509",
            "title": "Eloquent JavaScript, Third Edition",
            "authors": "Marijn Haverbeke",
            "publisher": "No Starch Press",
            "categories": [
                "Non-Fiction",
                "Technology"
            ],
            "description": "JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications."
}]
```

### Update a book

Endpoint: /update-book/<uuid>

Method: PUt

Request Body:  JSON payload of book attributes to be updated
Sample request:
```
{
            "authors": "Marijn Haverbeke",
            "publisher": "No Starch Press",
}
```
Response: Book details

Sample Response:
```
{
            "isbn": "9781593279509",
            "title": "Eloquent JavaScript, Third Edition",
            "authors": "Marijn Haverbeke",
            "publisher": "No Starch Press",
            "categories": [
                "Non-Fiction",
                "Technology"
            ],
            "description": "JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications."
}
```

### Delete a book

Endpoint: /delete-book/<uuid>

Method: DELETE

Request Body:  `None`

Response: `None`



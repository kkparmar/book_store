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


## Infrastructure

This application runs as a GCP Cloud Run application with Firestore database.

Most of the infrastructure is defined in terraform. Infrastructure and app deployment are done via GCP Cloud Build servicer.

However, following resources were created via clickOps to enable terraform and pipelines:
- Enable essential GCP services:
    - cloudbuild
    - secretmanager
- Integrate GitHub with CloudBuild
- Terraform Service Account

### Database

The application uses `(default)` database. The application uses `bookstore` collection and python automated tests uses `bookstore_test` collection and these are defined in `prodenv` and `testenv` configuration files

## How to run application locally

To run and test the application locally, perform the following steps:

- Ensure python 3.11 or higher is installed
- Clone the repository
- Create a python virtual env
    ```
    python -m venv venv
    ```
- Activate the venv
    ```
    Windows:
    .\venv\Scripts\activate

    Linux or Mac:
    . ./venv/Scripts/activate
    ```
- Install required python dependencies
    ```
    pip install -r requirements.txt
    ```

- Export `ENV_FILE_LOCATION` variable
    ```
    Windows:
    set ENV_FILE_LOCATION=testenv

    Linux or Mac:
    export ENV_FILE_LOCATION=testenv
    ```

- Run the application:
    ```
    python app/app.py
    ```

## Running automated tests:
    ```
    (venv) xxxxxxxxxxxxxxxxx>python -m pytest --cov app
    ================================================= test session starts =================================================
    platform win32 -- Python 3.11.2, pytest-8.2.2, pluggy-1.5.0
    rootdir: xxxxxxxxxxxxxxxxxxx
    configfile: pytest.ini
    plugins: cov-5.0.0, env-1.1.3, order-1.2.1
    collected 6 items

    tests\test_app.py ...                                                                                            [ 50%]
    tests\test_book.py ...                                                                                           [100%]

    ---------- coverage: platform win32, python 3.11.2-final-0 -----------
    Name                    Stmts   Miss  Cover
    -------------------------------------------
    app\.env.test               1      0   100%
    app\app.py                 79      9    89%
    -------------------------------------------
    TOTAL                      81     10    88%


    ================================================== 6 passed in 3.18s ==================================================
    ```


    TODO:
    GCP filestore does not support partial text search and needs integrated with 3rd party tool like Elastic so its probably not the best database for this requirement

    For next version, need to move the database to cloudsql relational DB which has better support for search and filter requirements
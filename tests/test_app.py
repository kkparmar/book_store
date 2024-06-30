import app.app as application
import json
from uuid import UUID
import unittest, pytest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = application.app.test_client()


    def test_info(self):
      #  response1 = test_app.test_client().get('/')
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response.text, "Hello! This is a Flask application running on Google Cloud Run.")

    @pytest.mark.order(1)
    def test_get_books(self):
       response = self.client.get('/get-books')
       self.assertEqual(response.status_code, 200)
       self.assertIsInstance(response.json, list)

    @pytest.mark.order(2)
    def test_book_operations(self):
        with open("tests\\test_data.json") as f:
            data = json.load(f)
        book_data = data['books'][0]
        response = self.client.post('/add-book', headers={"Content-Type": "application/json"}, data=json.dumps(book_data))
        result = response.json
        ## validate if result has key book_id
        self.assertIsNotNone(result.get('book_id',None))
        book_id = None
        ## check if book_id is valid UUID
        try:
            book_id = UUID(result.get('book_id'), version=1)

        except:
            pass

        self.assertIsNotNone(book_id)

        ## attempt to read the book details just created

        get_endpoint = f"/get-book/{book_id}"
        response = self.client.get(get_endpoint)
        self.assertDictEqual(response.json, book_data)

        ## update book

        book_data['authors'] = ["John Doe"]
        put_endpoint = f"/update-book/{book_id}"
        response = self.client.put(put_endpoint, headers={"Content-Type": "application/json"}, data=json.dumps(book_data))
        self.assertDictEqual(response.json, book_data)

        ## delete the book
        delete_endpoint = f"/delete-book/{book_id}"
        response = self.client.delete(delete_endpoint)
        self.assertEqual(response.json['message'], "Book deleted successfully")

        
